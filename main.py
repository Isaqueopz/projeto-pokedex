from funcoes.funcoes_pkdex import pesquisar

# Teste com um Pokémon
pokemon_nome = "corno"
info = pesquisar(pokemon_nome)
print(info)


# if erro in info:
#     print(info['erro'])
# else:
print(f"Nome: {info['nome']}")
print(f"Tipos: {', '.join(info['tipos'])}")
print(f"Habilidades: {', '.join(info['habilidade'])}")
print(f"Altura: {info['altura']} decímetros")
print(f"Peso: {info['peso']} hectogramas")