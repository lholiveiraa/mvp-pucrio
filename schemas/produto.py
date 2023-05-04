from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto

# from schemas import ComentarioSchema


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str
    estoque: Optional[int]
    preco_venda: float 
    preco_custo: float


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str 

class ListagemProdutosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for produto in produtos:
        result.append({
            "nome": produto.nome,
            "estoque": produto.estoque,
            "preco_venda": produto.preco_venda,
            "preco_custo": produto.preco_custo
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int
    nome: str
    estoque: int
    preco_venda: float
    preco_custo: float


class ProdutoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_produto(produto: Produto):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": produto.id,
        "nome": produto.nome,
        "estoque": produto.estoque,
        "preco_venda": produto.preco_venda,
        "preco_custo": produto.preco_custo
    }
