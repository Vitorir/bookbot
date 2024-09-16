# Configurações de Ambiente

## Stage

**ConnectionStrings**: Server=stage_db;Database=myDb;
**JwtSettings**: stage_secret_key
**Logging**: {'Default': 'Warning'}

## Sandbox

**ConnectionStrings**: Server=sandbox_db;Database=myDb;
**JwtSettings**: sandbox_secret_key
**Logging**: {'Default': 'Warning'}

## Production

**ConnectionStrings**: Server=prod_db;Database=myDb;
**JwtSettings**: prod_secret_key
**Logging**: {'Default': 'Error'}

