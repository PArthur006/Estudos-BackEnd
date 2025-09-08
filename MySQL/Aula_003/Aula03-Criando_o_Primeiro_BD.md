# Aula 03: Criação de Banco de Dados e Tipos Primitivos
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. Hierarquia da Informação e DDL

Antes de criar, é fundamental entender a estrutura:
1.  **Banco de Dados (Database):** O contêiner principal. É um espaço isolado que agrupa tabelas relacionadas.
2.  **Tabelas (Tables):** Estruturas de armazenamento de dados, compostas por colunas (campos) e linhas (registros).
3.  **Registros (Records/Rows):** Cada linha individual de dados dentro de uma tabela.

**DDL (Data Definition Language):** É o subconjunto de comandos SQL usado para **definir** e **modificar** a estrutura do banco de dados e suas tabelas. Os comandos principais desta aula são `CREATE DATABASE` e `CREATE TABLE`.

---

### 2. Comandos Essenciais de Criação

#### A. Criando um Banco de Dados

O comando `CREATE DATABASE` inicia um novo esquema.

**Sintaxe básica:**
```sql
CREATE DATABASE nome_do_banco;
````

**Boa prática:** Usar `IF NOT EXISTS` para evitar erros caso o banco de dados já exista.

```sql
CREATE DATABASE IF NOT EXISTS cadastro;
```

#### B. Selecionando o Banco de Dados

Depois de criar um banco de dados, você precisa "entrar" nele para poder criar tabelas:

```sql
USE cadastro;
```

#### C. Criando Tabelas

O comando `CREATE TABLE` define as colunas e os tipos de dados de cada coluna.

**Sintaxe básica:**

```sql
CREATE TABLE IF NOT EXISTS nome_da_tabela (
    nome_coluna1 tipo_dado constraints,
    nome_coluna2 tipo_dado constraints,
    nome_coluna3 tipo_dado constraints,
    PRIMARY KEY (coluna_chave)
);
```

**Exemplo Prático:**

```sql
CREATE TABLE IF NOT EXISTS clientes (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    peso DECIMAL(5, 2),
    PRIMARY KEY (id)
);
```

-----

### 3\. Tipos Primitivos de Dados no MySQL

Escolher o tipo correto é crucial para a **performance** (quanto espaço ocupa) e **integridade** (que tipo de dado é permitido) do banco.

#### A. Tipos Numéricos

Usados para armazenar números (idades, quantidades, preços, etc.).

**1. Inteiros:** Usados para números sem casas decimais. A principal diferença é o espaço de armazenamento e o intervalo de valores.

| Tipo | Armazenamento | Intervalo (Signed) | Intervalo (Unsigned) | Uso Comum |
| :--- | :--- | :--- | :--- | :--- |
| **TINYINT** | 1 byte | -128 a 127 | 0 a 255 | Idade, flags booleanas (0 ou 1) |
| **SMALLINT**| 2 bytes | -32.768 a 32.767 | 0 a 65.535 | Quantidades pequenas |
| **MEDIUMINT**| 3 bytes | -8.388.608 a 8.388.607 | 0 a 16.777.215 | Contadores médios |
| **INT** | 4 bytes | -2,1 bilhões a 2,1 bilhões | 0 a 4,2 bilhões | Chaves primárias (IDs), contadores grandes |
| **BIGINT** | 8 bytes | Muito grande | Muito grande | IDs em tabelas gigantescas (big data) |

  * **Signed vs. Unsigned:** `Signed` (padrão) permite números negativos. `Unsigned` não permite negativos, dobrando o limite positivo. Use `UNSIGNED` para IDs e quantidades que nunca serão negativas.

**2. Ponto Fixo e Flutuante:** Usados para números com casas decimais.

  * **DECIMAL(p, s) / NUMERIC(p, s):** Tipo de ponto fixo. Armazena o valor exato. Essencial para valores monetários e cálculos precisos.
      * `p` = precisão total (número total de dígitos, antes e depois da vírgula).
      * `s` = escala (número de dígitos *depois* da vírgula).
      * *Exemplo:* `DECIMAL(10, 2)` armazena até 10 dígitos no total, com 2 deles sendo decimais (ex: 12345678.99).
  * **FLOAT e DOUBLE:** Tipos de ponto flutuante. Armazenam valores aproximados. São mais rápidos para cálculos científicos complexos, mas podem ter problemas de arredondamento. Evite para dinheiro.

#### B. Tipos de String (Texto)

Usados para armazenar nomes, descrições, endereços, etc.

  * **CHAR(n):** Comprimento **fixo**. Sempre ocupa `n` caracteres de espaço, mesmo que o dado inserido seja menor (completa com espaços).
      * *Uso:* Ideal para dados que sempre têm o mesmo tamanho (ex: Sigla de Estado 'UF' com `CHAR(2)`, CEP `CHAR(8)`).
  * **VARCHAR(n):** Comprimento **variável**. Ocupa apenas o espaço necessário para os dados inseridos + 1 ou 2 bytes para armazenar o comprimento.
      * `n` é o tamanho *máximo* permitido.
      * *Uso:* Tipo mais comum para textos como nomes, e-mails, títulos. Muito mais eficiente que CHAR para dados de tamanho variável.
  * **TEXT:** Para textos longos. Não é necessário definir um tamanho máximo fixo como no VARCHAR.
      * Subdivisões: `TINYTEXT` (\~255 caracteres), `TEXT` (\~65 mil caracteres), `MEDIUMTEXT` (\~16 milhões), `LONGTEXT` (\~4 bilhões).
      * *Uso:* Postagens de blog, descrições detalhadas de produtos, comentários de usuários.

#### C. Tipos de Data e Hora

  * **DATE:** Armazena apenas a data. Formato padrão: `YYYY-MM-DD`.
      * *Uso:* Data de nascimento, data de emissão de nota fiscal.
  * **TIME:** Armazena apenas o horário. Formato padrão: `HH:MM:SS`.
      * *Uso:* Horário de funcionamento, hora de um evento.
  * **DATETIME:** Armazena a data e a hora combinadas. Formato: `YYYY-MM-DD HH:MM:SS`.
      * *Uso:* Data e hora exata de um cadastro, agendamento.
  * **TIMESTAMP:** Similar ao `DATETIME`, mas tem um intervalo menor (1970 a 2038). Sua principal característica é a capacidade de ser **atualizado automaticamente** para o horário atual sempre que a linha for modificada (útil para campos como `ultima_modificacao`).

#### D. Outros Tipos

  * **ENUM (Enumeração):** Define uma lista pré-determinada de valores permitidos para uma coluna.
      * *Exemplo:* `ENUM('ativo', 'inativo', 'pendente')`. Garante que apenas esses valores possam ser inseridos.
  * **BOOLEAN / BOOL:** Não existe de fato no MySQL. Ao criar um tipo `BOOLEAN`, o MySQL o converte internamente para `TINYINT(1)`. O valor `0` é falso e `1` é verdadeiro.
