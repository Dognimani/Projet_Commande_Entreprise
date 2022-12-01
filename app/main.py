from fastapi import FastAPI,Request,Form,Depends
import model
from config import engine
#prepa du front
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

#import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static") # specification of the folder of static files (css and js)
templates = Jinja2Templates(directory="templates") # specification of the folder of templates (html)

@app.get('/')
async def Home():
    return "Hello world"

# road for the list of molecule
@app.get("/List/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("List.html", {"request": request})

# road for the  molecule registration

@app.get("/band/", response_class=HTMLResponse)
async def band(request: Request):
    return templates.TemplateResponse("band.html", {"request": request})    

# road for the authentication

@app.get("/authentication/", response_class=HTMLResponse)
async def band(request: Request):
    return templates.TemplateResponse("authentication.html", {"request": request})        

# road for seeing details of a specific molecule

@app.get("/ViewMolecule/", response_class=HTMLResponse)
async def band(request: Request):
    return templates.TemplateResponse("ViewMolecule.html", {"request": request})      


#Create a molecule
    
#app.include_router(router.router,prefix="/result",tags=["result"])