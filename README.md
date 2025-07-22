# RecruitScope CLI

Esta é uma ferramenta de linha de comando (CLI) para auxiliar recrutadores analisar e visualizar a atividade de um usuário no GitHub.

## Funcionalidades

- Busca informações públicas do perfil do usuário no GitHub  
- Lista principais dados: nome, bio, localização, seguidores, repositórios públicos, total de estrelas, etc.  
- Mostra o repositório mais popular do usuário  
- Exibe as principais linguagens usadas  
- Salva os dados em arquivo JSON localmente  
- Interface bonita e interativa com a biblioteca [rich](https://github.com/Textualize/rich)

## Como usar

### Pré-requisitos

- Python 3.6 ou superior  
- Instalar dependências:

```bash
pip install -e .
```

## Como usar

Via linha de comando (CLI):
Execute o comando abaixo, substituindo <github_username> pelo nome do usuário GitHub que deseja analisar:

```bash
recruitscope <github_username>
```

Os dados serão exibidos no terminal e também salvos no arquivo <github_username>_profile.json.
