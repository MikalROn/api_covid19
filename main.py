from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+pymysql://root:191145@127.0.0.1/sucos')


def criar_vendedores(matricula: str, nome: str, comissao: float) ->  None:
    with engine.connect() as conn:
        comando_sql = f"""
        INSERT INTO tbVendedores
        (Matricula, Nome, Comissao)
        VALUES
        ('{matricula}', '{nome}', '{comissao}')
        """
        conn.execute(comando_sql)

data = pd.read_sql('SELECT * FROM tbVendedores', engine)
new_data = data.groupby('Matricula').first()
data.to_sql('tbVendedores', engine, 'sucos', if_exists='replace')