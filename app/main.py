# app/main.py

from fastapi import FastAPI
from app.service import calcular_recarga

app = FastAPI()

@app.post("/recarga")
def recarga(monto: int, premium: bool = False):

    return calcular_recarga(monto, premium)