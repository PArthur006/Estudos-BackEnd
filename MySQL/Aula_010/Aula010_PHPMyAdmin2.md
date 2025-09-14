# Aula 10: PHPMyAdmin na Prática (Parte 2)
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. Visão Geral da Interface

O PHPMyAdmin organiza as funcionalidades em abas, permitindo que as operações de SQL que aprendemos via código sejam realizadas de forma visual e interativa. Esta aula demonstrou o mapeamento entre os comandos e as ações na interface.

### 2. Mapeamento de Comandos DDL (Estrutura)

| Ação Desejada | Comando SQL (O que aprendemos) | Ação no PHPMyAdmin |
| :--- | :--- | :--- |
| **Criar um Banco de Dados** | `CREATE DATABASE nome;` | Na tela inicial, usar a seção "Criar novo banco de dados". |
| **Criar uma Tabela** | `CREATE TABLE nome (...);` | Dentro de um banco de dados, usar a seção "Criar nova tabela". |
| **Ver Estrutura da Tabela** | `DESCRIBE nome_tabela;` | Clicar na tabela e ir para a aba **"Estrutura"**. |
| **Modificar Tabela/Coluna** | `ALTER TABLE ...;` | Na aba **"Estrutura"**, usar os ícones de "Mudar" (renomear/modificar), "Apagar" (remover coluna), ou as opções abaixo da lista de colunas. |
| **Apagar uma Tabela** | `DROP TABLE nome_tabela;` | Na lista de tabelas, marcar a tabela e selecionar a opção "Eliminar" (ou "Drop"). |

---

### 3. Mapeamento de Comandos DML (Dados)

| Ação Desejada | Comando SQL (O que aprendemos) | Ação no PHPMyAdmin |
| :--- | :--- | :--- |
| **Inserir Dados** | `INSERT INTO ... VALUES ...;` | Clicar na tabela e ir para a aba **"Inserir"**. Preencher o formulário com os dados do novo registro. |
| **Visualizar Dados** | `SELECT * FROM ...;` | Clicar na tabela e ir para a aba **"Procurar"** (ou "Browse"). Os dados são exibidos em uma grade. |
| **Editar um Registro** | `UPDATE ... SET ... WHERE ...;` | Na aba **"Procurar"**, clicar no botão "Editar" da linha desejada. Alterar os valores e salvar. |
| **Apagar um Registro** | `DELETE FROM ... WHERE ...;` | Na aba **"Procurar"**, clicar no botão "Apagar" (ou "Delete") da linha desejada. |

---

### 4. Execução Direta de SQL e Gerenciamento

-   **Executar Comandos Manuais:** A aba **"SQL"** oferece um campo de texto onde é possível escrever e executar qualquer comando SQL. É o equivalente direto do terminal ou do editor do VS Code, com a vantagem de exibir os resultados em uma tabela formatada.

-   **Exportar (Backup/Dump):** A aba **"Exportar"** permite gerar o arquivo `.sql` de backup. É possível escolher entre o método "Rápido" (gera com as configurações padrão) ou "Personalizado" (permite escolher quais tabelas exportar, o formato, etc.).

-   **Importar (Restaurar):** A aba **"Importar"** é usada para restaurar um banco de dados. O usuário clica em "Escolher arquivo", seleciona o arquivo `.sql` do seu computador e executa a importação.

### 5. Conclusão

O PHPMyAdmin atua como um "tradutor" visual para os comandos SQL. Cada clique em um botão ou preenchimento de formulário está, nos bastidores, gerando e executando um comando SQL correspondente no banco de dados.