import os
import asyncio
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai
from fastmcp import Client

_ = load_dotenv(find_dotenv())

caminho_servidor = 'http://localhost:8000/sse'
cliente = Client(caminho_servidor)

async def testar_servidor(cliente_mcp, local_busca):
    """Conecta ao servidor, chama as ferramentas e gera uma resposta com o Gemini."""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Erro: A variável de ambiente GEMINI_API_KEY não foi encontrada.")
        return

    genai.configure(api_key=api_key)

    print(f"Cliente: Conectando ao servidor para buscar dados de '{local_busca}'...")
    async with cliente_mcp:
        argumentos = {"local": local_busca}
        
        tempo_atual = await cliente_mcp.call_tool("buscar_tempo_atual", arguments=argumentos)
        previsao_tempo = await cliente_mcp.call_tool("buscar_previsao_tempo", arguments=argumentos)

        print("Cliente: Dados recebidos. Montando prompt para o Gemini...")
        mensagem_sistema = f'''
        Você é um assistente de meteorologia amigável e prestativo.
        Sintetize as informações a seguir em uma resposta clara e agradável para o usuário.

        - Local da busca: {local_busca}
        - Dados do tempo atual: {tempo_atual}
        - Dados da previsão para os próximos dias: {previsao_tempo}

        Com base nesses dados, formate uma resposta completa, informando a temperatura atual, a sensação térmica, a condição do céu (ex: "céu claro", "nublado") e a previsão para as próximas horas ou dias de forma resumida.
        '''
        
        print("Cliente: Gerando resposta com o Gemini...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = await model.generate_content_async(mensagem_sistema)
        
        print("\n🤖 Resposta do Assistente de Meteorologia:\n")
        print(response.text)

if __name__ == '__main__':
    local_cidade = 'Rio Verde, Brasil'
    try:
        asyncio.run(testar_servidor(
            cliente_mcp=cliente,
            local_busca=local_cidade
        ))
    except Exception as e:
        print(f"\nOcorreu um erro ao executar o cliente: {e}")
        print("Verifique se o servidor está rodando em outro terminal.")