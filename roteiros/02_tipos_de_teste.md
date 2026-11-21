# Unidade integração e funcional

Tempo sugerido de 8 minutos. Execute na raiz do projeto.

```powershell
# Executa os testes que chamam diretamente a função de cálculo.
# -m seleciona unittest. discover procura os testes em -s testes.
# -p escolhe test_unidade.py. -v detalha os resultados.
python -m unittest discover -s testes -p test_unidade.py -v
```

Esperado, 3 testes e OK. Os casos utilizam 6 e 8, duas notas iguais e duas notas zero.

```powershell
# Executa os testes que integram a leitura de um arquivo JSON ao cálculo.
# -m seleciona unittest. -s define a pasta, -p o arquivo e -v o detalhamento.
python -m unittest discover -s testes -p test_integracao.py -v
```

Esperado, 2 testes e OK. Um teste cria um JSON temporário com duas notas e verifica a média. Outro verifica que a ausência da segunda nota é identificada. A criação e a remoção do arquivo são feitas pelo próprio teste.

```powershell
# Executa testes que iniciam o programa inteiro, enviam entradas e examinam a saída.
# -m seleciona unittest. -s define a pasta, -p o arquivo e -v o detalhamento.
python -m unittest discover -s testes -p test_funcional.py -v
```

Esperado, 2 testes e OK. Um teste simula a digitação de 6 e 8 e verifica Média: 7. Outro envia abc e verifica a mensagem de erro e o código de saída 1.

```powershell
# Executa todos os testes do projeto.
# -m seleciona unittest. discover procura testes, -s informa a pasta e -v detalha a execução.
python -m unittest discover -s testes -v
```

Esperado, 7 testes e OK. Os testes de unidade concentram-se na regra de cálculo. Os de integração verificam componentes trabalhando juntos. Os funcionais exercitam o comportamento observável do programa de terminal.

Um teste aprovado mostra o atendimento aos casos verificados. Novos requisitos podem exigir novos casos.
