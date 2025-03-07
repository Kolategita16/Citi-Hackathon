from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Citi Hackathon API!"}

@app.get("/predict")
def predict(value: int):
    return {"prediction": value * 2}  # Replace with your ML model
