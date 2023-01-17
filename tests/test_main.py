from fastapi.testclient import TestClient
from api import app, engine
from requests import get
from dados import DataCovid

#######
data = DataCovid(engine)
client = TestClient(app)
class Test:

    """ Testes da api e da classe DataCovid"""

    # [ - Testes de conecção e disponibilidade - ]
    def test_index_status(self):
        assert client.get('/').status_code == 200

    def test_docs_status(self):
        assert client.get('/docs').status_code == 200

    def test_get_data_by_country_status_with_valid_county(self):
        assert client.get('/Brazil/covid').status_code == 200

    def test_get_data_by_country_status_with_invalid_county(self):
        entrada = client.get('/asd/covid')
        assert entrada.status_code == 404
        assert entrada.json() == {'error': 'asd not found'}

    def test_get_full_data_status(self):
        assert client.get('/dados').status_code == 200

    # [ - Testes diversos - ]

    def test_index_to_docs(self):
        r = get('http://127.0.0.1:8000/')
        assert r.url == 'http://127.0.0.1:8000/docs'

    def test_all_countries(self):
        r = get('http://127.0.0.1:8000/all_countries')
        assert r.json() == data.get_all_countries

    def test_dados_retorna_lista(self):
        assert type(data.get_all_countries) == list

    def test_dados_retorna_full_data_dict(self):
        entrada = data.get_full_data
        assert type(entrada) == dict





