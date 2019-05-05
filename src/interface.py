"""Creates a command-line interface where users can interact with the database."""

import sqlite3

def welcome_message():
    """Displays welcome message."""
    print("+-----------------------------------------+")
    print("|    Welcome to the AfricaDB Interface    |")
    print("+-----------------------------------------+")
    print()
    print("This interface allows users to interact with the following tables:")
    print(" - HPI: Happy Planet Index information about countries from around the world.")
    print(" - DevIndicators: GDP growth and GDP per capita information for countries from around the world.")
    print(" - RealGDPGrowth: Real GDP Growth data for a number of years.")
    print(" - Resources: Resource Rent data for countries.")
    print()

def get_table_name():
    """Gets the name of a table."""
    table_list = ["HPI", "DevIndicators", "RealGDPGrowth", "Resources"]

    table_name = input()

    while(table_name not in table_list):
        print("** The entered table does not exist in the database. Please re-enter the name:")
        table_name = input()
    return table_name


def get_table_data():
    """Gets table contents."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    print("* Please enter a valid table name to display it's contents:")
    table_name = get_table_name()

    get_data_command = "SELECT * FROM {A}".format(A = table_name)

    result = conn.execute(get_data_command)

    tables = result.fetchall()

    for i in tables:
        print(i)
    conn.close()


def main():
    """Manages the running of the interface."""
    welcome_message()
    get_table_data()

main()
