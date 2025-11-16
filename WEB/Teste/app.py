from flask import Flask, request, redirect, url_for, flash, get_flashed_messages
import psycopg2
import os

# --- 1. CONFIGURAÇÃO DO BANCO DE DADOS (DAO SIMPLIFICADO) ---

# SUBSTITUA AQUI com suas credenciais do PostgreSQL!
DB_HOST = "localhost"
DB_NAME = "empresa"
DB_USER = "postgres"
DB_PASS = "123456"
SECRET_KEY = os.urandom(24) # Chave secreta para segurança e flash messages

class CadastroDAO:
    """DAO para gerenciar a conexão e operações no PostgreSQL."""

    def __init__(self):
        self._conectar()
        self._criar_tabela()

    def _conectar(self):
        """Tenta estabelecer a conexão."""
        try:
            self.conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("Conexão com PostgreSQL estabelecida.")
        except psycopg2.Error as e:
            print(f"ERRO DE CONEXÃO: Verifique as credenciais e se o PostgreSQL está rodando. {e}")
            raise RuntimeError("Falha ao conectar ao banco de dados.")

    def _criar_tabela(self):
        """Cria a tabela 'tabela_web' se ela não existir."""
        create_table_query = """
            CREATE TABLE IF NOT EXISTS tabela_web (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            );
        """
        try:
            self.cursor.execute(create_table_query)
            print("Tabela 'tabela_web' verificada/criada.")
        except psycopg2.Error as e:
            print(f"Erro ao criar a tabela: {e}")
            raise e

    def inserir_registro(self, nome, email):
        """Insere um novo registro (nome, email) na tabela."""
        insert_query = """
            INSERT INTO tabela_web (nome, email) VALUES (%s, %s) RETURNING id;
        """
        try:
            self.cursor.execute(insert_query, (nome, email))
            registro_id = self.cursor.fetchone()[0]
            return registro_id # Sucesso, retorna o ID
        except psycopg2.IntegrityError:
            return "Email duplicado" # E-mail já existe
        except psycopg2.Error as e:
            print(f"Erro ao inserir registro: {e}")
            return False

# --- 2. CONFIGURAÇÃO E ROTAS DO FLASK ---

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Tenta inicializar o DAO
try:
    cadastro_dao = CadastroDAO()
except RuntimeError:
    cadastro_dao = None # Define como None se a conexão falhar

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        if not cadastro_dao:
            flash('Erro: Serviço de banco de dados indisponível.', 'danger')
            return redirect(url_for('cadastro'))

        nome = request.form.get('nome')
        email = request.form.get('email')

        if not nome or not email:
            flash('Erro: Nome e E-mail são obrigatórios.', 'danger')
            return redirect(url_for('cadastro'))

        resultado = cadastro_dao.inserir_registro(nome, email)

        if isinstance(resultado, int):
            flash(f'Cadastro de **{nome}** realizado com sucesso! ID: {resultado}', 'success')
        elif resultado == "Email duplicado":
            flash(f'Erro: O e-mail **{email}** já está cadastrado.', 'warning')
        else:
            flash('Erro desconhecido ao cadastrar.', 'danger')

        return redirect(url_for('cadastro'))

    # Método GET: Renderiza o HTML com o CSS/JS embutidos
    return render_template_string(HTML_TEMPLATE)

# --- 3. TEMPLATE HTML COMPLETO (HTML/CSS/JS) ---

# Usando uma variável string para servir como template
# O CSS e o JS estão dentro da tag <style> e <script> respectivamente.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastro Web Unificado</title>
    <style>
        /* CSS SIMPLES */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            flex-direction: column;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            width: 350px;
        }
        h2 {
            text-align: center;
            color: #333;
            margin-bottom: 25px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #555;
        }
        input[type="text"], input[type="email"] {
            width: 95%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box; /* Inclui padding e border na largura total */
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #28a745; /* Verde moderno */
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1e7e34;
        }
        /* Estilos de Alerta */
        .alert {
            padding: 12px;
            margin-bottom: 15px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 14px;
        }
        .alert-success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .alert-danger {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        .alert-warning {
            background-color: #fff3cd;
            color: #856404;
            border: 1px solid #ffeeba;
        }
    </style>
    <script>
        // JS para validação básica no frontend
        function validarFormulario() {
            var nome = document.getElementById('nome').value;
            var email = document.getElementById('email').value;

            if (nome.trim() === "" || email.trim() === "") {
                alert("Por favor, preencha todos os campos.");
                return false;
            }
            // Regex simples de email
            var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert("Por favor, insira um endereço de e-mail válido.");
                return false;
            }
            return true;
        }
    </script>
</head>
<body>
    <div class="container">
        <h2>📝 Cadastro de Usuário</h2>

        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              <div class="alert alert-{{ category }}">{{ message | safe }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        <form method="POST" onsubmit="return validarFormulario();">
            <div class="form-group">
                <label for="nome">Nome Completo:</label>
                <input type="text" id="nome" name="nome" required>
            </div>
            <div class="form-group">
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <button type="submit">Cadastrar e Salvar</button>
        </form>
    </div>
</body>
</html>
"""

# --- 4. EXECUÇÃO ---

from flask import render_template_string # Importado aqui para clareza na separação

if __name__ == '__main__':
    # Usar debug=True para desenvolvimento.
    app.run(debug=True)
