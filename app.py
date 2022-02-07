from fastapi import FastAPI

app = FastAPI()


@app.get('/quote-query')
def quote(url: str, username: str, email: str):
    return {
        "tweet": url,
        "username": username,
        "email": email
    }
    
@app.post("/quote")
def create_post():
    

# uvicorn app:app --reload
