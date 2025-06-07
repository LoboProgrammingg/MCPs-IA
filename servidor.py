from fastmcp import FastMCP

servidor_mcp = FastMCP("mcp-teste")

@servidor_mcp.tool()
def dar_bom_dia(nome_usuario, id_usuario):
    return f'Ola, {nome_usuario}! (ID {id_usuario})'