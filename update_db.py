import sqlite3
import os

db = 'docs.db'
conn = sqlite3.connect(db)

ArticlesDir = "./docs/"
schema = 'schema.sql'

def update_db(notes):
    connection = sqlite3.connect(db)
    with open(schema) as files:
        connection.executescript(files.read())
    cur = connection.cursor()
    for i in notes:
        cur.execute("INSERT INTO docs (content) VALUES (?)", (str(i),))
    connection.commit()
    connection.close()

def get_from_folder():
    articles = [ j for j in os.listdir(ArticlesDir) if j.endswith('.md')]
    return articles

notes = get_from_folder()
print(len(notes))
update_db(notes)
#for i in notes:
#    print(len(i),i)


