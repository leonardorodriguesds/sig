import sqlite3

conn = sqlite3.connect('data.db')

cursor = conn.cursor()  #cursor = interador que permite navegar e manipular os registros do bd

cursor.execute("""
CREATE TABLE IF NOT EXISTS person (
    id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    second_name TEXT NOT NULL,
    register TEXT NOT NULL PRIMARY KEY,
    genre VARCHAR(1) NOT NULL,
    date_birth DATE NOT NULL,
    age INTEGER NOT NULL,
    number INTEGER DEFAULT 0,
    date_insurance DATE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS record (
    id INTEGER NOT NULL PRIMARY KEY,
    pacient_id INTEGER NOT NULL,
    auditor TEXT NOT NULL,
    auditor_position TEXT NOT NULL,
    weight FLOAT NOT NULL,
    height FLOAT NOT NULL,
    imc FLOAT NOT NULL,
    nutritional_state TEXT NOT NULL,
    hypertension_state TEXT NOT NULL,
    hemoglobin FLOAT NOT NULL,
    albumin FLOAT NOT NULL,
    phosphor FLOAT NOT NULL,
    FOREIGN KEY(pacient_id) REFERENCES person(id)
);
""")

conn.close()
