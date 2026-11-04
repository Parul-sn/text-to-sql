import sqlite3
from pathlib import Path

DB = Path(__file__).parent.parent / "data" / "sample.db"
DB.parent.mkdir(exist_ok=True)

con = sqlite3.connect(DB)
cur = con.cursor()

cur.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    signup_date TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    amount REAL,
    order_date TEXT
);

INSERT INTO customers VALUES
 (1,'Alice','Mumbai','2024-01-05'),
 (2,'Bob','Delhi','2024-02-10'),
 (3,'Cara','Mumbai','2024-03-15');

INSERT INTO orders VALUES
 (1,1,250.0,'2024-04-01'),
 (2,1,120.5,'2024-04-15'),
 (3,2,500.0,'2024-05-01'),
 (4,3,75.0,'2024-05-20');
""")

con.commit()
con.close()
print(f"Seeded {DB}")