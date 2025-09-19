import requests

def get_pokemon_list(limit=151):
    """Fetch list of first N Pokémon names and URLs."""
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['results']

def get_pokemon_details(pokemon_url):
    """Fetch Pokémon type(s) and base stats from detail API."""
    response = requests.get(pokemon_url)
    response.raise_for_status()
    data = response.json()

    # Extract types
    types = [t['type']['name'] for t in data['types']]

    # Extract stats (attack, defense, hp, etc.)
    stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}

    return {
        "name": data['name'],
        "types": types,
        "stats": stats
    }

if __name__ == "__main__":
    # Get first 151 Pokémon
    pokemon_list = get_pokemon_list(151)

    # Example: fetch details for first 5 Pokémon
    for poke in pokemon_list[:5]:
        details = get_pokemon_details(poke['url'])
        print(f"Name: {details['name'].capitalize()}")
        print(f"Types: {', '.join(details['types'])}")
        print(f"Stats: {details['stats']}")
        print("-" * 40)

