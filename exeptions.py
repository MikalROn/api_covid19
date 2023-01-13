from fastapi import HTTPException


class CountryNotFound(HTTPException):
    def __init__(self, country: str):
        self.message = f'{country} not found'
        self.status_code = 404
