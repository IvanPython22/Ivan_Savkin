import requests
import sqlite3
from concurrent.futures import ThreadPoolExecutor
from threading import Semaphore

connection = sqlite3.connect('starships.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS starships(
        id INTEGER PRIMARY KEY,
        name TEXT,
        model TEXT,
        manufacturer TEXT
    )
""")

connection.commit()


def get_starships_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        starships_info = response.json()

        connection = sqlite3.connect('starships.db')
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO starships (id, name, model, manufacturer)
            VALUES (?, ?, ?, ?)
            
            """, (
            starships_info.get('id'),
            starships_info.get('name'),
            starships_info.get('model'),
            starships_info.get('manufacturer')

        ))

        connection.commit()
        connection.close()


def create_starship():
    starships = range(1, 11)

    semaphore = Semaphore(10)

    with ThreadPoolExecutor(max_workers=10) as file:
        for starship_id in starships:
            url = f'https://swapi.dev/api/starships/{starship_id}/'
            semaphore.acquire()
            file.submit(get_starships_info, url)
            semaphore.release()


create_starship()






