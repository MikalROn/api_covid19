import pytest
import pandas as pd
from fastapi.testclient import TestClient
from api import app


client = TestClient(app)
class Test:

    def test_read_all_countries(self):
        entrada = client.get('/all_countries')

        assert entrada.status_code == 200

