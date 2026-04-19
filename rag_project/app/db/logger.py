import datetime

def log_query(query, response):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} | Q: {query} | A: {response}\n")