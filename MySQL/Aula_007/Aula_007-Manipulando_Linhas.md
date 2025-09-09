# Aula 07: Manipulação de Linhas com UPDATE, DELETE e TRUNCATE

**Fonte:** Curso de MySQL - Curso em Vídeo

-----

### 1\. Modificando Linhas com UPDATE

O comando `UPDATE` é utilizado para alterar os dados de registros que já existem em uma tabela. Ele faz parte da **DML (Data Manipulation Language)**.

A cláusula `WHERE` é fundamental para a segurança da operação, pois especifica **quais linhas** serão modificadas. Sem ela, **todas as linhas da tabela serão alteradas**. O `LIMIT` pode ser usado como uma camada extra de segurança.

**Sintaxe Básica:**

```sql
UPDATE nome_da_tabela
SET coluna1 = 'novo_valor1', coluna2 = 'novo_valor2'
WHERE condicao
LIMIT numero_de_linhas;
```

**Exemplos de Código:**

```sql
-- Alterando um único campo de uma linha específica
UPDATE cursos
SET nome = 'HTML5'
WHERE idcurso = '1';

-- Alterando múltiplos campos de uma linha
UPDATE cursos
SET nome = 'PHP', ano = '2015'
WHERE idcurso = '4';

-- Usando LIMIT como segurança para afetar apenas uma linha
UPDATE cursos
SET nome = 'Java', ano = '2015', carga = '40'
WHERE idcurso = '5'
LIMIT 1;
```

### 2\. Removendo Linhas com DELETE

O comando `DELETE` é utilizado para remover registros (linhas) de uma tabela. Assim como o `UPDATE`, a cláusula `WHERE` é crucial para evitar a remoção acidental de todos os dados.

**Sintaxe Básica:**

```sql
DELETE FROM nome_da_tabela
WHERE condicao;
```

**Exemplos de Código:**

```sql
-- Apagando uma linha específica
DELETE FROM cursos
WHERE idcurso = '8';

-- Apagando um número limitado de linhas que atendem a uma condição
DELETE FROM cursos
WHERE ano = '2050'
LIMIT 2;
```

### 3\. Limpando a Tabela com TRUNCATE TABLE

O comando `TRUNCATE` remove **todas as linhas** de uma tabela. Embora o resultado seja parecido com um `DELETE` sem `WHERE`, a operação é fundamentalmente diferente e muito mais eficiente.

**Sintaxe:**

```sql
TRUNCATE TABLE nome_da_tabela;
```

#### Diferenças entre DELETE e TRUNCATE

  - **Velocidade:** `TRUNCATE` é mais rápido pois não registra a remoção de cada linha individualmente (é uma operação DDL, não DML).
  - **Cláusula `WHERE`:** `TRUNCATE` não aceita `WHERE`. A operação sempre limpa a tabela inteira.
  - **Auto-Incremento:** `TRUNCATE` reinicia os contadores de `AUTO_INCREMENT` da tabela, enquanto `DELETE` não.