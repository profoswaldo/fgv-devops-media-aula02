# Artefato aprovado e feedback

Tempo sugerido de 5 minutos. O código deve estar na versão corrigida. Execute na raiz.

```powershell
# Executa os testes e gera o ZIP somente após sua aprovação.
python .\pipeline.py

# Mostra os arquivos de saída. -LiteralPath indica a pasta e -Name mostra os nomes.
Get-ChildItem -LiteralPath '.\dist' -Name

# Monta uma pasta nova para conferir a extração.
# -Path define a base e -ChildPath inclui data e horário formatados por -Format.
$conferencia = Join-Path -Path '.\dist' -ChildPath ('conferencia_' + (Get-Date -Format 'yyyyMMdd_HHmmss_fff'))

# Extrai o pacote aprovado. -LiteralPath indica o ZIP e -DestinationPath o destino.
Expand-Archive -LiteralPath '.\dist\media_aprovada.zip' -DestinationPath $conferencia

# Guarda os caminhos do programa e do JSON que vieram no ZIP.
# -Path define a pasta e -ChildPath informa cada arquivo.
$programa = Join-Path -Path $conferencia -ChildPath 'media.py'
$notas = Join-Path -Path $conferencia -ChildPath 'notas.json'

# Executa a cópia extraída. --arquivo recebe o JSON com as duas notas.
python $programa --arquivo $notas

# Mostra a identificação da versão. -LiteralPath recebe o caminho montado.
# Join-Path une a pasta de conferência ao nome versao.json.
Get-Content -LiteralPath (Join-Path -Path $conferencia -ChildPath 'versao.json')
```

Resultado esperado, Média: 7. O pacote contém media.py, notas.json, COMO_EXECUTAR.txt e versao.json. O campo commit relaciona a construção ao commit local ou à revisão obtida pelo runner. Se o projeto ainda não possui um repositório, aparece execucao-local.

No GitHub, o upload-artifact disponibiliza media-aprovada na página da execução. O download pode acrescentar um ZIP externo que contém media_aprovada.zip. Extraia esse arquivo interno para executar o programa. O workflow mantém esse artefato por sete dias, conforme a configuração do pacote.

Relacione o commit, o teste que encontrou o defeito, o resultado final e o artefato da execução aprovada.
