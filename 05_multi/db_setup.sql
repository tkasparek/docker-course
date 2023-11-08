-- as postgres user

CREATE DATABASE demodb;
CREATE USER demouser;
ALTER USER demouser WITH PASSWORD 'demopwd';
ALTER USER demouser WITH LOGIN;

ALTER DATABASE demodb OWNER TO demouser;

-- as demouser

CREATE TABLE IF NOT EXISTS data (
    id SERIAL,
    content TEXT,
    primary key (id)
) TABLESPACE pg_default;
