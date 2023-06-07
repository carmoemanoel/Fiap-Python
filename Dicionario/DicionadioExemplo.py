
# Criando uma lista para saber o comportamento dela
usuarios = {"chaves" : ["chaves do 8", "24/12/2017", "Recep_01"],
             "quico": ["Quico das Flores", "20/12/2017", "Raiox_03"]
             }
print(usuarios)

# No exemplo abaixo é exemplificado como se insere um novo usuário no Dicionário 
usuarios ["Florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]

print(usuarios)

print("####------####")
# Essa maneira é uma das forma onde eu consigo puxar, acessar uma informação no Dicionário
print(usuarios.get("quico"))