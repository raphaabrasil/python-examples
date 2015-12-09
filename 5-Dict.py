# coding:utf-8

''' 5-Dict.py '''

dados = {"nome": "Raphael", "idade": 22}

dados["nome"]                  # "Raphael"
dados["idade"] += 1            # 23

"nome" in dados                # True
"sobrenome" in dados		   # False

dados.get("likes", 0)          # Se a chave não existir, retorna 0

dados.keys()                   # ["nome", "idade"]
dados.values()                 # ["Raphael", 23]

dados['sobrenome'] = 'Brasil'  # Adicionando uma chave no dict

dados.keys()                   # ["idade", "nome", "sobrenome"]
dados.values()                 # [23, "Raphael", "Brasil"]

del dados['sobrenome']		   # Removendo uma chave do dict

dados.keys()                   # ["idade", "nome"]
