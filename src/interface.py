"""Creates a command-line interface where users can interact with the database."""

import sqlite3


def welcome_message():
    """Displays welcome message."""
    print("+-----------------------------------------+")
    print("|    Welcome to the AfricaDB Interface    |")
    print("+-----------------------------------------+")
    display_tables_info()


def display_tables_info():
    """Displays the info about each table."""
    print()
    print("This interface allows users to interact with the following tables:")
    print(" - HPI: Happy Planet Index information about countries from around the world.")
    print(" - DevIndicators: GDP growth and GDP per capita information for countries from around the world.")
    print(" - RealGDPGrowth: Real GDP Growth data for a number of years.")
    print(" - Resources: Resource Rent data for countries.")
    print()


def get_table_name():
    """Gets the name of a table."""
    table_list = ["HPI", "DevIndicators", "RealGDPGrowth", "Resources"] # list of tables in DB

    table_name = input()

    while(table_name not in table_list): # see if entered table name is in DB
        print("** The entered table does not exist in the database. Please re-enter the name:")
        table_name = input()
    print()
    return table_name


def get_table_data():
    """Gets table contents."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    print("* Please enter a valid table name to display it's contents:")
    table_name = get_table_name()

    get_data_command = "SELECT * FROM {A}".format(A = table_name) # query that gets the results from the given table

    result = conn.execute(get_data_command) # executes the querys
    data = result.fetchall()

    for i in data:
        print(i) # prints query results

    conn.close() # close DB connection


def user_query():
    """User chosen query from a table."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    print("* Which table would you like to query?:")
    table_name = get_table_name()
    print("* For what condition would you like to query for? (Ex: Rank = 1):")
    condition = input()

    query_command = "SELECT * FROM {A} WHERE {B}".format(A = table_name, B = condition)

    result = conn.execute(query_command) # executes the query
    data = result.fetchall()

    for i in data:
        print(i) # prints query results

    conn.close() # closes DB connection


def edit_data():
    """Perform update/edit on table."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    print("* Which table would you like to edit?:")
    table_name = get_table_name()

    print("* Choose what attribute to udpdate: ")
    attribute = input()
    print("* Choose a value for this attribute: ")
    value = input()
    print("* For what condition will this be updated? (Ex: Rank = 1): ")
    condition = input()

    update_command = "UPDATE {A} SET {B} = {C} WHERE {D}".format(A = table_name, B = attribute, C = value, D = condition)
    conn.execute(update_command) # execute the update command
    conn.commit() # commit the changess
    conn.close()

    print("Updating...")
    print()


def display_schema():
    """Displays database schema."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    schema = "select sql from sqlite_master where type='table'" # get the schema using this command
    result = conn.execute(schema)
    data = result.fetchall()

    print("Displaying schema...")
    print()

    for i in data: # print schema results
        print(i)
        print()

    conn.close()


def insert_data():
    """Inserts data into table."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    print("* Enter 1 to view database table schema to see what values to enter. Press 2 to skip this option.:")
    view_schema = int(input())
    if view_schema == 1:
        print()
        display_schema()
        print()
    elif view_schema == 2:
        pass
    else:
        print("** Incorrect option entered.")
        print("* Enter 1 to view database table schema to see what values to enter. Press 2 to skip this option.:")
        view_schema = int(input())

    print("* Which table would you like to insert into?:")
    table_name = get_table_name()

    print("* Enter what (comma-seperated) attributes to insert: ")
    attribute = input()
    print("* Enter (comma-seperated) values for attributes: ")
    value = input()

    try:
        insert_command = "INSERT INTO {A}({B}) VALUES ({C})".format(A = table_name, B = attribute, C = value)
        conn.execute(insert_command)
        conn.commit()
        conn.close()
        print()
        print("Inserting data...")
        print()
    except:
        print("Incorrect format. Exiting this option...")
        print()


def display_questions():
    print("Project questions:")
    print(" 1) Africa's Real GDP Growth rate seemed to steadily increase for a few decades, but then it took a downturn. When did this downturn occur and why?")
    print(" 2) Is there a correlation between GDP growth/GDP per capita and inequality rankings (income inequality)?")
    print(" 3) Is there a correlation between living standards and GDP per capita?")
    print(" 4) Are countries that live in a specific region overall happier than countries that don't live in that region? (i.e. Sub-Saharan Africa and MENA)")
    print(" 5) Do countries with a higher natural resources rent (as a % of GDP) have a higher GDP per capita or vice versa? Do the findings from this question make steps to validate the idea of the resource curse?")
    print()


def question_queries():
    """Perform the queries used for research project."""
    conn = sqlite3.connect("africaDB.sqlite3") # connect to the database

    print("* Type 1 to display the project research questions. Type 2 to skip this.")
    question_dec = int(input())
    if question_dec == 1:
        display_questions()
    else:
        pass

    print("* Type Question Number to display queries & results.")
    question_num = int(input())

    if question_num == 1:
        query_command = "SELECT \"2008\", \"2009\",\"2010\",\"2011\",\"2012\" from RealGDPGrowth"
        print("Using this query: ", query_command)
        result = conn.execute(query_command)
        data = result.fetchall()
        print()
        print("Displaying results:")
        for i in data:
            print(i)

    elif question_num == 2:
        query_command = "NOPE"
        print("Using this query: ", query_command)
        result = conn.execute(query_command)
        data = result.fetchall()

        for i in data:
            print(i)

    elif question_num == 3:
        query_command = "NOPE"
        print("Using this query: ", query_command)
        result = conn.execute(query_command)
        data = result.fetchall()

        for i in data:
            print(i)

    elif question_num == 4:
        query_command = "select * from HPI where region = \"Sub Saharan Africa\" OR \"Middle East and North Africa\""
        print("Using this query: ", query_command)
        result = conn.execute(query_command)
        data = result.fetchall()

        for i in data:
            print(i)

    elif question_num == 5:
        query_command = "NOPE"
        print("Using this query: ", query_command)
        result = conn.execute(query_command)
        data = result.fetchall()

        for i in data:
            print(i)

    else:
        print("Incorrect response; cancelling this action!")


def main():
    """Manages the running of the interface."""
    print()
    print("Please select an option from below:")
    print(" - 1: Display data from a selected table.")
    print(" - 2: Display schema.")
    print(" - 3: Perform a specific query based on user-chosen conditions.")
    print(" - 4: Display query and query results for a project research question.")
    print(" - 5: Add content to a table.")
    print(" - 6: Update/edit a table.")
    print(" - 7: Display the table names and descriptions.")

    print("* Enter your chosen option's number:")
    option = int(input())
    print()

    if option == 1:
        get_table_data()
    elif option == 2:
        display_schema()
    elif option == 3:
        user_query()
    elif option == 4:
        question_queries()
    elif option == 5:
        insert_data()
    elif option == 6:
        edit_data()
    elif option == 7:
        display_tables_info()
    else:
        print("** Incorrect option.")
        main()

    print()
    print("Would you like to exit the program? Enter 1 to Exit or 2 to Continue:")
    exit_decision = int(input())
    print()

    if exit_decision == 1:
        print("Exiting...")
        print()
        pass
    elif exit_decision == 2:
        main()
    else:
        print("Incorrect response.")
        print("Would you like to exit the program? Enter 1 to Exit or 2 to Continue:")
        exit_decision = input()

welcome_message() # display interface welcome message
main() # call main to run the program
