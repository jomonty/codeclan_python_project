DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS news;

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    class_date DATE,
    class_time TIME,
    capacity INT,
    is_active BOOLEAN,
    is_peak BOOLEAN
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    is_premium BOOLEAN,
    is_active BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
    member_id INT NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    news_item TEXT,
    create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);