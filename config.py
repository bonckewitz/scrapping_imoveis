# Parâmetros globais de configuração
list = []

# Funções de parâmetros de requisição
def configurar_parametros(auth: str, path: str, referer: str):
    params = {
        "authority": auth,
        "method": "GET",
        "path": path,
        "scheme": "https",
        "referer": referer,
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    return params

# Função para criar JSON
def criar_registro(dataPostagem, titulo, tamanho, quartos, banheiros, vagas, tipo, preco, url, regiao, regiaoCidade, resumo):
    print("titulo: " + str(titulo))
    print("Preco: " + str(preco))
    print(regiao)
    print(url)
    print(resumo)
    print("----")
    
    json = { 
        "preco": preco,
        "metragem": tamanho,
        "quartos": quartos,
        "banheiros": banheiros,
        "vagas": vagas,
        "tipo": tipo,
        "titulo": titulo,
        "regiao": regiao,
        "dataPostagem": dataPostagem,
        "regiaoCidade": regiaoCidade, 
        "resumo": resumo,
        "url": url,
    }
    
    list.append(json)
