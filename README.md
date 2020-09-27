# Grafana Viewers
A ideia deste projeto é disponibilizar a entrega de paineis renderizados utilizando a API do Grafana de busca e renderização, sendo um filtro para aplicações como BOTs.

## Como rodar?
Inicie o ambiente virtual e instale as dependencias:
- pipenv shell
- pipenv install

Para instalar na maquina as dependencias:
- pipenv install --system --deploy --ignore-pipfile

Rode o app.py com o python3.8 ou maior

## Visual studio code envFile

```
{
    "python.pythonPath": "<python_path_venv>",
    "python.envFile": "${workspaceFolder}/<envFile>"
}

```

Para localizar, dentro do ambiente virtual execute:
- pipenv --venv

## Contrato


```

{
    "metodo": "GET",
    "endpoint": "/grafana/search",
    "queryParms": [
        {
            "name": dashTitulo,
            "isOptional": true
        },
        {
            "name": painelTitulo,
            "isOptional": false
        },
        {
            "name": tag,
            "isOptional": false
        },
        {
            "name": tempo,
            "isOptional": true
        }
    ]
}

```


## Requisitos
- Uma instância do grafana com o plugin de renderização
- Configurar as variaveis de ambiente para execução, passando o host acompanhado do protocolo (http ou https) e o token de acesso

## Variaveis de Ambiente
- TOKEN_GRAFANA
- HOST_GRAFANA

![Grafana-Viewers](grafana_viewers_icon.png)