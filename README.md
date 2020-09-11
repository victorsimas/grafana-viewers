# Grafana Viewers
A ideia deste projeto é disponibilizar a entrega de paineis renderizados utilizando a API do Grafana de busca e renderização, sendo um filtro para aplicações como BOTs.

## Como rodar?
Inicie o ambiente virtual e instale as dependencias:
- pipenv shell
- pipenv install

No caso do vscode, talvez seja necessário configurar o python path do seu ambiente virtual:
```
"python.pythonPath": <caminho>
```
Para localizar, dentro do ambiente virtual execute:
- pipenv --venv

## Requisitos
- Uma instância do grafana com o plugin de renderização
- Configurar as variaveis de ambiente para execução, passando o host acompanhado do protocolo (http ou https) e o token de acesso

## Variaveis de Ambiente
- TOKEN_GRAFANA
- HOST_GRAFANA

![Grafana-Viewers](grafana_viewers_icon.png)