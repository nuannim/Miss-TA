from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("")
template = Jinja2Templates(directory='CJ')

@app.get('/', )
def index(req: Request):
    return template.TemplateResponse(
        name="admin_subject.html",
        context={"request": req}
    )

if __name__ == "__main__":
    uvicorn.run("main:app")
