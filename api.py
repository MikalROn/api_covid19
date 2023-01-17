from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from exeptions import CountryNotFound
from dados import DataCovid
from sqlalchemy import create_engine

app: FastAPI = FastAPI()

engine = create_engine('mysql+pymysql://root:191145@127.0.0.1/api_covid')

# Rotas

@app.get('/')
def read_root():
    return RedirectResponse('/docs')

@app.get('/docs')
def read_docs():
    return HTMLResponse(content=get_redoc_html(openapi_url='/docs', title='my_api'))

@app.get('/all_countries')
async def read_all_countries():
    dados = DataCovid(engine)
    return JSONResponse(content=dados.get_all_countries, status_code=200)


@app.get('/{country}/covid')
async def read_data_of_contry(country):
    dados = DataCovid(engine)
    if country in dados.get_all_countries:
        return JSONResponse(content=dados.get_covid_data_by_country(country), status_code=200)
    else:
        raise CountryNotFound(country)

@app.get('/dados')
async def read_data_of_contry():
    dados = DataCovid(engine)
    return JSONResponse(content=dados.get_full_data, status_code=200)

# Exeptions
@app.exception_handler(CountryNotFound)
async def handle_country_not_found(request, exc):
    return JSONResponse(content={"error": exc.message}, status_code=exc.status_code)