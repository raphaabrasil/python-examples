''' 5-Dict.py '''

dados = {"nome": "Raphael", "idade": 22}

dados["nome"]                 # "Raphael"
dados["idade"] += 1           # 23

"nome" in dados               # True
"sobrenome" in dados		  # False

dados.get("likes", 0)         # Se a chave não existir, retorna 0

dados.keys()                  # ["nome", "idade"]
dados.values()                # ["Raphael", 23]
