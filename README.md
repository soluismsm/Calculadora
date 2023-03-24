# Calculadora

Calculadora simples, interface feita com **Tkinter**, possui os 4 operadores básicos:

- Divisão
- Multiplicação
- Subtração
- Soma

## Interface Gráfica

![Interface do APP](/docs/APP.png)

### Problemas Solucionados

#### 1 - Continuar Operação após a primeira conta ser feita

- Adicionei um novo valor no dicionário de valores chamado "repeat" que tem valor de True ou False, se alguma conta já foi feita o valor muda para True. E caso o usuário digitar algum valor ou mudar o operador o valor muda para False novamente.

**Dicionário:**
`values = {"num1": "0", "num2": "0", "operator": None, "repeat": False}`

#### 2 - Continuar a operação quando não informar nenhum valor novo

##### Solução

Verifiquei se o **operator is None**, caso seja faça as operações com os valores salvos

```python
    if operator is not None:
        if "/" in operator:
            result = num1 / num2
        elif "x" in operator:
            result = num1 * num2
        elif "-" in operator:
            result = num1 - num2
        else:
            result = num1 + num2
    else:
        result = num1
```

##### Exemplo

![Exemplo da operação](/docs/calculator.gif)

### TODO

Lista de Afazeres por ordem de prioridade:

1. Botão para deletar último número.
2. Mais operadores de porcentagem, potenciação, raiz quadrada.
3. Adicionar parenteses para operações mais complexas.
4. Valores na memória.
5. Interface Gráfica
6. ....
