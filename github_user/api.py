import requests

def ghApi(userData):
    baseURL = 'https://api.github.com'
    
    perfilURL = f"{baseURL}/users/{userData}"
    reposURL = f"{baseURL}/users/{userData}/repos?per_page=100"
    
    perfilResp = requests.get(perfilURL)
    if perfilResp.status_code != 200:
        print(f'ERROR: {perfilResp.status_code}')
        return {"error": f"User not found or API error ({perfilResp.status_code})"}
    
    profile = perfilResp.json()

    reposResp = requests.get(reposURL)
    if reposResp.status_code != 200:
        repos = []
    else:
        repos = reposResp.json()
        
    linguagens = {}
    total_stars = 0
    popular = None

    for repo in repos:
        total_stars += repo.get('stargazers_count', 0)
            
        lang = repo.get('language')
        if lang:
            linguagens[lang] = linguagens.get(lang, 0) + 1 

        if not popular or repo['stargazers_count'] > popular['stargazers_count']:
            popular = repo

    resultado = {
        "usuario": profile['login'],
        "nome": profile.get('name'),
        "bio": profile.get('bio'),
        "localizacao": profile.get('location'),
        "desde": profile['created_at'][:10],
        "seguidores": profile['followers'],
        "seguindo": profile['following'],
        "repos_publicos": profile['public_repos'],
        "total_estrelas": total_stars,
        "repo_mais_popular": {
            "nome": popular['name'],
            "estrelas": popular['stargazers_count']
        } if popular else None,
        "linguagens_usadas": linguagens
    }

    return resultado