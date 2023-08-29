# README - Documentação dos Códigos

Este é um README que fornece documentação para os códigos neste repositório. Ele contém informações sobre os diferentes arquivos, suas funcionalidades e como executá-los corretamente.

## Arquivos

1. **app.py**: Este é o arquivo principal que contém a lógica principal do aplicativo. Ele importa outros módulos e realiza operações com base nas escolhas do usuário. O programa começa limpando a tela e cria um arquivo com a função `ca.criararquivo()`. Em seguida, entra em um loop while para exibir um menu e aguardar as entradas do usuário. Dependendo da escolha do usuário, diferentes ações são executadas, como visualizar transações, adicionar, atualizar ou excluir dados, ou encerrar o programa.

2. **Formatacao/Formatacao_Menu.py**: Este arquivo contém funções para formatação e exibição do menu. Ele importa as funções necessárias para formatar o cabeçalho e os tópicos do menu, que são usados no arquivo `app.py`.

3. **Manipulacao_de_arquivos/criação_de_arquivo.py**: Este arquivo contém a função `criararquivo()`, que é chamada no arquivo `app.py` para criar um arquivo. Ele retorna o nome do arquivo criado.

4. **CRUD/leitor_de_dados.py**: Este arquivo contém funções para ler dados do arquivo. Ele inclui a função `ler_saldo_total()`, que lê o saldo total do arquivo; a função `ler()`, que lê todas as transações do arquivo; e a função `ler_filtrado_por_categoria()`, que lê transações filtradas por categoria. Essas funções são usadas no arquivo `app.py` para exibir as informações solicitadas pelo usuário.

5. **CRUD/adicionador_de_dados.py**: Este arquivo contém a função `adicionar()`, que é responsável por adicionar uma nova transação ao arquivo. Ele é chamado no arquivo `app.py` quando o usuário escolhe a opção de adição.

6. **CRUD/atualizador_de_dados.py**: Este arquivo contém a função `atualizar()`, que é responsável por atualizar uma transação existente no arquivo. Ele é chamado no arquivo `app.py` quando o usuário escolhe a opção de atualização.

7. **CRUD/deletador_de_dados.py**: Este arquivo contém a função `deletar()`, que é responsável por excluir uma transação do arquivo. Ele é chamado no arquivo `app.py` quando o usuário escolhe a opção de deleção.

8. **.gitignore**: Este arquivo contém as configurações do Git para ignorar certos arquivos e diretórios durante o versionamento. Ele especifica quais arquivos e tipos de arquivos devem ser excluídos do controle de versão. Isso inclui arquivos compilados, arquivos de configuração específicos do ambiente e arquivos gerados automaticamente.

## Execução

Para executar o aplicativo, certifique-se de ter todos os arquivos necessários no mesmo diretório. Em seguida, execute o arquivo `app.py` usando o interpretador Python. O programa exibirá um menu e aguardará as entradas do usuário. Siga as instruções exibidas no menu para realizar as diferentes

   ## Membros

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Thomazrlima">
        <img src="https://avatars3.githubusercontent.com/Thomazrlima" width="100px;" alt="Foto de Thomaz"/><br>
        <sub>
          <b>Thomaz R. Lima</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/evaldocunhaf">
        <img src="https://avatars3.githubusercontent.com/evaldocunhaf" width="100px;" alt="Foto de Evaldo"/><br>
        <sub>
          <b>Evaldo G. Filho</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/hsspedro">
        <img src="https://avatars.githubusercontent.com/hsspedro" width="100px;" alt="Foto de Pedro"/><br>
        <sub>
          <b>Pedro S. Souza</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Luiz-Edu0202">
        <img src="https://avatars.githubusercontent.com/Luiz-Edu0202" width="100px;" alt="Foto de Dustin"/><br>
        <sub>
          <b>Luiz Eduardo Brayner</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Sofia-Saraiva">
        <img src="https://avatars.githubusercontent.com/Sofia-Saraiva" width="100px;" alt="Foto de Sofia"/><br>
        <sub>
          <b>Sofia Saraiva</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
