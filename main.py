from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.templating import Jinja2Templates
from generate_model import generate_plan

app = FastAPI()

# Подключение статических файлов (например, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализация шаблонов Jinja2
templates = Jinja2Templates(directory="templates")

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Обработка данных из формы
@app.post("/")
async def form_handler(request: Request, input_text: str = Form(...)):
    generated_text = generate_plan(input_text)

    # Вместо возвращения JSON используем редирект на главную страницу
    return templates.TemplateResponse("index.html", {"request": request, "input_text": generated_text})