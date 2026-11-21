# Resultado esperado e teste automatizado

Tempo sugerido de 4 minutos. Terminal na raiz do projeto.

```powershell
# Executa a aplicação interativa. media.py identifica o programa.
python .\media.py
```

Quando aparecer Primeira nota, digite 6 e pressione Enter. Quando aparecer Segunda nota, digite 8 e pressione Enter. O resultado é Média: 7.

Abra media.py e mostre a função calcular_media. O resultado soma as duas notas e divide o total por dois. Os parênteses garantem que a soma acontece antes da divisão.

```powershell
# Executa apenas o teste que compara a média de 6 e 8 com o valor 7.
# -m executa unittest. discover procura arquivos de teste.
# -s informa a pasta. -p escolhe o arquivo. -k filtra pelo nome do teste.
# -v apresenta cada resultado detalhadamente.
python -m unittest discover -s testes -p test_unidade.py -k media_de_6_e_8 -v
```

Resultado esperado, Ran 1 test e OK. Leia test_media_de_6_e_8 em testes/test_unidade.py. assertEqual compara o resultado obtido com o valor esperado. A expectativa agora pode ser repetida automaticamente.
