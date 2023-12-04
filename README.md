# Aplicacao-Socket
## Aplicação
O projeto simula um streaming, o cliente faz uma busca e então o servidor retornar os resultados que batem com a busca, o cliente pode solicitar ver um item em específico e o servidor iria enviar o arquivo para ele.

A pasta `server` contém os código do servidor e a pasta `client` contém os código do cliente.

### Server
Na parte do servidor existem três partes, o `server.py`, o `CiCflix.py` e uma pasta de dados.
 - O `server.py` é o arquivo que contém o código do servidor, ele é responsável por receber as requisições do cliente e enviar os dados para ele.
 - O `CiCflix.py` é o arquivo que contém a classe `CiCflix`, ela é responsável por fazer a leitura dos dados pode enviar a resposta para o cliente acerca de pesquisas feitas ou solicitações de arquivos.
 - A pasta de dados contém os arquivos que serão enviados para o cliente.
  
### Dados
Na pasta dados existe um arquivo chamado `index.json`, ele contém os indices dos filmes e séries que estão disponíveis para serem enviados para o cliente. 

No cada item tem:

    - `id`: O id do item.
    - `original_title`: O titulo original do item.
    - `title_ptBR`: O nome em portugues do item.
    - `type`: O tipo do item, podendo ser 'filme' ou 'serie'.
    - `genres`: Uma lista de generos do filme.
  
Existem divergencia de atributos entre filmes e séries, os atributos que são exclusivos de filmes são:

    - `year`: O ano que o filme foi lançado.
    - `duration`: A duração em minutos do filme.
    - `director`: Uma lista de diretores do filme.
  
Os atributos que são exclusivos de séries são:

    - `premiered`: A data de estreia da série, no formato 'YYYY-MM-DD'.
    - `seasons`: O número de temporadas do item.
    - `creator`: Uma lista de criadores da serie.

Ainda na pasta de dados existem varias pastas com numeros como nome, cada pasta contém os arquivos de um item, o nome da pasta corresponde ao id do item. Dentro de cada uma dessas pastas de itens existe apenas um arquivo chamado `file.txt`, ele contém o conteúdo do arquivo que será enviado para o cliente e simula o streaming de um video.

### Cliente
O cliente é responsável por fazer as requisições para o servidor e receber os dados que ele envia.

O arquivo `cliente.py` faz a conexão com o servidor e envia as requisições para ele, ele também é responsável por receber os dados que o servidor envia.

O arquivo `interface.py` faz a interface com o usuário, e é responsável por receber os comandos do usuário e enviar para o `cliente.py` fazer as requisições.

## Como executar
Para executar o projeto é necessário ter o python instalado, o projeto foi feito utilizando a versão 3.11.2 do python, mas deve funcionar em versões mais antigas do pyhton 3.

Para executar o projeto é necessário executar o arquivo `server.py` e o arquivo `interface.py`, o arquivo `server.py` deve ser executado primeiro, pois o arquivo `interface.py` depende dele para funcionar.

Ao sair da interface do usuario o servidor esta configurado para encerrar a execução.

A execução de cliente e servidor pode ser feita em computadores diferentes, para isso o computador que será o servidor deve ter a pasta server baixada, e então nas linhas 6 arquivo `server.py` deve ser alterado o ip para o ip do computador da maquina. Ja o cliente deve ter baixada a pasta client e então na linha 8 do arquivo `cliente.py` deve ser alterado o ip para o ip do computador do servidor.

## Protocolo

### Visão Geral


### Estrutura do Protocolo

- **Arquitetura:** Explique a arquitetura geral do protocolo, incluindo como os dados são organizados e transmitidos.

### Formato de Mensagens

- **Cabeçalhos e Corpos de Mensagem:** Descreva a estrutura de uma mensagem típica, incluindo informações sobre cabeçalhos, dados e metadados.
- **Codificação de Dados:** Especifique como os dados são codificados nas mensagens (por exemplo, JSON, XML, binário).

### Operações e Comandos

- **Lista de Operações:** Enumere todas as operações suportadas pelo protocolo.
- **Descrição de Operações:** Forneça informações detalhadas sobre cada operação, incluindo os parâmetros esperados e os resultados retornados.

### Comportamento do Cliente e do Servidor

- **Fluxo de Comunicação:** Ilustre os cenários de comunicação típicos entre clientes e servidores.
- **Gestão de Conexão:** Explique como a conexão é estabelecida, mantida e encerrada.

### Exemplos e Cenários

- **Exemplos de Uso:** Forneça exemplos práticos de como usar o protocolo em diferentes situações.
- **Cenários de Erro:** Descreva possíveis cenários de erro e como lidar com eles.

### Segurança

- **Considerações de Segurança:** Identifique as práticas recomendadas para garantir a segurança ao utilizar o protocolo.
- **Criptografia:** Se necessário, explique como a criptografia é aplicada para proteger a comunicação.

### Referência de API

- **Lista de Funções ou Métodos:** Forneça uma referência clara de todas as funções ou métodos disponíveis para os desenvolvedores.

### Configuração

- **Parâmetros de Configuração:** Se houver parâmetros de configuração, liste-os e explique seu impacto na operação do protocolo.

### Exigências do Ambiente

- **Requisitos de Sistema:** Especifique os requisitos mínimos do sistema para implementar o protocolo.