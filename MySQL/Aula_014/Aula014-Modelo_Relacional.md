# Aula 14: Modelo Relacional

### 1. Conceitos Fundamentais

- **Modelo Relacional:** é um modelo teŕoico para a organizaçãode dados em bancos de dados. A ideia central é que todos os dados são armazenados em tabelas (chamdas relações), que são compostas por linhas (tuplas) e colunas (atributos). A "cola" que une essas tabelas são as chaves.
- **Diagrama Entidade-Relacionamento (DER ou ERD): É a representação visual desse modelo. Pense nele como a planta baixa do seu banco de dados. Ele mostra as entidades, seus atributos e como elas se relacionam, antes mesmo de você escrever a primeira linha de `CREATE TABLE`.

### 2. Componentes do DER

- **Entidade:** é qualquer objeto do mundo real sobre o qual queremos armazenar informações. No diagraa, é representada por um **retângulo**.
    - Exemplos: `Aluno`, `Curso`, `Professor`, `Pedido`.
- **Atributo:** é uma característica ou propriedade de uma entidade. São as colunas da nossa futura tabela.
    - Exemplos: Para a entidade `Aluno`, os atributos seriam `nome`, `matrícula`, `data_nascimento`.

### 3. Chaves (As "Identidades")

- **Chave Primária (Primary Key - PK):** É o atributo (ou conjunto de atributos) que identifica de forma única cada registro em uma tabela. Uma PK não pode ser nula e não pode se repetir. É o "CPF" do registro.
- **Chave Estrangeira (Foreign Key - FK):** É um atributo em uma tabela que faz referência à Chave Primária de outra tabela. É o campo que efetivamente cria o link ou a ponte entre duas tabelas.

### 4. Relacionamento e Cardinalidade

A cardinalidade descreve a quantidade de instâncias de uma entidade que podem se relacionar com as instâncias de outra entidade.

- **Relacionamento Um-para-Um (1-1):** Uma ocorrência da Entidade A se relaciona com, no máximo, uma ocorrência na Entidade B, e vice-versa.
    - Um `Motorista` se relaciona com uma única `CarteiraDeMotorista`.
- **Relacionamento Um-para-Muitos (1-N):** Uma ocorrrência na Entidade A pode se relacionar com várias ocorrências na Entidade B, mas uma ocorrência em B só pode se relacionar com uma em A. (Este é o tipo mais comum).
    - Um `Cliente` pode ter muitos `Pedidos`. Cada `Pedido` pertence a um único `Cliente`.
- **Relacionamento Muitos-para-Muitos (N-N):** Várias ocorrências na Entidade A podem se relacionar com várias ocorrências na Entidade B.
    - Um `Aluno`pode estar matriculado em muitos `Cursos`, e um `Curso` pode ter muitos `Alunos`.
    - Esse tipo de relacionamento **não pode** ser criado diretamente. Ele precisa ser "quebrado" e, dpos relacionamentos 1-N através de uma terceira tabela, chamada de **tabela associativa** ou **tabela de junção**.
