# 🏥 Clinic Data Viewer

> **MVP — Sistema de gerenciamento de fichas clínicas de emergência**

O **Clinic Data Viewer** é um sistema web desenvolvido para o gerenciamento de **informações clínicas essenciais**, permitindo que dados médicos importantes sejam acessados rapidamente em situações de emergência por meio de um **QR Code**.

O acesso às informações é protegido por um **PIN de segurança definido pelo próprio usuário**, garantindo uma camada adicional de privacidade e controle sobre seus dados.

---

## 🚀 Funcionalidades

* 👤 Cadastro e autenticação de usuários
* 🩺 Cadastro e edição de informações clínicas
* 🔐 Proteção da ficha médica por PIN
* 📱 Geração de QR Code exclusivo para cada usuário
* 🚨 Acesso rápido às informações em situações de emergência
* 📋 Visualização da ficha médica em modo de alta legibilidade
* 📥 Download do QR Code para impressão ou uso digital
* ✏️ Edição dos dados clínicos
* 🗑️ Exclusão definitiva da conta e dos dados associados
* 🔒 Controle de acesso às informações médicas

---

## 🛠️ Tecnologias utilizadas

| Tecnologia            | Utilização                      |
| --------------------- | ------------------------------- |
| 🐍 **Python 3.10**    | Linguagem principal             |
| 🌐 **Django 5.2**     | Framework web / Backend         |
| 🐘 **PostgreSQL 15**  | Banco de dados                  |
| 🐳 **Docker**         | Containerização                 |
| 🐳 **Docker Compose** | Orquestração dos containers     |
| 🎨 **MDBootstrap**    | Interface e componentes visuais |
| 🔳 **qrcode**         | Geração dos QR Codes            |
| 🖼️ **Pillow**         | Processamento de imagens        |

---

# 🐳 Como executar a aplicação

A aplicação foi preparada para ser executada utilizando **Docker e Docker Compose**, facilitando a configuração do ambiente.

### Pré-requisitos

Certifique-se de ter instalado:

* [Docker](https://www.docker.com/)
* Docker Compose

---

### 1️⃣ Clone o repositório

```bash
git https://github.com/ThiagorPassos/clinic-data-viewer
```

---

### 2️⃣ Suba os containers

Execute:

```bash
docker compose up -d --build
```

Esse comando irá construir as imagens necessárias e iniciar os containers da aplicação.

---

### 3️⃣ Execute as migrações

Com os containers em execução:

```bash
docker compose exec web python manage.py migrate
```

---

### 4️⃣ Acesse a aplicação

Abra seu navegador e acesse:

**http://localhost:8000/**

---

# 🖥️ Telas e fluxo do sistema

O sistema possui um fluxo integrado dividido em **quatro áreas principais**.

---

## 1. 🔐 Login e Cadastro

**Rotas:**

```text
/login/
/cadastro/
```

O usuário pode:

* Entrar utilizando suas credenciais;
* Criar uma nova conta;
* Realizar login automaticamente após o cadastro.

Após o primeiro cadastro, o sistema direciona o usuário para o preenchimento inicial de suas informações clínicas.

---

## 2. 🩺 Formulário Clínico

**Rota:**

```text
/formulario/
```

Permite cadastrar ou editar a ficha médica do usuário.

### Informações disponíveis

* Nome completo
* Tipo sanguíneo
* Telefone de emergência
* Alergias
* Doenças crônicas
* Medicamentos de uso contínuo
* Cirurgias prévias
* PIN de segurança

O **PIN de segurança** é utilizado para restringir o acesso de terceiros às informações médicas.

---

## 3. 📊 Dashboard do Usuário

**Rota:**

```text
/
```

ou

```text
/dashboard/
```

O dashboard centraliza as principais funcionalidades do usuário.

### 👤 Perfil

Permite visualizar as informações cadastradas e consultar a data da última atualização da ficha.

### 🔳 QR Code de emergência

Cada usuário possui um **QR Code exclusivo**, gerado pelo sistema.

O QR Code pode ser:

* Visualizado diretamente no sistema;
* Baixado como imagem;
* Impresso;
* Utilizado digitalmente, por exemplo, na tela de bloqueio de um celular.

### ✏️ Gerenciamento

O usuário pode editar suas informações clínicas ou excluir sua conta.

> ⚠️ **A exclusão da conta é uma ação destrutiva.** O usuário e todos os dados clínicos associados são removidos definitivamente do banco de dados.

### 🚪 Logout

Permite encerrar a sessão do usuário de forma segura.

---

## 4. 🚨 Acesso de Emergência

**Rota:**

```text
/emergencia/id/
```

Essa área foi projetada para situações em que um socorrista precisa consultar rapidamente as informações médicas de um paciente.

### 🔳 1. Leitura do QR Code

O socorrista acessa a página através do QR Code associado ao paciente.

### 🔐 2. Validação do PIN

Antes de visualizar os dados, é necessário informar o **PIN numérico definido pelo paciente**.

### 🩺 3. Ficha Médica de Urgência

Após a validação do PIN, o sistema apresenta uma interface de **alto contraste e leitura rápida**, priorizando informações relevantes em situações de emergência:

* 🩸 Tipo sanguíneo
* 📞 Contato de emergência
* ⚠️ Alergias
* 🩺 Doenças crônicas
* 💊 Medicamentos em uso

O objetivo é facilitar a identificação das informações essenciais em situações nas quais **tempo e legibilidade são fatores importantes**.

---

# 🎯 Objetivo do projeto

O **Clinic Data Viewer** busca demonstrar como tecnologias web podem ser utilizadas para disponibilizar **informações médicas essenciais de forma rápida e controlada**, utilizando QR Codes como mecanismo de acesso e um PIN como camada adicional de segurança.

O projeto também serve como MVP para exploração de conceitos relacionados a:

* Desenvolvimento Web;
* APIs e sistemas backend;
* Banco de dados relacionais;
* Containerização;
* Autenticação;
* Segurança da informação;
* UX/UI;
* Acessibilidade e legibilidade em situações críticas.

---

## 👨‍💻 Status do projeto

**🚧 MVP — Em desenvolvimento**

Novas funcionalidades, melhorias de segurança, acessibilidade e experiência do usuário podem ser adicionadas conforme a evolução do projeto.

---

## 📄 Licença

Este projeto está em desenvolvimento para fins **acadêmicos e experimentais**.

---

<div align="center">

### 🏥 Clinic Data Viewer

**Informação certa. No momento certo.**

</div>
