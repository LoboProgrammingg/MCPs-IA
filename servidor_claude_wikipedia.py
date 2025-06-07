from fastmcp import FastMCP
import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError

servidor_mcp = FastMCP("mcp-busca-wikipedia")

wikipedia.set_lang("pt")

@servidor_mcp.tool()
async def buscar_wikipedia_local(busca: str) -> str:
    """
    Busca um resumo sobre o tema na Wikipedia em português,
    tratando possíveis erros.
    """
    print(f"Recebi uma busca por: '{busca}'")
    try:
        return wikipedia.summary(busca, auto_suggest=True, sentences=5)

    except PageError:
        print(f"Erro: PageError. Não encontrei nada para '{busca}'")
        return f"Desculpe, não encontrei nenhum artigo na Wikipedia para '{busca}'."

    except DisambiguationError as e:
        print(f"Erro: DisambiguationError. Opções: {e.options[:3]}")
        opcoes = ", ".join(e.options[:3])
        return f"A busca por '{busca}' é ambígua. Tente ser mais específico. Algumas opções são: {opcoes}."

if __name__ == "__main__":
    servidor_mcp.run(transport='stdio')