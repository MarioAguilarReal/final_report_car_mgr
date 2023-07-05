--Table definition
CREATE TABLE car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_car VARCHAR(128),
    color VARCHAR(128),
    license VARCHAR(128),
    owner_last_name VARCHAR(128),
    owner_first_name VARCHAR(128)
);

-- Dummy data (for testing purposes)

INSERT INTO car (
    type_car,
    color,
    license,
    owner_last_name,
    owner_first_name
) VALUES (
    "SUV",
    "Red",
    "HNG123",
    "Aguilar",
    "Mario"
),
(
    "Hatchback",
    "Blue",
    "3KDHDK",
    "Real",
    "Diego"
);


