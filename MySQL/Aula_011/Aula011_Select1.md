# Aula 11: Consultando Dados com SELECT (Parte 1)
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. O Comando "SELECT"

O `SELECT` é o principal comando da **DQL (Data Query Language)**. Sua função é buscar e exibir dados armazenados em tabelas. Toda consulta de dados começa com `SELECT`.

**Sintaxe Básica:**

```sql
-- Seleciona TODAS as colunas da tabela
SELECT * FROM nome_da_Tabela;

-- Seleciona colunas específicas
SELECT coluna1, coluna2 FROM nome_da_tabela;
```
---

### 2. Ordenando os Resultados com `ORDER BY`

A cláusula `ORDER BY` é usada para classificar o resultado da consulta com base em uma ou mais colunas.
- `ASC` (Ascendente): Ordem padrão, do menos para o maior (A-Z, 0-9). Pode ser omitido.
- `DESC` (Descendente): Ordem inversa, do maior para o menor (Z-A, 9-0).

**Exemplos:**

```sql
-- Ordena os cursos por nome em ordem alfabética
SELECT * FROM cursos ORDER BY nome;

-- Ordena os cursos por nome em ordem alfabética inversa
SELECT * FROM cursos ORDER BY nome DESC;

-- Ordena primeiro pelo ano e, para anos iguais, ordena pelo nome
SELECT ano, nome, carga FROM cursos ORDER BY ano, nome;
```

---

### 3. Filtrando Resultados com `WHERE`

A cláusula `WHERE` é usada para extrair apenas os registros que satisfazem uma condição específica.

**Operadores de Comparação**

| Operador | Descrição | Exemplo |
| :--- | :--- | :--- |
| = | Igual a | WHERE ano = '2016' |
| > | Maior que | WHERE carga > 40 |
| < | Menor que | WHERE totaulas < 30 |
| >= | Maior ou igual a | WHERE ano >= '2015' |
| <= | Menor ou igual a | WHERE ano <= '2015' |
| != ou <>| Diferente de | WHERE ano != '2016' |

**Exemplo:**

```sql
SELECT nome, carga FROM cursos
WHERE ano = 2016
ORDER BY nome;
```

---

### 4. Operadores Lógicos e de Intervalo

Para criar filtros mais complexos, usamos operadores lógicos.

- `BETWEEN ... AND ...`: Seleciona valores dentro de um intervalo (inclusivo).

```sql
-- Seleciona cursos entre 2014 e 2016
SELECT * FROM cursos WHERE ano BETWEEN 2014 AND 2016;
```

- `IN (...)`: Seleciona valores que estão em uma lista específica.

```sql
-- Seleciona cursos que são de 2014 OU 2016
SELECT * FROM cursos WHERE ano IN (2014, 2016);
```

`AND`: Combina condições, onde ambas devem ser verdadeiras.

```sql
SELECT * FROM cursos WHERE carga > 35 AND totaulas < 30;
``` 

`OR`: Combina condições, onde pelo menos uma delas deve ser verdadeira.

```sql
SELECT * FROM cursos WHERE carga > 35 OR totaulas < 30;
```
