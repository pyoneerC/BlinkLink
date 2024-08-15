SELECT version();

SELECT EXISTS (
    SELECT FROM information_schema.tables
    WHERE table_name = 'urls'
) AS table_exists;

SELECT * from urls;

