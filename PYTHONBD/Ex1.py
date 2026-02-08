import psycopg2
from psycopg2 import extras  # Módulo para otimização de inserção em massa

# Dados estruturados em uma lista de tuplas
carros = [
    (1, 'Celta', 35000.00),
    (2, 'Fusca', 30000.00),
    (3, 'Fiat Uno', 32000.00)
]

def otimizar_banco():
    con = None
    try:
        # 1. Conexão utilizando gerenciador de contexto (opcional, mas seguro)
        con = psycopg2.connect(
            database='TESTE_ESTACIO', 
            user='postgres', 
            password='123',
            host='localhost'
        )
        
        with con.cursor() as cursor:
            # 2. Criação da tabela otimizada
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cars (
                    id INTEGER PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    preco NUMERIC(10, 2) NOT NULL
                )
            """)

            # 3. OTIMIZAÇÃO: Usando execute_values para inserção em lote único
            # Note que a query termina no 'VALUES' e o %s não tem parênteses ao redor
            query_insert = "INSERT INTO cars (id, nome, preco) VALUES %s ON CONFLICT (id) DO NOTHING"
            
            extras.execute_values(cursor, query_insert, carros)
            
            con.commit()
            print(f"Inserção otimizada concluída: {len(carros)} registros processados.")

            # 4. SELECT rápido
            cursor.execute("SELECT * FROM cars ORDER BY id")
            for row in cursor.fetchall():
                print(f"ID: {row[0]} | Carro: {row[1]:<10} | Preço: R$ {row[2]:>8.2f}")

    except Exception as e:
        print(f"Erro na operação: {e}")
        if con:
            con.rollback()
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    otimizar_banco()