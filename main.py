from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

app = FastAPI(title="Estoque")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def exibir_home(request: Request, db:Session = Depends(get_db)):
    lista_produtos = db.query(Produto).all()
    return templates.TemplateResponse(request, "index.html", {"request": request, "produtos": lista_produtos})

