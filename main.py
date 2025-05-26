from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def assesor():
    return "Server running..."
@app.get('/assesor')
def assesor():
    return {
        "Recomendación": "OK"
    }