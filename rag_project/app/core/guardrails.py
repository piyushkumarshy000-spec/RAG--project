from app.config import settings

def validate_query(query: str):
    if not query:
        raise ValueError("Query cannot be empty")
    
    if len(query) > settings.MAX_QUERY_LENGTH:
        raise ValueError("Query too long")
    
    blocked_words = ["hack", "attack"]
    if any(word in query.lower() for word in blocked_words):
        raise ValueError("Unsafe query detected")
    
    return query