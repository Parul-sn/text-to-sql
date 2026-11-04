from src.db import get_schema, execute_sql
from src.llm import generate_sql


def run(question: str) -> dict:
    schema = get_schema()
    sql = generate_sql(question, schema)
    try:
        cols, rows = execute_sql(sql)
        return {"question": question, "sql": sql, "columns": cols, "rows": rows, "error": None}
    except Exception as e:
        return {"question": question, "sql": sql, "columns": [], "rows": [], "error": str(e)}