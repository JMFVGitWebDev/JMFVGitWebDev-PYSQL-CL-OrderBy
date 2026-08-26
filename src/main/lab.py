import os
import sqlite3

from src.main.character import Character

"""
SQL sublanguage: DQL (Data Query Language)

When we query a database for information, that information is not necessarily ordered. When querying for
information we usually want to indicate the order for our results. This is done with the ORDER BY clause.

Example: SELECT * FROM table_name ORDER BY column1 [, column2, column3, etc...] [ASC|DESC]
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def problem1():
    """
    character table
    | id |  first_name  |  last_name  |
    -----------------------------------
    |1   |'Leto'        |'Atreides'   |
    |2   |'Vladimir'    |'Harkonnen'  |
    |3   |'Jessica'     |'Atreides'   |
    |4   |'Paul'        |'Atreides'   |
    |5   |'Feyd-Rautha' |'Harkonnen'  |

    Problem 1: Write a statement below to query the database for all characters. Make sure the results are in
    ascending order by last name, and first name as a tie-breaker.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE character(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT
    );
    """)
    cur.execute(
        "INSERT INTO character (first_name, last_name) VALUES "
        "('Leto', 'Atreides'),"
        "('Vladimir', 'Harkonnen'),"
        "('Jessica', 'Atreides'),"
        "('Paul', 'Atreides'),"
        "('Feyd-Rautha', 'Harkonnen');"
    )
    conn.commit()

    result_list = []
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            result_list.append(Character(row[0], row[1], row[2]))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return result_list
