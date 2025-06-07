import os
import dotenv
from fastmcp import FastMCP
import requests

dotenv.load_dotenv()

servidor_mcp = FastMCP('mcp-tempo')

@servidor_mcp.tool()
def buscar_tempo_atual(local: str) -> dict:
    """Busca o tempo atual para um determinado local na API do OpenWeatherMap."""
    app_id = os.environ["CHAVE_API_OPENWEATHER"]
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": local,
        "appid": app_id,
        "units": "metric",
        "lang": "pt_br"
    }
    
    print(f"Servidor: buscando tempo atual para '{local}'...")
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()

@servidor_mcp.tool()
def buscar_previsao_tempo(local: str) -> dict:
    """Busca a previsão do tempo para os próximos dias para um local."""
    app_id = os.environ["CHAVE_API_OPENWEATHER"]
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        "q": local,
        "appid": app_id,
        "units": "metric",
        "lang": "pt_br"
    }
    
    print(f"Servidor: buscando previsão do tempo para '{local}'...")
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print("Iniciando o servidor de previsão do tempo...")
    servidor_mcp.run(transport='stdio')