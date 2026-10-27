import os
import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/whoami")
def whoami():
    return {"host": socket.gethostname(), "account": os.getenv("ACCOUNT_NAME", "unknown")}


@app.get("/health")
def health():
    return {"status": "ok"}
