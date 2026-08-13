PROJETO DE FIXAÇÃO — SQL📊 E PYTHON🐍

Criei um Sistema de Cadastro de Passageiros de Ônibus com Inspiração na empresa que eu trabalho atualmente, ela faz serviços de transporte publico.

1. Sobre o Projeto

Eu desenvolvi esse projeto com o objetivo de exercitar a sintaxe e os conceitos fundamentais das linguagens Python e SQL. Esse sistema de cadastro de passageiros de ônibus, executa no terminal, fiz na IDE PyCharm, utilizando o banco de dados SQLite como base de armazenamento.
O projeto foi estruturado em dois arquivos com responsabilidades separadas, um arquivo dedicado exclusivamente à comunicação com o banco de dados, e outro dedicado à interação com o usuário através de um menu no terminal. Essa separação já representa, por si só, um conceito importante de organização de código.

2. Fundamentos de Python Praticados 

Eu utilizei uma estrutura básica para reaproveitar blocos de código sem repetição, recebendo dados de entrada e devolvendo resultados.
Estruturas condicionais, uso de if, elif e else para direcionar o programa conforme a escolha feita pelo usuário no menu.
Laço de repetição while, fiz o uso do laço while para manter o menu em execução contínua até que o usuário decida encerrar o programa.
Laço de repetição for, uso do laço for para percorrer os resultados vindos do banco de dados e exibir um a um.
Entrada de dados input, captura de texto digitado pelo usuário no terminal, e conversão de texto para número quando necessário (idade e identificador).
Formatação de texto, com o uso de strings para compor mensagens formatadas, combinando texto fixo com valores armazenados em variáveis.
Listas e tuplas, compreensão de listas e tuplas como estruturas usadas para armazenar múltiplos valores, especialmente ao lidar com os resultados retornados pelo banco de dados.
Padrão if __name__ == "__main__", entendimento da diferença entre código executado apenas quando o arquivo é rodado diretamente e código que fica disponível para importação em outros arquivos.
Modularização, utilizei conceitos de organização do código em múltiplos arquivos, cada um com uma função específica dentro do projeto.

3. Fundamentos de SQL Praticados

CREATE TABLE: criação de uma tabela no banco de dados, definindo colunas, tipos de dado e uma chave primária com incremento automático.
INSERT INTO: inserção de novos registros na tabela, com valores enviados de forma segura por meio de parâmetros.
SELECT: consulta e recuperação dos dados armazenados na tabela, tanto para listagem completa quanto para buscas filtradas.
WHERE / LIKE: aplicação de filtros nas consultas, incluindo busca parcial de texto utilizando o operador LIKE.
UPDATE: modificação de um registro já existente, sempre localizado por meio de um identificador específico.
DELETE: remoção de um registro específico da tabela, também localizado por meio de um identificador.
Confirmação de alterações (commit): entendimento da diferença entre executar um comando e efetivamente gravá-lo no arquivo do banco de dados.

4. Integração entre Python e SQL

Além dos fundamentos de cada linguagem, o projeto permitiu praticar a integração entre elas, por meio do módulo nativo do Python responsável pela comunicação com bancos de dados SQLite. Foram exercitados os conceitos de conexão com o banco, uso de um cursor para executar comandos, envio de parâmetros de forma segura, e o fechamento adequado da conexão ao final de cada operação.
Também fez parte do processo o exercício de identificação e correção de erros, incluindo problemas de indentação, erros de digitação em palavras-chave do SQL e o uso correto da sintaxe de tuplas em Python, situações que me ensinaram bastante conceitos de programação e que reforçam a atenção a detalhes de sintaxe.

5. Considerações Finais

Fiz o projeto com a intenção de exercitar, de forma prática os principais fundamentos de Python e SQL, trabalhando com variáveis, estruturas condicionais, laços de repetição, funções, manipulação de texto e número, além dos comandos essenciais de manipulação de banco de dados. O tema escolhido, relacionado ao contexto de trabalho no setor de monitoramento de transporte coletivo, contribuiu para tornar o exercício mais próximo da realidade prática.
