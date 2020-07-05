import sqlite3

DB_NAME = "my_pk_project.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_table():
    """
    Creates a table ready to accept our data.

    write code that will execute the given sql statement
    on the database
    """

    create_table = """ CREATE TABLE authors(
        ID          INTEGER PRIMARY KEY     AUTOINCREMENT,
        author      TEXT                NOT NULL,
        title       TEXT                NOT NULL,
        pages       INTEGER             NOT NULL,
        due_date    CHAR(15)            NOT NULL
    )   
    """

    conn = get_db_connection()
    conn.execute(create_table)
    conn.close()

def populate_table():
    add_data_stmt = ''' INSERT INTO authors(author,title,pages,due_date) VALUES(?,?,?,?); '''

    conn = get_db_connection()
    contract_list = ('prasanth', 'A book by PK', '300', '2020')
    conn.executemany(add_data_stmt, contract_list)
    conn.commit()
    conn.close()