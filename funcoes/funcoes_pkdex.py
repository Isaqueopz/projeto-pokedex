from modulos import requests

def pesquisar(nome_pokemon_ou_id):
        nome_pokemon_ou_id = nome_pokemon_ou_id.lower()  # A API exige o nome em minúsculo
        url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon_ou_id}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Levanta uma exceção para qualquer erro HTTP
        except requests.exceptions.RequestException as err:
            # Tratar qualquer erro de requisição (conexão, timeout, etc.)
            return {"erro": f"Erro ao acessar a API: {err}"}

        if response.status_code == 200:
            dados = response.json()

            pokemon_info = {
                'nome': dados['name'],
                'tipos': [tipo['type']['name'] for tipo in dados['types']],
                'id': dados['id'],
                'habilidade': [habilidade['ability']['name'] for habilidade in dados['abilities']],
                'altura': dados['height'],
                'peso': dados['weight'],
                'base_experience': dados['base_experience'],
            }
            return pokemon_info
        else:
            return {"erro": "Pokémon não encontrado ou houve um problema na requisição."}

def printar_info_pokemon(info):
    try:
        print(f"Nome: {info['nome']}")
        print(f"(ID: {info['id']})")
        print(f"Tipos: {', '.join(info['tipos'])}")
        print(f"Habilidades: {', '.join(info['habilidade'])}")
        print(f"Altura: {info['altura']} decímetros")
        print(f"Peso: {info['peso']} hectogramas")
    except KeyError:
        print("Nome ou ID inválido!")

def printar_primeiro_pokemon_ou_ultimo(posicao):
    if posicao == "primeiro":
        info = pesquisar("1")
        try:
            print(f"Nome: {info['nome']}")
            print(f"(ID: {info['id']})")
            print(f"Tipos: {', '.join(info['tipos'])}")
            print(f"Habilidades: {', '.join(info['habilidade'])}")
            print(f"Altura: {info['altura']} decímetros")
            print(f"Peso: {info['peso']} hectogramas")
        except KeyError:
            print("Nome ou ID inválido!")
    else:
        posicao == "ultimo"
        info = pesquisar("1025")
        try:
            print(f"Nome: {info['nome']}")
            print(f"(ID: {info['id']})")
            print(f"Tipos: {', '.join(info['tipos'])}")
            print(f"Habilidades: {', '.join(info['habilidade'])}")
            print(f"Altura: {info['altura']} decímetros")
            print(f"Peso: {info['peso']} hectogramas")
        except KeyError:
                print("Nome ou ID inválido!")
    
def batalha_pokemons(pokemon1, pokemon2):
    info1 = pesquisar(pokemon1)
    info2 = pesquisar(pokemon2)

    if 'erro' in info1 or 'erro' in info2:
        return "Erro ao buscar informações de um ou ambos os Pokémon."

    base_experience_1 = info1.get('base_experience',0 )  
    base_experience_2 = info2.get('base_experience',0)  

    if base_experience_1 > base_experience_2:
        print (f"{info1['nome']} venceu a batalha!")
    elif base_experience_1 < base_experience_2:
        print (f"{info2['nome']} venceu a batalha!")
    else:
        print("A batalha terminou em empate!")
