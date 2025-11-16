# app.py

import os
from flask import Flask, jsonify, request, send_from_directory
from Cliente import Cliente
from ClienteDAO import ClienteDAO

app = Flask(__name__, static_folder='../frontend', static_url_path='')
cliente_dao = ClienteDAO()

# Define a pasta onde estão os arquivos HTML, CSS e JS
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# --- Rota para servir o Frontend ---
@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

# --- Rotas da API REST ---

@app.route('/api/clientes', methods=['POST'])
def cadastrar_cliente():
    """Rota para cadastrar um novo cliente."""
    try:
        data = request.json
        nome = data['nome']
        email = data['email']
        
        novo_cliente = Cliente(nome=nome, email=email)
        cliente_salvo = cliente_dao.inserir(novo_cliente)

        if cliente_salvo:
            return jsonify(cliente_salvo.to_dict()), 201
        else:
            return jsonify({"erro": "Erro ao salvar cliente ou email já existe."}), 400
            
    except Exception as e:
        return jsonify({"erro": f"Dados inválidos: {e}"}), 400

@app.route('/api/clientes', methods=['GET'])
def listar_clientes():
    """Rota para listar todos os clientes."""
    clientes = cliente_dao.buscar_todos()
    return jsonify(clientes)

if __name__ == '__main__':
    # Para rodar o servidor, use: python app.py
    # O servidor estará disponível em http://localhost:5000/
    app.run(debug=True)