import os
import json

# Define os diretórios dos ambientes e os arquivos appsettings.json
ENVIRONMENTS = {
    "STAGE": "stage/appsettings.json",
    "SANDBOX": "sandbox/appsettings.json",
    "PRODUÇÃO": "production/appsettings.json"
}

# Chaves específicas para extrair do appsettings.json
KEYS_TO_EXTRACT = ["ConnectionStrings", "JwtSettings", "Logging"]

def read_appsettings(filepath):
    """Lê o conteúdo do appsettings.json"""
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o JSON em {filepath}")
        return None

def extract_keys(data, keys):
    """Extrai os valores das chaves específicas do appsettings.json"""
    extracted_data = {}
    for key in keys:
        extracted_data[key] = data.get(key, "Chave não encontrada")
    return extracted_data

def create_readme(content):
    """Cria o arquivo README.md com o conteúdo formatado"""
    with open("README.md", "w") as readme_file:
        readme_file.write("# Configurações do App\n\n")
        for env, env_content in content.items():
            readme_file.write(f"## {env} Environment\n\n")
            for key, value in env_content.items():
                readme_file.write(f"**{key}**: {json.dumps(value, indent=2)}\n\n")
        print("README.md criado com sucesso!")

def main():
    readme_content = {}

    # Itera sobre cada ambiente para extrair as chaves e seus valores
    for env, path in ENVIRONMENTS.items():
        print(f"Lendo arquivo de {env}...")
        data = read_appsettings(path)
        if data:
            extracted_data = extract_keys(data, KEYS_TO_EXTRACT)
            readme_content[env] = extracted_data
        else:
            print(f"Não foi possível ler o arquivo para {env}.")

    # Gera o README.md
    create_readme(readme_content)

if __name__ == "__main__":
    main()
