from modulos import requests

def pesquisar(nome_pokemon):
    nome_pokemon = nome_pokemon.lower()  # A API exige o nome em minúsculo
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    
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
            'habilidade': [habilidade['ability']['name'] for habilidade in dados['abilities']],
            'altura': dados['height'],
            'peso': dados['weight']
        }
        return pokemon_info
    else:
        return {"erro": "Pokémon não encontrado ou houve um problema na requisição."}


