def generate_sql(question: str, schema: str) -> str:
    """Stub — replace with real LLM later."""
    q = question.lower()
    if "customer" in q and "mumbai" in q:
        return "SELECT name FROM customers WHERE city = 'Mumbai';"
    return "SELECT * FROM customers LIMIT 5;"