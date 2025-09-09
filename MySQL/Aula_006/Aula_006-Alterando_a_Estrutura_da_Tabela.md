# Aula 06: Alterando Estruturas com ALTER TABLE e DROP TABLE
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. Introdução a Comandos DDL de Alteração

Enquanto `CREATE` é usado para criar novas estruturas, os comandos `ALTER TABLE` e `DROP TABLE` são usados para modificar ou excluir estruturas de tabelas já existentes. Eles também fazem parte da **DDL (Data Definition Language)**.

### 2. Comando Auxiliar: `DESCRIBE`

Para visualizar a estrutura atual de uma tabela antes de modificá-la, usamos o comando `DESCRIBE`.

**Sintaxe:**
```sql
DESCRIBE nome_da_tabela;
-- ou a forma curta
DESC nome_da_tabela;
```

### 3. Modificando a Tabela com ALTER TABLE
O comando `ALTER TABLE` é um comando versátil que possui diversas cláusulas para realizar diferentes tipos de modificações.

```sql
-- Renomeando a Tabela
ALTER TABLE nome_antigo RENAME TO nome_novo;

-- Adicionando uma Coluna

--- Adiciona a coluna no final da tabela
ALTER TABLE pessoas ADD COLUMN profissao VARCHAR(20);

--- Adiciona a coluna em uma posição específica (depois de 'nome')
ALTER TABLE pessoas ADD COLUMN profissao VARCHAR(20) AFTER nome;

--- Adiciona a coluna como a primeira da tabela
ALTER TABLE cursos ADD idcurso INT FIRST;

-- Removendo uma Coluna

ALTER TABLE pessoas DROP COLUMN profissao;
```

#### Modificando o Tipo e as Constraints de uma Coluna
Usa-se `MODIFY COLUMN` quando você quer alterar as propriedades da coluna, mas manter o mesmo nome.

```sql
ALTER TABLE pessoas MODIFY COLUMN profissao VARCHAR(25) DEFAULT '';
```

#### Renomeando e Modificando uma Coluna
Usa-se `CHANGE COLUMN` quando você quer renomear a coluna. Você obrigatoriamente precisa informar o nome antigo, o nome novo e as novas definições.

```sql
ALTER TABLE pessoas CHANGE COLUMN profissao prof VARCHAR(20);
```

#### Adicionando Chave Primária
É possível adicionar uma chave primária a uma tabela que foi criada sem uma.

```sql
ALTER TABLE cursos ADD PRIMARY KEY(idcurso);
```

### 4. Excluindo uma Tabela com DROP TABLE
Este comando remove permanentemente uma tabela, incluindo sua estrutura e todos os dados contidos nela.

```sql
DROP TABLE IF EXISTS nome_da_tabela;
```

### 5. Novas Constraints e Modificadores
- **UNIQUE:** Uma constraint que garante que todos os valores em uma coluna sejam únicos (não repetidos). Diferente da PRIMARY KEY, uma tabela pode ter várias colunas com UNIQUE.
- **UNSIGNED:** Um modificador para tipos numéricos inteiros. Ele impede que a coluna aceite valores negativos e, com isso, dobra a capacidade de armazenamento para números positivos. Ideal para campos como carga horária e totaulas, que nunca seriam negativos.