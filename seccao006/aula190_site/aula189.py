# O módulo requests para requisições HTTP no Python
# HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e receber
# dados na internet. Ele funciona no modo cliente/servidor, onde cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor
# (site, por exemplo) e o servidor responde ao cliente com dados adequados.
#
# A mensagem de requisição do cliente deve incluir dados como:
# - o método HTTP
#   - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#   - escrita (safe) - POST, PUT (substitui), PATCH (atualiza), DELETE
# - o endereço do recurso a ser acessado (/users/)
# - os cabeçalhos HTTP (Content-Type, Accept, Authorization, etc)
# - o corpo da mensagem (caso necessário, de acordo com o método)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - o código de status HTTP (200 success, 404 not found, 301 moved permanently)
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
# - os cabeçalhos HTTP (Content-Type, Content-Length, etc)
# - o corpo da mensagem (pode estar vazio em alguns casos)
