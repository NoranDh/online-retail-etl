import os

import psycopg
from dotenv import load_dotenv


load_dotenv()

host = os.getenv("DB_HOST")

port= os.getenv("DB_PORT")
dbname=os.getenv("DB_NAME")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")

with psycopg.connect(
    host=host,
    port=int(port),
    dbname=dbname,
    user=user,
    password=password,
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT VERSION();")
        print(cur.fetchone()[0])