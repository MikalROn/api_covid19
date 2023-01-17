from api import engine
from dados import DataCovid

dados = DataCovid(engine)

print(dados.get_full_data)