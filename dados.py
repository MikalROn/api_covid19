import pandas as pd
import os


class DataCovid:
    """ Classe que busca e filtra os dados """

    def __init__(self):
        self._dados = pd.read_csv('dados/df_covid19_countries.csv')
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
