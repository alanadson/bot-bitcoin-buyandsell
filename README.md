# 🤖Bot compra e venda automática de Bitcoin

Bot criado para compra e venda de bitcoin ao atingir "X" valor na corretora https://www.bitstamp.net/.


## Instalação

Instale com pip

```
  pip install websocket-client
```
```
  pip install BitstampClient==2.0.3
```
    
## Uso/Exemplos

```Utilize os dados da corretora bitstamp no "credentials.py"
1) Faça login na sua conta Bitstamp
2) Clique em Segurança -> Acesso à API
3) Selecione as permissões que você deseja ter para sua chave de acesso (se você não marcar nenhuma caixa, receberá a mensagem de erro 'Nenhuma permissão encontrada' após cada chamada de API)
4) Clique no botão 'Gerar chave' e não se esqueça de anotar seu Segredo!
5) Clique em 'Ativar'
6) Vá para sua caixa de entrada e clique no link enviado por Bitstamp para ativar esta chave de API
USER='YOUR USER'
KEY='YOUR KEY'
SECRET='YOUR SECRET'
```

