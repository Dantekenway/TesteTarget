import json

def analisar_faturamento_diario(dados_faturamento):

    faturamento_diario = [dia["faturamento"] for dia in dados_faturamento["dias"]]
    
   
    dias_com_faturamento = [dia for dia in dados_faturamento["dias"] if dia["faturamento"] > 0]
    media_mensal = sum(dia["faturamento"] for dia in dias_com_faturamento) / len(dias_com_faturamento)
    
   
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    
    
    dias_acima_da_media = sum(dia["faturamento"] > media_mensal for dia in dados_faturamento["dias"])
    
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open("dados_faturamento.json", "r") as f:
    dados_faturamento = json.load(f)


menor_faturamento, maior_faturamento, dias_acima_da_media = analisar_faturamento_diario(dados_faturamento)


print("Menor faturamento diário:", menor_faturamento)
print("Maior faturamento diário:", maior_faturamento)
print("Dias com faturamento acima da média mensal:", dias_acima_da_media)