# Validador de CPF em Python

Este projeto é um script em Python que verifica se um CPF fornecido pelo usuário está no formato correto e se os dígitos verificadores são válidos.

## 📌 Funcionalidades

- **Verificação do formato**: O CPF deve estar no formato `XXX.XXX.XXX-XX`.
- **Remoção de caracteres especiais**: O código remove os pontos (`.`) e o hífen (`-`) para validar apenas os números.
- **Cálculo dos dígitos verificadores**: O script aplica o algoritmo de validação do CPF para verificar se os dois últimos dígitos são válidos.
- **Mensagens de erro**: O programa informa ao usuário se o CPF está incorreto ou inválido.

## 🚀 Como executar

1. Certifique-se de ter o Python instalado (versão 3.x recomendada).
2. Salve o código em um arquivo Python, por exemplo: `validador_cpf.py`.
3. Execute o script com o seguinte comando:
   ```bash
   python validador_cpf.py
   ```
4. Insira um CPF no formato correto quando solicitado.

## 📜 Algoritmo de Validação

O CPF é validado seguindo as etapas:

1. **Verificação do formato**: O CPF deve conter 14 caracteres e seguir o padrão `XXX.XXX.XXX-XX`.
2. **Remoção de símbolos**: Os caracteres `.` e `-` são removidos.
3. **Cálculo do primeiro dígito verificador**:
   - Multiplica-se os 9 primeiros números por pesos decrescentes de 10 a 2.
   - Soma-se os produtos e multiplica-se por 10.
   - O resultado é dividido por 11; se o resto for maior que 9, o primeiro dígito verificador é `0`, caso contrário, é o próprio resto.
4. **Cálculo do segundo dígito verificador**:
   - Multiplica-se os 10 primeiros números (incluindo o primeiro dígito verificador) por pesos decrescentes de 11 a 2.
   - Segue-se o mesmo procedimento do primeiro dígito para obter o segundo.
5. **Comparação com o CPF inserido**: Se os dois dígitos calculados coincidirem com os do CPF informado, ele é considerado válido.

## 🔍 Exemplo de Uso

Entrada:

```
Digite seu CPF: 123.456.789-09
```

Saída:

```
O primeiro dígito do seu CPF é 0
O segundo dígito é 9
CPF válido
```

## ⚠️ Observação

Este código apenas verifica a validade estrutural do CPF. Ele não consulta bases de dados oficiais para verificar se um CPF está registrado ou pertence a uma pessoa real.

## 📌 Tecnologias Utilizadas

- Linguagem: **Python**
- Biblioteca: `input()`, `str.replace()`, `isdigit()`, `for`, `if-else`

## 📜 Licença

Este projeto é de código aberto e pode ser usado para fins educacionais ou pessoais. Caso utilize este código, considere dar os devidos créditos. 😊

