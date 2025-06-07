import os
import asyncio
from dotenv import load_dotenv, find_dotenv

import google.generativeai as genai

_ = load_dotenv(find_dotenv())

from fastmcp import Client

caminho_servidor = 'http://localhost:8000/sse'
cliente = Client(caminho_servidor)

async def testar_servidor(cliente, busca):
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Erro: A variável de ambiente GEMINI_API_KEY não foi encontrada.")
        return

    genai.configure(api_key=api_key)

    async with cliente:
        print("Buscando na Wikipedia...")
        argumentos = {"busca": busca}
        resultado = await cliente.call_tool("buscar_wikipedia", arguments=argumentos)
        
        print("\n--- Resumo da Wikipedia ---")
        print(resultado)
        print("---------------------------\n")

        mensagem_sistema = f'''
        Você é um assistente prestativo. O usuário fez uma busca na Wikipedia pelo tema "{busca}".
        O resultado da busca foi:
        ---
        {resultado}
        ---
        Com base nesse conteúdo, formate uma resposta amigável e concisa para o usuário.
        '''
        
        print("Gerando resposta com o Gemini...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = await model.generate_content_async(mensagem_sistema)
        
        print("\n🤖 Resposta do Assistente:\n")
        print(response.text)


if __name__ == '__main__':
    asyncio.run(testar_servidor(
        cliente=cliente,
        busca='Inteligência Artificial'
    ))