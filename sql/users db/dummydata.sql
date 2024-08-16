INSERT INTO users (
    username, email, password_hash, created_at, last_login, is_active, role
) VALUES (
    'admin', 'maxcomperatore@gmail.com', '$2b$12$3', '2025-01-01 00:00:00', '2025-01-01 00:00:00', TRUE, 'admin');

INSERT INTO users (
    username, email, password_hash, created_at, last_login, is_active, role
) VALUES (
    'user', 'test@gmail.com', '$2b$12$3', '2025-01-01 00:00:00', '2025-01-01 00:00:00', TRUE, 'user');