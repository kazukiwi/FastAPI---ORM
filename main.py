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
    categorias_do_banco = db.query(Categoria).all()
    return templates.TemplateResponse(request, "index.html", {"request": request, "produtos": lista_produtos, "categorias": categorias_do_banco})

@app.get("/produtos/cadastro", response_class=HTMLResponse)
def exibir_produtos(request: Request, db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    produtos = db.query(Produto).all()
    return templates.TemplateResponse(request, "cadastro_produto.html", {"request": request, "categorias": categorias, "produtos": produtos})

@app.post("/produtos/salvar")
def criar_produto(
    nome: str = Form(...),
    marca: str = Form(...),
    categoria_id: int = Form(...),
    db: Session = Depends(get_db)
):
    novo_produto = Produto(nome=nome, marca=marca, categoria_id=categoria_id)
    db.add(novo_produto)
    db.commit()

    return RedirectResponse(url="/", status_code=303)

@app.post("/produtos/deletar/{id}")
def deletar_produtos(
    id:int,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).get(id)
    if produto:
        db.delete(produto)
        db.commit()

    return RedirectResponse(url="/", status_code=303)

@app.get("/categorias")
def exibir_categorias(request: Request, db: Session = Depends(get_db)):
    lista_categorias = db.query(Categoria).all()
    return templates.TemplateResponse(request, "categorias.html", {"request": request, "categorias": lista_categorias})

@app.post("/categorias/salvar")
def criar_categorias(
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(nome=nome, descricao=descricao)
    db.add(nova_categoria)
    db.commit()
    return RedirectResponse(url="/categorias", status_code=303)

@app.post("/categorias/deletar/{id}")
def excluir_categoria(
    id:int,
    db: Session = Depends(get_db)
):
    categoria = db.query(Categoria).get(id)
    if categoria:
        db.delete(categoria)
        db.commit()

    return RedirectResponse(url="/categorias", status_code=303)