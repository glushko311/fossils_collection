from main import app

@app.get("/")
def main():
    return "Hello world"