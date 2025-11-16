// frontend/script.js

const API_URL = 'http://localhost:5000/api/clientes';

// --- Função de Cadastro ---
document.getElementById('cadastroForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;

    cadastrarCliente(nome, email);
});

async function cadastrarCliente(nome, email) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nome, email })
        });

        const data = await response.json();

        if (response.ok) {
            alert(`Cliente ${data.nome} cadastrado com sucesso! ID: ${data.id}`);
            document.getElementById('cadastroForm').reset(); // Limpa o formulário
            carregarClientes(); // Recarrega a lista
        } else {
            alert(`Erro ao cadastrar: ${data.erro}`);
        }
    } catch (error) {
        console.error('Erro na comunicação com a API:', error);
        alert('Erro de conexão com o servidor.');
    }
}

// --- Função de Listagem ---
async function carregarClientes() {
    const tableBody = document.querySelector('#clientesTable tbody');
    tableBody.innerHTML = '<tr><td colspan="3">Carregando...</td></tr>';

    try {
        const response = await fetch(API_URL);
        
        if (!response.ok) {
            throw new Error(`Erro HTTP: ${response.status}`);
        }

        const clientes = await response.json();
        
        tableBody.innerHTML = ''; // Limpa a tabela
        
        if (clientes.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="3">Nenhum cliente cadastrado.</td></tr>';
            return;
        }

        clientes.forEach(cliente => {
            const row = tableBody.insertRow();
            row.insertCell().textContent = cliente.id;
            row.insertCell().textContent = cliente.nome;
            row.insertCell().textContent = cliente.email;
        });

    } catch (error) {
        console.error('Erro ao buscar clientes:', error);
        tableBody.innerHTML = '<tr><td colspan="3">Falha ao carregar dados. Verifique o console do servidor.</td></tr>';
    }
}

// Carregar a lista assim que a página for carregada
document.addEventListener('DOMContentLoaded', carregarClientes);