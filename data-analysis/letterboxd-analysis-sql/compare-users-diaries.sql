-- SQL script for Python + psycopg2
-- This script compares two diary datasets and shows the common films
-- Placeholders: {table_1} and {table_2} (table names)


SELECT
    table_1.release_year AS "release year",
    table_1.film_title AS "title",
    table_1.watch_date AS "watched by 1",
    table_2.watch_date AS "watched by 2",
    table_1.rating AS "rating 1",
    table_2.rating AS "rating 2"
FROM
    {table_1} AS table_1
INNER JOIN
    {table_2} AS table_2
ON
    table_1.film_title = table_2.film_title
AND
    table_1.release_year = table_2.release_year
ORDER BY
    table_1.release_year,
    table_1.watch_date,
    table_2.watch_date;