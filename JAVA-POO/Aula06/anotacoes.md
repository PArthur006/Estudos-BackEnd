# 📘 Aula 06 – Teoria: Encapsulamento

## 🧠 Conceito
- **Encapsulamento** é um dos pilares da **Programação Orientada a Objetos** (POO).
- Tem como principal objetivo **proteger os dados** de uma classe, controlando como eles podem ser acessados ou modificados.
- Na prática, isso significa **declarar os atributos como privados (`private`)** e expô-los ao mundo externo por meio de **métodos públicos** (getters e setters).

---

## 🔐 Modificadores de Acesso

| Modificador | Descrição |
|-------------|-----------|
| `public`    | Acesso liberado para qualquer classe |
| `private`   | Acesso permitido **apenas dentro da própria classe** |
| `protected` | Acesso permitido dentro da classe, subclasses e mesmo pacote |

---

## 🛠️ Prática do Encapsulamento

- Atributos da classe devem ser privados:
```java
private String nome;
private int idade;
```

- Devem ser criados métodos públicos para acessar e modificar esses atributos:
```java
public String getNome() {
    return this.nome;
}

public void setNome(String nome) {
    this.nome = nome;
}
```

---

## ✅ Vantagens do Encapsulamento

- Garante a **integridade dos dados**
- Permite **regras de validação** nos setters
- Melhora a **manutenibilidade** e **legibilidade** do código
- Facilita o uso de bibliotecas e frameworks que dependem do padrão **JavaBeans**

---

## 📌 Convenção JavaBeans

- Padrão seguido para encapsulamento:
  - Atributos privados
  - Métodos `getAtributo()` e `setAtributo()`
  - Para `boolean`, usa-se `isAtributo()` em vez de `get`

---

## 🧪 Exemplo simples

```java
public class Pessoa {
    private String nome;
    private int idade;

    public String getNome() {
        return nome;
    }

    public void setNome(String n) {
        this.nome = n;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int i) {
        if (i >= 0) {
            this.idade = i;
        }
    }
}
```

