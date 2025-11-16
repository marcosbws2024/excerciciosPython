import psycopg2
import json
from flask import Flask, jsonify, request

# --- 1. Configuração do Flask ---
app = Flask(__name__)

# --- 2. Credenciais do PostgreSQL ---
DBNAME = "empresa"
USER = "postgres"
PASSWORD = "123456"
HOST = "localhost"
PORT = "5432"

# --- 3. Função de Conexão e Consulta ao BD ---
def get_db_data(table_name="clientes"):
    """Conecta ao PostgreSQL e busca dados, retornando colunas e linhas."""
    conn = None
    try:
        conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
        cur = conn.cursor()
        
        # Consulta SQL
        consulta = f"SELECT * FROM {table_name} LIMIT 50;"
        cur.execute(consulta)
        
        columns = [desc[0] for desc in cur.description]
        data_list = cur.fetchall()
        cur.close()

        # Converte as linhas em uma lista de dicionários para JSON
        result = [dict(zip(columns, row)) for row in data_list]
        return result
        
    except psycopg2.Error as error:
        print(f"Erro no Banco de Dados: {error}")
        return {"error": str(error)}
    finally:
        if conn:
            conn.close()

# --- 4. Rota de API (Retorna Dados em JSON) ---
@app.route('/api/clientes')
def api_clientes():
    """Endpoint que o JavaScript do frontend chamará."""
    data = get_db_data("clientes")
    return jsonify(data)

# --- 5. Rota Principal (Retorna o HTML, CSS e JavaScript) ---
@app.route('/')
def index():
    """
    Rota principal que renderiza a interface web.
    O HTML, CSS e JS estão em uma string multi-linha.
    """
    html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Dados PostgreSQL em Arquivo Único</title>
    <style>
        /* CSS INLINE AQUI */
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f9;
            color: #333;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            color: #007bff;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }}
        #data-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        #data-table th, #data-table td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }}
        #data-table th {{
            background-color: #007bff;
            color: white;
        }}
        #status {{
            font-weight: bold;
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Dados da Tabela Clientes (PostgreSQL)</h1>
        <p id="status">Carregando dados...</p>
        <table id="data-table">
            <thead></thead>
            <tbody></tbody>
        </table>
    </div>

    <script>
        // JAVASCRIPT AQUI
        async function loadData() {{
            const statusElement = document.getElementById('status');
            const tableHead = document.querySelector('#data-table thead');
            const tableBody = document.querySelector('#data-table tbody');

            try {{
                // Chama a API que o Flask expôs
                const response = await fetch('/api/clientes'); 
                const data = await response.json();

                if (data.error) {{
                    statusElement.textContent = `Erro do Servidor: ${{data.error}}`;
                    statusElement.style.color = 'red';
                    return;
                }}

                if (data.length === 0) {{
                    statusElement.textContent = "Nenhum dado encontrado.";
                    return;
                }}

                // Cria o cabeçalho da tabela
                const columns = Object.keys(data[0]);
                tableHead.innerHTML = `<tr>${{columns.map(col => `<th>${{col.toUpperCase()}}</th>`).join('')}}</tr>`;

                // Cria as linhas da tabela
                tableBody.innerHTML = data.map(row => {{
                    return `<tr>${{columns.map(col => `<td>${{row[col]}}</td>`).join('')}}</tr>`;
                }}).join('');

                statusElement.textContent = `Dados carregados com sucesso: ${{data.length}} registros.`;
                statusElement.style.color = 'green';

            }} catch (error) {{
                statusElement.textContent = `Erro ao buscar dados: ${{error}}`;
                statusElement.style.color = 'red';
            }}
        }}

        loadData();
    </script>
</body>
</html>
    """
    return html_content

# --- 6. Execução ---
if __name__ == '__main__':
    # Roda o servidor Flask. Acesse em http://127.0.0.1:5000/
    app.run(debug=True)