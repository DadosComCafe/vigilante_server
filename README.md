# Vigilante Server
- Um produtor de relatórios que roda em um servidor gradio.

## Sobre
Como desenvolvedor, cientista ou engenheiro de dados, é muito comum haver a necessidade de validar certos conjuntos de dados, sejam eles gerados por ingestão, construção de novos processos ou afins, não importa, a validação é parte fundamental do processo. Logo, é através da mesma que garantimos que os dados não foram perdidos ao longo do processo. 

No entanto, a geração de evidências acaba sendo um processo chato, e repetitivo. Imagine um cenário onde é necessário a construção de relatórios (planilhas xlsx) tornando a visualização e identificação de ocorrências mais fácil. A comodidade obtida tem um alto custo.

Este projeto possui como objetivo a criação de um servidor gradio, onde o usuário envia um arquivo xlsx, e o servidor retorna para o usuário um arquivo xlsx contendo o relatório da análise quantitativa e um outro da análise qualitativa. Automatizando todo o processo de geração de relatórios.


## Como Usar
    - __Clone o repositório:__
        - git clone https://github.com/DadosComCafe/vigilante_server
    
    - __Preparar o ambiente e instalar dependências:__
        - cd vigilante_server `para acessar o diretório raíz do projeto`
        - uv sync `para sincronizar com as dependências listadas no pyproject.toml`
    
    - __Rodar o servidor:__
        - uv run main.py
    
    - __Acessar o servidor:__
        - O servidor estará disponível em: http://127.0.0.1:7860/
        - Pronto! Agora é possível enviar um xlsx de uma planilha, que será retornado um outro xlsx com as métricas das colunas numéricas desta planilha
    
    - __Parar o servidor:__
        - No terminal onde o servidor está executando, pressione ctrl + c.
        - Pronto! Seu terminal será interrompido.


## Ferramentas utilizadas no projeto
- ### __gradio__:
    - Framework simples, mas poderoso, para tornar fácil a criação de um servidor python. Uma alternativa ao Streamlit

- ### __python_sample_xlsx_report__:
    - Biblioteca desenvolvida com o intuito de tornar fácil e rápida a produção de relatórios xlsx. Ainda em desenvolvimento, mas atualmente funciona gerando relatórios da análise quantitativa de um xlsx fornecido.
    - Biblioteca disponível no pypi, sendo possível instalá-la com o pip ou qualquer outro gerenciador de pacotes python (como é o caso, o uv):
    https://pypi.org/project/python-sample-xlsx-report/ 


## Docker
Caso desejado, é possível subir o servidor através do docker. Para buildar a imagem siga os passos:

### __Buildar__
- Certifique-se de estar com o terminal aberto na raíz do projeto, e execute:
    - docker build -t generate_report .

### __Levantar o container__
- Certifique-se de ter executado o passo anterior, e de substituir `generate_report` por um nome a sua escolha. Então execute:
    - docker run -p 7860:7860 generate_report
    - O servidor estará acessível em http://localhost:7860/
