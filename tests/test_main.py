import pytest
import pandas as pd
from fastapi.testclient import TestClient
from api import app
from api import inicio

client = TestClient(app)

class Test:
    def test_read_root(self):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json() == inicio

    def test_get_all_countries(self):
        entrada = pd.read_json('http://127.0.0.1:8000/all_countries')[0].tolist()

        esperado = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
                    'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia',
                    'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
                    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
                    'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
                    'Bonaire Sint Eustatius and Saba', 'Bosnia and Herzegovina',
                    'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei',
                    'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon',
                    'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic',
                    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands',
                    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia',
                    'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica',
                    'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'England',
                    'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe Islands',
                    'Falkland Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia',
                    'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam',
                    'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
                    'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
                    'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea', 'North Macedonia',
                    'Northern Cyprus', 'Northern Ireland', 'Northern Mariana Islands',
                    'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palau', 'Palestine',
                    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
                    'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania',
                    'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
                    'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa',
                    'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal',
                    'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)',
                    'Slovakia', 'Slovenia', 'Solomon Islands',
                    'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain',
                    'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
                    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tokelau',
                    'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                    'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                    'United Kingdom', 'United States', 'United States Virgin Islands',
                    'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam',
                    'Wales', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
        assert client.get('/all_contries').status_code == 200
        assert esperado == entrada
