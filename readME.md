# Projeto & Dor

Desenvolvo SaaS no dia-a-dia e uma dos produtos que criei quebrou e infelizmente ainda não tem como reprocessar Webhooks na Evermart. A solução que encontrei foi baixar o xlsx do período que quebrou e processar as informações.

O código apenas faz a leitura do XLSX formatado da Evermart, vai de você escolher o que deseja fazer com a formatação dessa informação do XLSX.

Você pode executar em um modelo de Machine Learning ou então, enviar e-mail automaticamente para esses usuários, ou SMS. O céu não é o limite para a criatividade.

Enjoy.

# Como rodar esse código

Precisa ter Python 3.9 instalado no computador, e basta utilizar o código `pip install -r requirements.txt` e depois `python main.py` para rodar o código. É necessário possuír um arquivo chamado `pedidos.xlsx` aonde está localizado o arquivo `main.py`
