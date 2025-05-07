-- SQL script for Python + psycopg2
-- This script imports new data into the specified table, replacing existing records.
-- Placeholders: {table} (table name), {src} (CSV path)


CREATE TABLE IF NOT EXISTS {table} (
    watch_date DATE,
    film_title TEXT,
    release_year INT,
    rating INT
);

-- Remove existing data
TRUNCATE {table};

-- Import data from CSV (requires absolute path)
COPY {table} FROM {src}
DELIMITER ',' 
CSV HEADER;
