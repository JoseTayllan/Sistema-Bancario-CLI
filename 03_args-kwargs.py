def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"[{chave.title()}]: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)



exibir_poema(
    "Segunda-feira, 10 de junho de 2025",    
    "Noite estrelada",
    "A noite estrelada",
    "Sob o céu brilhante",
    autor="Vinicius de Moraes",
    ano="2025",
)