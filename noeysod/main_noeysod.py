#! พัง

'''run by put 'fastapi dev main_noeysod.py' in terminal'''

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory='page')

@app.get('/', response_class=HTMLResponse)
async def admin_subject(request: Request):
    return template.TemplateResponse(
        name="admin_subject.html",
        context={"request": request}
    )

if __name__ == "__main_noeysod__":
    uvicorn.run("main:app")
