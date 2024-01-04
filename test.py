import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="dev",
    password="")
cur = conn.cursor()
print('yes')
cur.execute("SELECT * FROM clothing;")
print(cur.fetchall())
