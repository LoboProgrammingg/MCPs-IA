from fastmcp import FastMCP

servidor_mcp = FastMCP("mcp-teste")

@servidor_mcp.tool()
async def dar_bom_dia(nome_usuario: str, id_usuario: int) -> str:
    return f'Ola, {nome_usuario}! (ID {id_usuario})'


if __name__ == "__main__":
    servidor_mcp.run(transport='sse')