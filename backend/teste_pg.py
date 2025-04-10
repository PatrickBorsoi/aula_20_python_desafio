import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="root",
    port=5432
)
print("Conectado com sucesso!")
conn.close()
