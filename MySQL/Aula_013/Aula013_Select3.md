# Aula 13: Agrupando Resultados

### 1. Agrupando Registros com `GROUP BY`

A cláusula `GROUP BY` é usada para agrupar linhas que têm os mesmos valores em uma ou mais colunas, transformando-as em um único registro de resumo.
Seu principal objetivo é ser usada em conjunto com as funções de agregação (`COUNT`, `MAX`, `AVG`, `SUM`, `MIN`) para que a função seja aplicada a cada grupo individualmente, em vez de à tabela inteira.

**Sintaxe Básica:**

```sql
SELECT coluna_agrupadora, FUNCAO_AGG(outra_coluna)
FROM nome_da_tabela
GROUP BY coluna_agrupadora;
```

**Exemplo Prático:**

```sql
-- Conta quantos cursos existem para cada carga horária diferente
SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga;
```

---

### 2. Diferença entre `DISTINCT` e `GROUP BY`

Apesar de às vezes parecerem produzir resultados similares, seus propósitos são fundamentalmente diferentes:

- `DISTINCT`: Apenas seleciona e exibe os valores únicos de uma coluna, eliminando repetições. Ele responde à pergunta *"Quais valores diferentes existem?"*.
    ```sql
    -- Retorna uma lista simples: 30, 40, 20, 8...
    SELECT DISTINCT carga FROM cursos;
    ```
- `GROUP BY`: Cria "agrupamentos" ou "caixas" para cada valor único, permitindo que você realize cálculos sobre o que há dentro de cada grupo. Ele responde à pergunta: *O que podemos dizer sobre cada um desses valores diferentes?*.
    ```sql
    -- Retorna uma análise: carga 30 tem 5 cursos, carga 40 tem 8 cursos...
    SELECT carga, COUNT(*) FROM cursos GROUP BY carga;
    ```

---

### 3. Filtrando Grupos com `HAVING`

Enquanto a cláusula `WHERE` filtra as linhas **antes** de serem agrupadas, a cláusula `HAVING` é usada para filtrar os grupos **depois** que as funções de agregação foram aplicadas.

**A Regra de Ouro**
- Use `WHERE` para filtrar dados brutos da tabela (colunas normais).
- Use `HAVING` para filtrar o resultado de uma função de agregação.

**Sintaxe:**

```sql
SELECT coluna_agrupadora, FUNCAO_AGG(outra_coluna)
FROM nome_da_tabela
GROUP BY coluna_agrupadora
HAVING CONDICAO_SOBRE_A_FUNCAO_AGG;
```

**Exemplo Prático:**

```sql
-- Mostra apenas as cargas horárias que têm mais de 3 cursos
SELECT carga, COUNT(nome) FROM cursos
GROUP BY carga
HAVING COUNT(nome) > 3;
```

---

### 4. Subqueries: O Superpoder do `HAVING`

Usando o exemplo visto na aula: `HAVING carga > (SELECT AVG(carga) FROM cursos)`, podemos ver o poder do SQL.
Isto é chamado de **subquery** (uma consulta dentro de outra). O que o MySQL faz:

1. Primeiro, ele resolve a consulta de dentro. Ele calcula a média de carga de todos os cursos e guarda esse número (Supomos 35.5).
2. Depois, ele substitui na consulta principal: A cláusula `HAVING` se torna `HAVING carga > 35.5`.

Assim ele responde a uma pergunta de negócio mais complexa: *"Depois de agrupar os cursos por carga horária, me mostre apenas os grupos cuja carga está acima da média geral da plataforma"*.
