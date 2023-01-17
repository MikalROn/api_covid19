from fastapi import HTTPException


class CountryNotFound(HTTPException):
    """ Verifica seo país existe na base de dados"""
    def __init__(self, country: str):
        self.message = f'{country} not found'
        self.status_code = 404
