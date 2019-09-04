# africa_db README
### Team Members: Christian Lussier, Robert Samuel, Jordan Wilson

## Project Overview:
Our project looks into a variety of questions surrounding African development and economics using database systems, such as why Africa's Real GDP growth rate suddenly declined after years of steady growth and if there is a correlation between region of residence and citizen happiness. Our research has provided a number of insights into these questions, finding for instance, that African citizens of countries in the MENA region seem to be much happier than those in Sub-Saharan Africa.

To do this, our team compiled a plethora of data and used Sqlite3 to organize it and store it. Additionally, the project features a text-based interface developed in Python that can interact with the database.

## Running the Project
To clone the project, open a terminal window, navigate to your preferred directory, and run the command:
```
git clone https://github.com/lussierc/africa_db.git
```

To run the project's text-based database interface, first ensure both Python3 and Sqlite3 are installed. Then navigate to the `src` directory and run the following commands (depending on what you want to run):
- To run the text-based interface run the command: `python3 interface.py`

- To open the database run the command: `sqlite3 africaDB.sqlite3`

- To run the database builder file, run the command: `cat africaDB-build.txt | sqlite3 africaDB.sqlite3`


## Contributors
Thanks to the following people who contributed to this project:
- Christian Lussier ([See GitHub Profile](https://github.com/lussierc))
- Robert Samuel ([See GitHub Profile](https://github.com/robert-samuel07))
- Jordan Wilson ([See GitHub Profile](https://github.com/wilsonj24))

## Problems or Praise?
If you find any issues with the project or have some new ideas, please leave an issue in the project's issue tracker. If you have praise, feel free to leave a comment somewhere in the repository.
