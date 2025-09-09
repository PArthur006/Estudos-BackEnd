# Aula 04: Melhorando a Estrutura do Banco de Dados
**Fonte:** Curso de MySQL - Curso em Vídeo

---

### 1. Definições no Nível do Banco de Dados

Ao criar um banco de dados, podemos especificar padrões de caracteres para garantir a compatibilidade com acentuação e símbolos.

-   **`DEFAULT CHARACTER SET utf8`**
    -   **O que faz:** Define `UTF-8` como o conjunto de caracteres padrão para o banco de dados.
    -   **Por que usar:** O `UTF-8` é o padrão da web e suporta praticamente todos os caracteres e símbolos existentes, incluindo acentos (`ã`, `é`) e `ç`. É a escolha ideal para sistemas em português ou com suporte a múltiplos idiomas.

-   **`DEFAULT COLLATE utf8_general_ci`**
    -   **O que faz:** Define as regras de ordenação e comparação de texto.
    -   **Por que usar:** A terminação `_ci` significa **Case-Insensitive**. Isso faz com que, em buscas e ordenações, o banco de dados trate letras maiúsculas e minúsculas como iguais (ex: 'Maria' é igual a 'maria').

---

### 2. Constraints: As Regras das Colunas

Constraints são regras aplicadas às colunas para garantir a integridade, validade e consistência dos dados.

-   **`PRIMARY KEY` (Chave Primária)**
    -   **O que faz:** Transforma uma coluna no identificador único de cada registro (linha) da tabela.
    -   **Regras:** Uma Chave Primária não pode conter valores nulos (`NULL`) nem valores duplicados. É a "identidade" de um registro.

-   **`AUTO_INCREMENT`**
    -   **O que faz:** Usado geralmente na chave primária, faz com que o MySQL preencha o valor da coluna automaticamente, incrementando o último número inserido (1, 2, 3, ...).
    -   **Por que usar:** Automatiza a criação de IDs únicos, evitando que você precise controlar a numeração manualmente.

-   **`NOT NULL` (Não Nulo)**
    -   **O que faz:** É uma constraint que obriga o preenchimento da coluna. A coluna não poderá ter valores vazios (nulos).
    -   **Por que usar:** Garante que dados essenciais, como o nome de um cliente, nunca fiquem em branco.

-   **`DEFAULT` (Valor Padrão)**
    -   **O que faz:** Define um valor padrão para uma coluna. Se, ao inserir um novo registro, nenhum valor for especificado para essa coluna, o valor `DEFAULT` será usado.
    -   **Exemplo:** `nacionalidade VARCHAR(20) DEFAULT 'Brasil'`.

-   **`ENUM` (Enumeração)**
    -   **O que faz:** Cria uma lista de valores permitidos para uma coluna. Apenas os valores definidos na lista `ENUM` poderão ser inseridos.
    -   **Por que usar:** Garante a consistência dos dados, evitando erros de digitação ou valores inválidos. Ex: `sexo ENUM('M', 'F')` só aceitará 'M' ou 'F'.

---
