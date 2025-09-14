# Aula 08: Gerenciando Cópias de Segurança (Backup)
**Fonte:** Métodos Padrão de Linha de Comando (Universal)

> **Aviso:** O conteúdo desta anotação descreve o processo de backup (exportação) e restauração (importação) de um banco de dados MySQL utilizando o **terminal (linha de comando)**. Este é o método padrão, gratuito e universal usado por profissionais, sendo uma alternativa às ferramentas gráficas que podem ter limitações ou funcionalidades pagas.

---

### 1. Conceito de DUMP

Um "DUMP" é um arquivo de texto, geralmente com a extensão `.sql`, que contém todos os comandos SQL necessários para recriar a estrutura (`CREATE TABLE`) e os dados (`INSERT INTO`) de um banco de dados. É a forma mais comum de se criar uma cópia de segurança (backup).

### 2. Ferramentas Utilizadas

O processo utiliza dois programas que já vêm com a instalação padrão do MySQL:
-   **`mysqldump`**: O utilitário para **EXPORTAR** o banco de dados e criar o arquivo de DUMP.
-   **`mysql`**: O cliente padrão do MySQL, que será usado para **IMPORTAR** os dados de um arquivo de DUMP.

---

### 3. Exportando um Banco de Dados (Gerando o DUMP)

Este comando lê um banco de dados existente e gera o arquivo `.sql` correspondente.

**Sintaxe Padrão:**
```bash
mysqldump -u [usuario] -p [nome_do_banco] > [arquivo_de_backup].sql
````

**Explicação dos Parâmetros:**

  - `-u [usuario]`: Especifica o nome de usuário (ex: `-u root`).
  - `-p`: Solicita a senha do usuário de forma segura. A senha será pedida após executar o comando.
  - `[nome_do_banco]`: O nome do banco de dados que você deseja salvar.
  - `>`: Operador de redirecionamento. Salva o resultado do comando no arquivo especificado à direita.
  - `[arquivo_de_backup].sql`: O nome do arquivo que será criado com a cópia de segurança.

**Exemplo Prático:**

```bash
mysqldump -u root -p cadastro2 > backup_cadastro.sql
```

-----

### 4\. Importando um Banco de Dados (Restaurando o DUMP)

Este comando lê um arquivo `.sql` e executa todos os comandos dentro dele em um banco de dados de destino.

**Pré-requisito:** O banco de dados de destino já deve existir. Se necessário, crie-o antes com `CREATE DATABASE nome_do_banco;`.

**Sintaxe Padrão:**

```bash
mysql -u [usuario] -p [nome_do_banco_destino] < [arquivo_de_backup].sql
```

**Explicação dos Parâmetros:**

  - `[nome_do_banco_destino]`: O nome do banco de dados (geralmente vazio) que receberá os dados do backup.
  - `<`: Operador de redirecionamento. Usa o conteúdo do arquivo à direita como entrada para o comando à esquerda.

**Exemplo Prático:**

```bash
mysql -u root -p cadastro2 < backup_cadastro.sql
```

-----

### Resumo Rápido

  - **Para Criar Backup:** `mysqldump -u root -p nome_banco > arquivo.sql`
  - **Para Restaurar Backup:** `mysql -u root -p nome_banco < arquivo.sql`
