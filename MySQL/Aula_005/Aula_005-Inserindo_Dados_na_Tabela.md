Aula 05: Inserindo dados na tabela
# Aula 05: Inserindo Dados na Tabela (INSERT INTO)
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. O Comando `INSERT INTO`

O comando `INSERT INTO` pertence ao grupo DML (Data Manipulation Language) e sua função é adicionar novos registros (linhas) a uma tabela.

### 2. Sintaxe Recomendada

A forma mais segura e legível de usar o comando é especificando as colunas que receberão os valores.

**Sintaxe:**
```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, ...)
VALUES (valor1, valor2, ...);
```

- A ordem dos valores deve corresponder exatamente à ordem das colunas listadas.

- Omitir a chave primária id (que é AUTO_INCREMENT) fará com que o MySQL a preencha automaticamente.

### 3. Inserindo Múltiplos Registros de Uma Vez

Para otimizar o processo, é possível inserir várias linhas com um único comando INSERT INTO. Para isso, basta separar cada conjunto de valores entre parênteses por uma vírgula.

**Sintaxe:**
```sql
INSERT INTO nome_da_tabela (colunas)
VALUES
    (valores_linha1),
    (valores_linha2),
    (valores_linha3);
```

### 4. Usando a Palavra-Chave DEFAULT

Se uma coluna possui um valor padrão definido na sua criação (ex: DEFAULT 'Brasil'), você pode usar a palavra-chave DEFAULT na lista de VALUES para que o MySQL insira o valor padrão definido.

```sql
INSERT INTO pessoas (..., nacionalidade)
VALUES (..., DEFAULT);
-- Insere 'Brasil' na coluna nacionalidade.
```

### 5. Verificando a Inserção com SELECT *

Após inserir dados, o comando ```SELECT * FROM nome_da_tabela;``` é usado para visualizar todos os registros e colunas da tabela, permitindo verificar se a inserção ocorreu corretamente.

```sql
USE cadastro2;

INSERT INTO pessoas
(nome, nascimento, sexo, peso, altura, nacionalidade)
VALUES
('Ana', '1975-12-22', 'F', '52.3', '1.45', 'EUA'),
('Pedro', '2006-08-24', 'M', '87.5', '1.80', DEFAULT),
('Júlia', '1999-05-30', 'F', '75.9', '1.7', 'Portugal');

SELECT * FROM pessoas;
```
