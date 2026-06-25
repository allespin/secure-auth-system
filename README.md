#### [PORTUGUESE/ ENGLISH]

# 🔐 Sistema de login, cadastro e autenticação de usuários 

Sistema de autenticação desenvolvido em Python com Flask, disponibilizado como aplicação web. O sistema oferece cadastro de usuários, login seguro, recuperação de senha por meio de token de 8 caracteres e gerenciamento de sessões autenticadas.

Entre os recursos implementados estão proteção contra tentativas de força bruta com bloqueio após múltiplas falhas de autenticação, armazenamento seguro de credenciais e comunicação entre cliente e servidor por meio de API REST.

A interface adota uma estética inspirada em terminais de comando, proporcionando uma experiência visual diferenciada sem comprometer a usabilidade.



## 📸 Preview
### Tela inicial
<img width="1706" height="816" alt="image" src="https://github.com/user-attachments/assets/73cc7998-1dad-47f7-bd98-895196c934ad" />



### 1. Tela de login
Tela de login e usuário não encontrado.

<div align="center">
  <table>
    <tr>
      <td><img alt="1" src="https://github.com/user-attachments/assets/179e0f0f-2b46-4b43-b6c4-08b0009d633c" width="400"></td>
      <td><img alt="2" src="https://github.com/user-attachments/assets/7c1be4ac-a37f-4a52-af1a-e8fdd1d85ac2" width="400"></td>
    </tr>
  </table>
</div>

---

### 2. Tela de cadastro
Tela de cadastro e usuário cadastrado com sucesso

<div align="center">
  <table>
    <tr>
      <td><img alt="3" src="https://github.com/user-attachments/assets/a7be2ec6-a152-4f9b-8d46-0eae6377701f" width="400"></td>
      <td><img alt="4" src="https://github.com/user-attachments/assets/fcf8a428-5801-43cf-9fdb-eba4f238460e" width="400"></td>
    </tr>
  </table>
</div>

---

### 3. Senha incorreta e bloqueio temporário de conta

Após o usuário inserir três vezes uma senha errada sua conta sofre um bloqueio de 30s.
<div align="center">
  <table>
    <tr>
      <td><img alt="5" src="https://github.com/user-attachments/assets/ad6ffca1-fd57-4682-b5af-39873476f2a7" width="400"></td>
      <td><img alt="5-1" src="https://github.com/user-attachments/assets/df981b9a-4437-4b07-83db-ceb2ff1e3979" width="350"></td>
    </tr>
  </table>
</div>

---

### 4. Recuperação de senha e envio de token

<div align="center">
  <table>
    <tr>
      <td><img alt="5-2" src="https://github.com/user-attachments/assets/c33b0746-b963-4f12-af31-0bece382cd4c" width="400"></td>
      <td><img alt="6" src="https://github.com/user-attachments/assets/fda149e3-065a-4c54-9ab6-896bdcb5a9b7" width="350"></td>
    </tr>
  </table>
</div>



### 5. Mensagem de boas vindas ao usuário e autenticação da conta no sistema.

<div align="center">
  <table>
    <tr>
      <td><img alt="7" src="https://github.com/user-attachments/assets/d40c1812-6e7f-416e-a035-09fd68170f6b" width="400"></td>
      <td><img alt="8" src="https://github.com/user-attachments/assets/6efda7e4-6081-42d4-af2e-755c4709c790" width="400"></td>
    </tr>
  </table>
</div>

---

## ✨ Funcionalidades

### 🌐 Web Interface (Flask)

* Páginas de login, cadastro, recuperação de senha e dashboard
* Tema terminal com fontes Rajdhani e Roboto Mono, fundo escuro e efeito scanlines
* Comunicação via API REST utilizando JSON
* Gerenciamento de sessão com `flask.session`
* Interface responsiva para desktop e dispositivos móveis

### 🛡️ Segurança

* Aplicação de hash SHA-256 para armazenamento de senhas e tokens
* Limite de tentativas de login com bloqueio após 3 erros consecutivos
* Bloqueio temporário de 30 segundos após exceder o limite de tentativas
* Recuperação de senha por token gerado aleatoriamente e validado via hash
* Invalidação automática do token após a redefinição da senha

---

## 📁 Estrutura do projeto

```
login-register-system/
├── app.py                  # Backend Flask (rotas e API)
├── requirements.txt        # Dependências
├── usuarios.json           # Banco de dados local (gerado automaticamente)
└── templates/
    ├── base.html           # Layout base com tema terminal
    ├── login.html
    ├── cadastro.html
    ├── recuperar.html
    └── dashboard.html
```

---

## 🚀 Como rodar

### Pré-requisitos
- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/allespin/login-register-auth-system-python-and-flask
cd login-register-system-python-and-flask

# Instale as dependências
pip install -r requirements.txt
```

### Rodando o sistema

```bash
python app.py
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Como usar

### Cadastro
1. Escolha a opção **Cadastrar**
2. Informe nome de usuário, senha e e-mail
3. Confirme a senha

### Login
1. Informe nome de usuário e senha
2. Após **3 tentativas erradas**, a conta é bloqueada por **30 segundos**

### Recuperação de senha
1. Informe o nome de usuário
2. Um token de 8 caracteres é gerado e "enviado" ao e-mail cadastrado
3. Insira o token para validar e redefinir a senha

> ⚠️ Em produção: o token simula o envio do código por serviço de e-mail.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| Flask | Web framework |
| SHA-256 (hashlib) | Hash de senhas e tokens |
| JSON | Armazenamento de usuários |
| Jinja2 | Templates HTML |
| HTML/CSS/JS | Front-end da interface web |

---

## 📌 Observações

- O arquivo `usuarios.json` é criado automaticamente na primeira execução
- A `secret_key` do Flask deve ser trocada por uma chave segura em produção
- O sistema não usa banco de dados externo

---

# 🔐 Login & user register system — English

A complete authentication system built in Python, available a web app via Flask.
Supports user registration, secure login, and password recovery through an 8-character token.
Passwords are stored with SHA-256 hashing and brute-force protection locks the account after 3 failed attempts.
The web interface features a terminal-style theme, REST API communication, and authenticated sessions.

---

## ✨ Features

### 🌐 Web Interface (Flask)
- Login, register, password recovery and dashboard pages
- **Terminal** theme with Rajdhani e Mono font, dark background and scanline effect
- REST API communication in JSON
- User session with `flask.session`
- Responsive and fully functional design

### 🛡️ Security
- **SHA-256 hashing** on all passwords and tokens
- **Login attempt limit** — account locked after 3 consecutive failures
- **Temporary lockout** of 30 seconds after exceeding the limit
- **Token-based password recovery** — randomly generated and validated via hash
- Token invalidated after use

---

## 📁 Project Structure

```
login-register-system/
├── app.py                  # Flask backend (routes and API)
├── requirements.txt        # Dependencies
├── usuarios.json           # Local database (auto-generated)
└── templates/
    ├── base.html           # Base layout with terminal theme
    ├── login.html
    ├── cadastro.html
    ├── recuperar.html
    └── dashboard.html
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/allespin/login-register-system-python-and-flask
cd login-register-system-python-and-flask

# Install dependencies
pip install -r requirements.txt
```

### Run the system

```bash
python app.py
```

Access at: [http://localhost:5000](http://localhost:5000)

---

## 🧪 How to Use

### Register
1. Choose the **Register** option
2. Enter username, password and email
3. Confirm your password

### Login
1. Enter your username and password
2. After **3 wrong attempts**, the account is locked for **30 seconds**

### Password Recovery
1. Enter your username
2. An 8-character token is generated and "sent" to the registered email
3. Enter the token to validate and reset your password

> ⚠️ In production: the token simulates delivery of the code via an email service.

---

## 🛠️ Technologies

| Technology | Usage |
|---|---|
| Python 3 | Main language |
| Flask | Web framework |
| SHA-256 (hashlib) | Password and token hashing |
| JSON | User storage |
| Jinja2 | HTML templates |
| HTML/CSS/JS | Front-end web interface |

---

## 📌 Notes

- The `usuarios.json` file is created automatically on first run
- The Flask `secret_key` should be replaced with a secure key in production
- The system uses no external database
