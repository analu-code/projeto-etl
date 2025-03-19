from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês no formato 'YYYY | Mês'")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_Dia: str = Field(..., description="Tipo do dia (útil, final de semana, etc.)")
    Objetivo: str = Field(..., description="Objetivo da campanha")
    Date: str = Field(..., description="Data no formato YYYY-MM-DD")
    AdSet_name: str = Field(..., description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(..., ge=0, le=1200.00, description="Valor gasto no anúncio (mínimo 0, máximo 600)")
    Link_clicks: Optional[int] = Field(None, description="Quantidade de cliques no link")
    Impressions: int = Field(..., description="Número de impressões")
    Conversions: Optional[int] = Field(None, description="Número de conversões")
    Segmentação: str = Field(..., description="Tipo de segmentação utilizada")
    Tipo_de_Anúncio: str = Field(..., description="Tipo do anúncio")
    Fase: str = Field(..., description="Fase do lançamento ou campanha")

