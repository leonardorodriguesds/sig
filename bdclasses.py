import sqlite3
import openpyxl
from openpyxl import Workbook, load_workbook
from colorama import Fore, Back, Style, init

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
        self._result = self._cursor.fetchall()
        self.desconnect()

    def executemany(self, command, rows_list):
        self.connect()
        self._cursor = self._conn.cursor()
        self._cursor.executemany(command, rows_list)
        self._conn.commit()
        self.desconnect()

    def print_table(self, command, table_name):
        self.connect()
        self._cursor = self._conn.cursor()
        self._cursor.execute(command)

        if table_name.lower() == "person":
            aux = 'Tabela Pessoas'
            print("\n\n\n" + Fore.GREEN + Back.LIGHTBLACK_EX + "{0:^80}".format(aux) + Style.RESET_ALL + "\n\n")
            print(Fore.LIGHTRED_EX + '(id, first_name, second_name, register, genre, date_birth, age, number, date_insurance)' + Style.RESET_ALL)

        elif table_name.lower() == "record":
            aux = 'Tabela Ficha'
            print("\n\n\n" + Fore.GREEN + Back.LIGHTBLACK_EX + "{0:^80}".format(aux) + Style.RESET_ALL + "\n\n")
            print(Fore.LIGHTRED_EX + '(id, pacient_id, auditor, auditor_position, weight, height, imc, nutritional_state, hypertension_state, hemoglobin, albumin, phosphor)' + Style.RESET_ALL)

        for row in self._cursor.fetchall():
            print(Fore.GREEN + str(row) + Style.RESET_ALL)
        self.desconnect()

class Filter(SQLCommand):
    def __init__(self, table_person, table_record, type_filter, value):
        super(Filter, self).__init__()
        self.table_person = table_person
        self.table_record = table_record
        self.type_filter = type_filter
        self.value = value

        self.execute(self.table_person)
        self.aux_person = self._result
        self.execute(self.table_record)
        self.aux_record = self._result
        self.selected_row_person = []
        self.selected_row_record = []
        self.id = []

        if self.type_filter == "1" or self.type_filter.lower() == "sexo":
            self.filter_genre()
        
        elif self.type_filter == "2" or self.type_filter.lower() == "nome":
            self.filter_name()

        elif self.type_filter == "3" or self.type_filter.lower() == "imc":
            self.filter_imc()
            
    def filter_genre(self):
        self.selected_row_person.clear()
        self.selected_row_record.clear()
        self.id.clear()
        self.sexo_const = 4

        self.cell_search_person(self.sexo_const)

        self.print_result()

    def filter_name(self):
        self.selected_row_person.clear()
        self.selected_row_record.clear()
        self.id.clear()
        self.nome_const = 1

        self.cell_search_person(self.nome_const)

        self.print_result()

    def filter_imc(self):
        self.selected_row_person.clear()
        self.selected_row_record.clear()
        self.id.clear()
        self.imc_const = 6

        self.cell_search_record(self.imc_const)

        self.print_result()

    def cell_search_person(self, cell):
        for row in self.aux_person:
                if str(row[cell]).lower() == str(self.value).lower():
                    self.selected_row_person.append(row)
                    self.id.append(row[0])
            
        for row in self.aux_record:
            for patient_id in self.id:
                if patient_id == row[1]:
                    self.selected_row_record.append(row)

    def cell_search_record(self, cell):
        for row_record in self.aux_record:
            if str(row_record[6]) == self.value:
                self.selected_row_record.append(row_record)
                self.id.append(row_record[1])

        for row_person in self.aux_person:
            for id_person in self.id:
                if id_person == row_person[0]:
                    self.selected_row_person.append(row_person)

    def print_result(self):
        if self.selected_row_person:
            aux = "Resultados:"
            print("\n\n" + Fore.LIGHTYELLOW_EX + Back.LIGHTBLACK_EX +"{0:^80}".format(aux) + Style.RESET_ALL +"\n\n")
            for row_person in self.selected_row_person:
                print(Fore.LIGHTRED_EX + "Paciente: " + Style.RESET_ALL + "\n" + Fore.GREEN + "Nome: " + str(row_person[1]) + "; Sobrenome: " + str(row_person[2]) + "; RG: " 
                + str(row_person[3]) + "; Sexo: " + str(row_person[4]) + "; Data de nascimento: " + str(row_person[5]) 
                + "; Idade: " + str(row_person[6]) + "; Data de entrada no seguro: " + str(row_person[8]) + Style.RESET_ALL +"\n")

                for row_record in self.selected_row_record:
                    if row_record[1] ==  row_person[0]:
                        print(Fore.LIGHTRED_EX + "Exames: " + Style.RESET_ALL + "\n" + Fore.GREEN + "Auditor: " + str(row_record[2]) + "; Cargo do Auditor: " + str(row_record[3]) 
                        + "; Peso (KG): " + str(row_record[4]) + "; Altura (M): " + str(row_record[5]) + "; IMC: " 
                        + str(row_record[6]) + "; Estado nutricional: " + str(row_record[7]) + "; Estado de Hipertensão: " 
                        + str(row_record[8]) + "; Hemoglobina: " + str(row_record[9]) + "; Albúmina sérica: " 
                        + str(row_record[9]) + "; Fósforo: " + str(row_record[10]) + Style.RESET_ALL + "\n")
                        break
        else:
            print("\nNão houve resultados para sua pesquisa.\n")




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

class FillPersonTable:
    def __init__(self):
        self.command = """
        INSERT INTO person (id, first_name, second_name, register, genre, date_birth, age, number, date_insurance) 
        VALUES (?,?,?,?,?,?,?,?,?)
        """
    def getCommand(self):
        return self.command

class FillRecordTable:
    def __init__(self):
        self.command = """
        INSERT INTO record (id, pacient_id, auditor, auditor_position, weight, height, imc, nutritional_state, hypertension_state, hemoglobin, albumin, phosphor) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """
    def getCommand(self):
        return self.command

class GetTablePerson:
    def __init__(self):
        self.command = """
        SELECT * from person;
        """
    def getCommand(self):
        return self.command

class GetTableRecord:
    def __init__(self):
        self.command = """
        SELECT * from record;
        """
    def getCommand(self):
        return self.command