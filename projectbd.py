import sqlite3

class SQLCommand:
    def __init__(self):
        self.bd_name = 'data.db'
    def connect(self):
        self._conn = sqlite3.connect(self.bd_name)
    def desconnect(self):
        self._conn.close()
    def execute(self, command):
        self.connect()
        self._cursor = self._conn.cursor()
        self._cursor.execute(command)
        self.desconnect()

class CreateTablePerson:
    def __init__(self):
        self.command = """
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
        """
    def getCommand(self):
        return self.command

class CreateTableRecord:
    def __init__(self):
        self.command = """
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
        """
    def getCommand(self):
        return self.command

if __name__ == "__main__":
    TabelaPessoa = CreateTablePerson()
    TabelaFicha = CreateTableRecord()
    Executar = SQLCommand()

    Executar.execute(TabelaPessoa.getCommand())
    Executar.execute(TabelaFicha.getCommand())
