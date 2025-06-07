import asyncio
from pathlib import Path

from fastmcp import Client

caminho_servidor = Path(__file__).parent / 'servidor.py'
cliente = Client(caminho_servidor)

async def testar_servidor(cliente, nome_usuario, id_usuario):
    async with cliente:
        argumentos = {"nome_usuario": nome_usuario, "id_usuario": id_usuario}
        resultado = await cliente.call_tool("dar_bom_dia", arguments=argumentos)
        print(f'Resultado obtido do servidor MPC: {resultado}')
        

if __name__ == '__main__':
    asyncio.run(testar_servidor
                (cliente=cliente,
                nome_usuario='matheus',
                id_usuario=5)
            )