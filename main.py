import random
from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
app.current_system = ""

systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}


@app.get("/status")
def status():
    app.current_system = random.choice(list(systems.values()))
    return app.current_system


@app.get("/repair-bay", response_class=HTMLResponse)
def repair_bay():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
    <div class="anchor-point">{app.current_system}</div>
    </body>
    </html>
    """


@app.post("/teapot")
def teapot():
    raise HTTPException(status_code=418, detail="I'm a teapot")
