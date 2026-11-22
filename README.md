# Scripts de TI

Exercícios e scripts em Python que estou desenvolvendo para praticar programação, automação e análise de logs, como preparação para trabalhar com administração de sistemas e redes.

## Como executar

Os scripts foram feitos para Python 3 e testados no Ubuntu (WSL):

```bash
python3 nome_do_script.py
```

## Básico de Python

| Script | O que faz |
|---|---|
| `ola.py` | Primeiro script, imprime "Olá, mundo!". |
| `par_impar.py` | Lê um número e informa se ele é par ou ímpar. |
| `tabuada.py` | Mostra a tabuada de um número até um limite escolhido pelo usuário. |
| `lista.py` | Calcula a soma e a média de uma lista de números. |
| `max_min.py` | Encontra o maior e o menor valor de uma lista. |
| `fizzbuzz.py` | Imprime "Fizz", "Buzz" ou "FizzBuzz" conforme os múltiplos de 3 e 5. |

## Textos, listas e dicionários

| Script | O que faz |
|---|---|
| `conta_palavra.py` | Conta quantas vezes cada palavra aparece em uma frase. |
| `contador_vogais.py` | Conta as vogais de uma frase. |
| `inverter_texto.py` | Inverte uma palavra. |
| `letra_inicial.py` | Filtra uma lista de nomes e devolve os que começam com "A". |
| `replicadas.py` | Remove valores repetidos de uma lista. |

## Arquivos e logs

| Script | O que faz |
|---|---|
| `ler_log.py` | Lê um arquivo de log e imprime as linhas. |
| `contar_erros.py` | Conta quantas linhas de um log têm o nível `ERROR`. |
| `analisar_log.py` | Conta as linhas por nível (INFO, WARNING, ERROR), ignora linhas mal formatadas, trata arquivo inexistente e grava um relatório em arquivo. |
| `sistema.log` | Arquivo de log de exemplo usado nos testes. |

## Automação de arquivos

| Script | O que faz |
|---|---|
| `explorar.py` | Lista o conteúdo de uma pasta mostrando nome, extensão e tipo de cada item. |
| `organizar.py` | Organiza os arquivos de uma pasta em subpastas por extensão. Aceita o caminho como argumento e a opção `--simular`. |

## Próximos passos

- Scripts de teste de rede (`socket`, `subprocess`)
- Shell script para backup e automação
- Noções de Docker