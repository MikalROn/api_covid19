import pandas as pd
from sqlalchemy import create_engine

class DataCovid:
    """ Classe que busca e filtra os dados """

    def __init__(self):
        self._engine = create_engine(f'mysql+pymysql://root:191145@127.0.0.1/api_covid')
        self._dados = pd.read_sql('SELECT * FROM covid;', self._engine)
        self._all_countries = self._dados['location'].unique().tolist()

    @property
    def get_all_countries(self) -> list[str]:
        return self._all_countries

    @property
    def get_full_data(self) -> dict:
        return self._dados.to_dict()

    def get_covid_data_by_country(self, country: str) -> dict:
        filtro = self._dados['location'] == country
        return self._dados[filtro].to_dict()
