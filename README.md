# Aplicacao-Socket
## Proposito do Software
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
Para executar o projeto é necessário ter o python instalado, o projeto foi feito utilizando a versão 3.11.2 do python, para execução da interface do cliente é necessario ter o python 3.10 ou superior.

Para executar o projeto é necessário executar o arquivo `server.py` e o arquivo `interface.py`, o arquivo `server.py` deve ser executado primeiro, pois o arquivo `interface.py` depende dele para funcionar.

Ao sair da interface do usuario o servidor esta configurado para encerrar a execução.

A execução de cliente e servidor pode ser feita em computadores diferentes, para isso o computador que será o servidor deve ter a pasta server baixada, e então nas linhas 6 arquivo `server.py` deve ser alterado o ip para o ip do computador da maquina. Ja o cliente deve ter baixada a pasta client e então na linha 8 do arquivo `cliente.py` deve ser alterado o ip para o ip do computador do servidor.

## Protocolo

### Visão Geral
O protocolo é baseado em requisições e respostas, o cliente faz uma requisição e o servidor responde com os dados solicitados.

Para implementar o protocolo foi utilizado o protocolo TCP/IP, pois ele garante a entrega dos dados e a ordem deles. 


### Mensagens
A tres tipos de mensagens, as de requisição, as de resposta e as de confirmação.
- **Mensagens de requisição:** As requisições são feitas pelo cliente e tem um cabeçalho pra especificar que tipo de solicitação sera feita e com que parametros.
  - Busca: search---"termo_de_busca"---"tipo_de_busca"
    - termo_de_busca: Uma palavra que sera usada para fazer a busca, não pode conter "---".
    - tipo_de_busca: "title" | "genre" | "year" | "director" | "type"
  - Streaming: stream---"id"
    - id: O id do item que o cliente quer ver.
  - Sair: "end---"
- **Mensagens de resposta:** Mensagens do servidor, que faz uma busca nos dados de acordo com solicitação do cliente e retorna os dados que batem com a busca. Uma das formas de resposta é o envio de um arquivo com indices de itens que batem com a busca, a outra forma é o envio do arquivo de um item que o cliente solicitou. As respostas não sao mandadas de uma vez, elas sao mandadas em pacotes de 1024 bytes.
- **Mensagens de confirmação:** Mensagens de confirmação são mensagens que o cliente envia para o servidor para confirmar que ele recebeu a mensagem do servidor. Isso acontece quando o servidor envia o tamanho dos dados de resposta e o cliente manda um OK, ou quando o servidor envia a resposta e o cliente manda um DONE.

### Eventos e Estados
#### Busca
- **Estado Inicial**
  - Ciente: Sem conexão com o servidor.
  - Servidor: Em espera de uma requisição do cliente.
- **Evento de Transição**
  - Cliente: Manda um comando de busca com os parametros de tipo de busca e o termo de busca.
- **Estado Final**
  - Cliente: Com uma lista de indices de itens que batem com a busca e concexao com o servidor fechada.
  - Servidor: Em espera de uma nova requisição.
#### Streaming
 - **Estado Inicial**
   - Cliente: Com uma lista de indices de itens que batem com a busca feita. Sem conexão com o servidor.
   - Servidor: Em espera de uma requisição.
 - **Evento de Transição**
   - Cliente: Manda um comando de streaming com o id do item que ele quer ver.
 - **Estado Final**
   - Cliente: Com o arquivo do item que ele queria ver e a conexão com o servidor fechada.
   - Servidor: Em espera de uma nova conexão.

#### Sair
 - **Estado Inicial**
   - Cliente: Sem conexão com o servidor.
   - Servidor: Em espera de uma requisição.
 - **Evento de Transição**
   - Cliente: Manda um comando de sair.
 - **Estado Final**
   - Cliente: Com a conexão com o servidor e socket fechados.
   - Servidor: Com socket fechado.


### Comunicaçao
Exemplo de execução para o cliente procurar um item por titulo com a palavra 'harry', selecionar o filme 'Harry Potter and the Sorcerer's Stone' com id 1 e então sair do programa.

1. Cliente: search---harry---title
2. Servidor: <tamanho_da_resposta>
3. Clientr: OK
4. Servidor: [{"id": 1, "original_title": "Harry Potter and the Sorcerer's Stone", "title_ptBR": "Harry Potter e a Pedra Filosofal", "type": "filme", "genres": ["Adventure", "Fantasy", "Family"], "year": 2001, "duration": 152, "director": ["Chris Columbus"]}]
   - O servidor envia a resposta em pacotes de 1024 bytes.
5. Cliente: DONE
   
  --Fim da busca--

6. Cliente: stream---1
7. Servidor: <tamanho_do_arquivo>
8. Cliente: OK
9. Servidor: <arquivo_>
   - O servidor envia o arquivo em pacotes de 1024 bytes.
10. Cliente: DONE
   
--Fim do streaming--
1. Cliente: end---

Todas as mensagens são enviadas codificadas e o receptor decodifica elas.


### Requisitos minimos de funcionamento
 - O servidor deve esta executando para que o cliente funcione, não é necessario que o servidor tenha acesso a internet, mas precisa ter acesso a rede local para que o cliente consiga se conectar a ele.
 - O servidor precisa ter acesso a pasta de dados para que ele consiga enviar os arquivos para o cliente.
 - A conectividade pode ser feita apenas um cliente por vez.