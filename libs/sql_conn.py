import yaml
import psycopg2
import pandas as pd




with open('connection.yaml', 'r') as file:
    infos = yaml.safe_load(file)

conn = psycopg2.connect(user=infos['user'],
                        password=infos['password'],
                        host=infos['host'],
                        database=infos['database'])




insert_query = """
        INSERT INTO animals (age_upon_outcome, animal_id, animal_type, breed, color, date_of_birth, datetime_, monthyear, name, outcome_subtype, outcome_type, sex_upon_outcome)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """


def read_animals(query):
    df = pd.read_sql(query, conn)
    return df



def insert_animal_one(values):
    """Fonsiyon input olarak liste formatinda dogru sirada 12 deger alir"""
    conn = psycopg2.connect(user= infos['user'],
                            password= infos['password'],
                            host= infos['host'],
                            database= infos['database'])

    cursor = conn.cursor()

    cursor.execute(insert_query, tuple(values))

    conn.commit()

    cursor.close()
    print('Kaydetme islemi basarili.')
    print('1 kayit yapildi.')