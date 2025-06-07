import os
import dotenv

import requests


def buscar_tempo_atual(local: str) -> dict:
    dotenv.load_dotenv()
    app_id = os.environ["CHAVE_API_OPENWEATHER"]
    url = f'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": local,
        "appid": app_id,
        "units": "metric",
        "lang": "pt_br"
    }
    
    response = requests.get(url=url, params=params)
    return response.json()

def buscar_previsao_tempo(local: str) -> dict:
    dotenv.load_dotenv()
    app_id = os.environ["CHAVE_API_OPENWEATHER"]
    url = f'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        "q": local,
        "appid": app_id,
        "units": "metric",
        "lang": "pt_br"
    }
    
    response = requests.get(url=url, params=params)
    return response.json()

if __name__ == "__main__":
    local = "Cuiaba"
    tempo_atual = buscar_tempo_atual(local=local)
    print(tempo_atual)
    previsao_tempo = buscar_previsao_tempo(local=local)
    print(previsao_tempo)