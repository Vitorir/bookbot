import os
import json

# Diretório onde os arquivos appsettings.json estão localizados
BASE_DIR = 'config-simulation'
ENVIRONMENTS = ['stage', 'sandbox', 'production']

# Chaves que desejamos extrair
KEYS_TO_EXTRACT = {
    'ConnectionStrings': 'DefaultConnection',
    'JwtSettings': 'Secret',
    'Logging': 'LogLevel'
}

def read_appsettings(env):
    file_path = os.path.join(BASE_DIR, env, 'appsettings.json')
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_values(data, keys):
    result = {}
    for key, sub_key in keys.items():
        if key in data:
            if sub_key in data[key]:
                result[key] = data[key][sub_key]
            else:
                result[key] = 'N/A'
        else:
            result[key] = 'N/A'
    return result

def write_readme():
    readme_path = 'README.md'
    with open(readme_path, 'w') as file:
        file.write('# Configurações de Ambiente\n\n')
        
        for env in ENVIRONMENTS:
            file.write(f'## {env.capitalize()}\n\n')
            appsettings = read_appsettings(env)
            values = extract_values(appsettings, KEYS_TO_EXTRACT)
            
            for key, value in values.items():
                file.write(f'**{key}**: {value}\n')
            
            file.write('\n')

    print(f"Arquivo README.md criado em: {os.path.abspath(readme_path)}")

def main():
    write_readme()

if __name__ == "__main__":
    main()
