CREATE TABLE IF NOT EXISTS urls_backup (
id SERIAL PRIMARY KEY,
short_code VARCHAR(6) NOT NULL UNIQUE,
original_url TEXT NOT NULL UNIQUE,
created_at TIMESTAMP NOT NULL,
last_updated_at TIMESTAMP NOT NULL,
expiration_date TIMESTAMP NOT NULL,
access_count INT NOT NULL
);