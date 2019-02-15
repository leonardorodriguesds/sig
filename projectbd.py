import bdclasses

if __name__ == "__main__":
    bdclasses.init()
    Executar = bdclasses.SQLCommand()
    table_person = bdclasses.GetTablePerson()
    table_record = bdclasses.GetTableRecord()
    Executar.print_table(table_person.getCommand(), "person")
    Executar.print_table(table_record.getCommand(), "record")

    print(bdclasses.Fore.LIGHTRED_EX +"\nEscolha um Filtro: " + bdclasses.Style.RESET_ALL + bdclasses.Fore.LIGHTYELLOW_EX 
    +"\n 1) Sexo\n 2) Nome \n 3) IMC\n" + bdclasses.Style.RESET_ALL)

    type_filter = str(input())

    print(bdclasses.Fore.LIGHTRED_EX + "\nDigite o valor (M ou F no caso do filtro ser Sexo):\n" + bdclasses.Style.RESET_ALL)

    value = str(input())
    
    filter = bdclasses.Filter(table_person.getCommand(), table_record.getCommand(), type_filter, value)


    


