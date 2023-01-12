from fastapi import FastAPI
from dados import DataCovid

app = FastAPI()


@app.get('/')
def read_all_countries():
    return {'Comandos': {
        'all_contries': 'retorna todos os paises presentes no data frame',
        '/nome_país/covid': 'retorna dados filtrados por país',
        'dados': 'retorna todos os dados'
                         }}


@app.get('/all_countries')
def read_all_countries():
    dados = DataCovid()
    return dados.get_all_countries


@app.get('/{country}/covid')
def read_data_of_contry(country):
    dados = DataCovid()
    return dados.get_covid_data_by_country(country)

@app.get('/dados')
def read_data_of_contry():
    dados = DataCovid()
    return dados.get_full_data
