import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "sample.db"


def get_schema(db_path: Path = DB_PATH) -> str:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = [r[0] for r in cur.fetchall()]

    parts = []
    for t in tables:
        cur.execute(f"PRAGMA table_info({t})")
        cols = [f"  {c[1]} {c[2]}" for c in cur.fetchall()]
        parts.append(f"CREATE TABLE {t} (\n" + ",\n".join(cols) + "\n);")
    con.close()
    return "\n\n".join(parts)


def execute_sql(sql: str, db_path: Path = DB_PATH):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description] if cur.description else []
    con.close()
    return cols, rows