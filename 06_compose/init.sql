CREATE TABLE IF NOT EXISTS data (
    id SERIAL,
    content TEXT,
    primary key (id)
) TABLESPACE pg_default;
