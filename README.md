# Background

SQL sublanguage: DQL (Data Query Language)

When we query a database for information, the results are not necessarily ordered the way we'd like. This is
done with the ORDER BY clause.

SELECT * FROM table_name ORDER BY column1 [, column2, column3, etc...] [ASC|DESC]

When ordering by multiple columns, the priority is from left to right. By default, ORDER BY is ascending.

## Problem 1

Assume the following table character already exists.

| id | first_name | last_name |
|----|------------|-----------|
| 1 | Leto | Atreides |
| 2 | Vladimir | Harkonnen |
| 3 | Jessica | Atreides |
| 4 | Paul | Atreides |
| 5 | Feyd-Rautha | Harkonnen |

Write a statement in `problem1.sql` to query the database for all characters. Make sure the results are in
ascending order by last name, and first name as a tie-breaker.
