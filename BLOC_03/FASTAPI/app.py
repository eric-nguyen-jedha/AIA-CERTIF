import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
import pandas as pd
from datetime import datetime
import random


description = """
Welcome to Jedha Real-time Payments API. This application is part of the Lead program project! Try it out 🕹️
## Endpoints

There is currently just a few endpoints:

* `/`: **GET** request that display a simple default message.
* `/current-transactions`: **GET** request that gives you 1 current transaction

The API is limited to **5 calls/ minutes** 🚧. If you try more, your endpoint will throw back an error.
"""

app = FastAPI(
    title="Jedha - Real-time Payments API 💵",
    description=description,
    version="0.1",
    contact={
        "name": "Jedha",
        "url": "https://jedha.co",
    },
)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/current-transactions")
@limiter.limit("5/minute")
async def current_transactions(request: Request):
    filename = "fraud_api.csv"
    df = pd.read_csv(filename, header=0, index_col=[0])
    
    # Tirer une ligne aléatoire
    df = df.sample()
    
    # Debug: Afficher les infos temporelles
    print(f"unix_time: {df['unix_time'].iloc[0]}")
    print(f"trans_date_trans_time: {df['trans_date_trans_time'].iloc[0]}")
    print(f"is_fraud (vérité terrain): {df['is_fraud'].iloc[0]}")
    
    # Convertir unix_time en current_time (millisecondes)
    df["current_time"] = (df["unix_time"] * 1000).astype(int)
    print(f"current_time généré: {df['current_time'].iloc[0]}")
    
    # Supprimer les colonnes temporelles originales
    df = df.drop(columns=["trans_date_trans_time", "unix_time"])
    
    return df.to_json(orient="split")

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)