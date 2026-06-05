from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
import hashlib
import random
import string
import time

app = Flask(__name__)
app.secret_key = "chave_secreta_de_sistema"

ARQUIVO_USUARIOS = "usuarios.json"
MAX_TENTATIVAS = 3
TEMPO_BLOQUEIO = 30

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def gerar_token(tamanho=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=tamanho))

# ── Rotas de página ──────────────────────────────────────────────────────────

@app.route("/")
def index():
    if "usuario" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login_page"))

@app.route("/login")
def login_page():
    if "usuario" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/cadastro")
def cadastro_page():
    return render_template("cadastro.html")

@app.route("/recuperar")
def recuperar_page():
    return render_template("recuperar.html")

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login_page"))
    return render_template("dashboard.html", usuario=session["usuario"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_page"))

# ── API ──────────────────────────────────────────────────────────────────────

@app.route("/api/cadastrar", methods=["POST"])
def api_cadastrar():
    dados = request.json
    nome = dados.get("nome", "").strip()
    senha = dados.get("senha", "").strip()
    confirmacao = dados.get("confirmacao", "").strip()
    email = dados.get("email", "").strip()

    if not all([nome, senha, confirmacao, email]):
        return jsonify({"ok": False, "msg": "Preencha todos os campos."})

    usuarios = carregar_usuarios()

    if nome in usuarios:
        return jsonify({"ok": False, "msg": "Usuário já existe."})

    if senha != confirmacao:
        return jsonify({"ok": False, "msg": "As senhas não coincidem."})

    usuarios[nome] = {
        "senha": hash_senha(senha),
        "email": email,
        "tentativas": 0,
        "bloqueado_ate": 0,
        "token_recuperacao": None
    }
    salvar_usuarios(usuarios)
    return jsonify({"ok": True, "msg": f"Usuário '{nome}' cadastrado com sucesso!"})


@app.route("/api/login", methods=["POST"])
def api_login():
    dados = request.json
    nome = dados.get("nome", "").strip()
    senha = dados.get("senha", "").strip()

    usuarios = carregar_usuarios()

    if nome not in usuarios:
        return jsonify({"ok": False, "msg": "Usuário não encontrado."})

    usuario = usuarios[nome]
    agora = time.time()

    if usuario.get("bloqueado_ate", 0) > agora:
        restante = int(usuario["bloqueado_ate"] - agora)
        return jsonify({"ok": False, "msg": f"Conta bloqueada. Tente em {restante}s."})

    if usuario["senha"] == hash_senha(senha):
        usuario["tentativas"] = 0
        usuario["bloqueado_ate"] = 0
        salvar_usuarios(usuarios)
        session["usuario"] = nome
        return jsonify({"ok": True, "msg": f"Bem-vindo, {nome}!"})
    else:
        usuario["tentativas"] = usuario.get("tentativas", 0) + 1
        restantes = MAX_TENTATIVAS - usuario["tentativas"]

        if usuario["tentativas"] >= MAX_TENTATIVAS:
            usuario["bloqueado_ate"] = time.time() + TEMPO_BLOQUEIO
            usuario["tentativas"] = 0
            salvar_usuarios(usuarios)
            return jsonify({"ok": False, "msg": f"Conta bloqueada por {TEMPO_BLOQUEIO}s."})
        else:
            salvar_usuarios(usuarios)
            return jsonify({"ok": False, "msg": f"Senha incorreta. Tentativas restantes: {restantes}."})


@app.route("/api/recuperar/solicitar", methods=["POST"])
def api_recuperar_solicitar():
    dados = request.json
    nome = dados.get("nome", "").strip()

    usuarios = carregar_usuarios()

    if nome not in usuarios:
        return jsonify({"ok": False, "msg": "Usuário não encontrado."})

    token = gerar_token()
    usuarios[nome]["token_recuperacao"] = hash_senha(token)
    salvar_usuarios(usuarios)

    email = usuarios[nome]["email"]
    # Em produção: enviar por e-mail. Aqui retorna a  resposta para simulação.
    return jsonify({"ok": True, "msg": f"Token enviado para {email}.", "token_simulado": token})


@app.route("/api/recuperar/confirmar", methods=["POST"])
def api_recuperar_confirmar():
    dados = request.json
    nome = dados.get("nome", "").strip()
    token = dados.get("token", "").strip()
    nova_senha = dados.get("nova_senha", "").strip()
    confirmacao = dados.get("confirmacao", "").strip()

    usuarios = carregar_usuarios()

    if nome not in usuarios:
        return jsonify({"ok": False, "msg": "Usuário não encontrado."})

    if usuarios[nome].get("token_recuperacao") != hash_senha(token):
        return jsonify({"ok": False, "msg": "Token inválido."})

    if nova_senha != confirmacao:
        return jsonify({"ok": False, "msg": "As senhas não coincidem."})

    usuarios[nome]["senha"] = hash_senha(nova_senha)
    usuarios[nome]["token_recuperacao"] = None
    usuarios[nome]["tentativas"] = 0
    usuarios[nome]["bloqueado_ate"] = 0
    salvar_usuarios(usuarios)
    return jsonify({"ok": True, "msg": "Senha alterada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
