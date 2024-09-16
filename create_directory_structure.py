import os
import json

# Define os diretórios dos ambientes e o conteúdo do appsettings.json
ENVIRONMENTS = {
    "stage": {
        "ConnectionStrings": {"DefaultConnection": "Server=stage_db;Database=myDb;"},
        "JwtSettings": {"Secret": "stage_secret_key", "Issuer": "stage_issuer"},
        "Logging": {"LogLevel": {"Default": "Warning"}}
    },
    "sandbox": {
        "ConnectionStrings": {"DefaultConnection": "Server=sandbox_db;Database=myDb;"},
        "JwtSettings": {"Secret": "sandbox_secret_key", "Issuer": "sandbox_issuer"},
        "Logging": {"LogLevel": {"Default": "Warning"}}
    },
    "production": {
        "ConnectionStrings": {"DefaultConnection": "Server=prod_db;Database=myDb;"},
        "JwtSettings": {"Secret": "prod_secret_key", "Issuer": "prod_issuer"},
        "Logging": {"LogLevel": {"Default": "Error"}}
    }
}

def create_directory_structure(base_path):
    for env, settings in ENVIRONMENTS.items():
        env_path = os.path.join(base_path, env)
        os.makedirs(env_path, exist_ok=True)
        file_path = os.path.join(env_path, 'appsettings.json')
        with open(file_path, 'w') as file:
            json.dump(settings, file, indent=2)
        print(f"Arquivo criado: {file_path}")

def main():
    base_path = 'config-simulation'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    create_directory_structure(base_path)

if __name__ == "__main__":
    main()
