# Aula 2 de DevOps

Um projeto novo para explicar testes automatizados, integração contínua e preparação da entrega em 40 minutos.
A aplicação calcula a média de duas notas. Digitar 6 e 8 deve produzir Média: 7.

## Abrir e preparar

1. Extraia o ZIP para uma pasta de sua preferência.
2. No VS Code, use Arquivo e Abrir Pasta e selecione FGV_DevOps_Aula2_Exemplos_Do_Zero. Nessa raiz devem aparecer media.py, pipeline.py, testes, infra, roteiros e .github.
3. Abra Terminal e Novo Terminal e selecione PowerShell. Todos os comandos dos roteiros partem dessa raiz.
4. Confira o Python instalado. Os exemplos utilizam a biblioteca padrão do Python 3.10 ou superior.

```powershell
# Mostra a versão do Python. --version solicita o número da versão.
python --version

# Guarda o caminho atual da raiz na variável pastaAula.
# Get-Location consulta o diretório e Path seleciona seu endereço.
$pastaAula = (Get-Location).Path

# Lista os itens da raiz. -Force inclui a pasta .github se estiver oculta.
# -Name mostra os nomes, sem a tabela de metadados.
Get-ChildItem -Force -Name
```

Para a parte local, o Python é suficiente. O uso do GitHub Actions exige Git, uma conta GitHub, acesso à internet e um repositório autorizado. Prepare esse repositório antes da aula seguindo roteiros/04_integracao_continua.md. Os tempos abaixo consideram essa preparação concluída.

## Sequência

| Minutos | Roteiro | Demonstração |
| --- | --- | --- |
| 0 a 4 | 01_resultado_esperado.md | Digitar duas notas e conferir automaticamente a média |
| 4 a 12 | 02_tipos_de_teste.md | Executar testes de unidade, integração e funcionais |
| 12 a 16 | 03_quadrantes.md | Classificar exemplos e discutir observação humana |
| 16 a 28 | 04_integracao_continua.md | Enviar alteração com defeito, observar a falha e corrigir |
| 28 a 33 | 05_artefato.md | Examinar e executar o ZIP aprovado |
| 33 a 37 | 06_entrega_e_implantacao.md | Comparar aprovação manual e publicação automática locais |
| 37 a 40 | 07_infraestrutura_como_codigo.md | Aplicar uma definição de ambiente local |

Os testes e o pipeline local foram executados durante a preparação do pacote. O workflow deve ser enviado ao seu repositório para executar no GitHub. As demonstrações de entrega e ambiente utilizam pastas locais e mostram os conceitos com código pequeno.

O programa aceita duas notas numéricas e calcula a média aritmética. O intervalo de 0 a 10 pode ser discutido como um requisito adicional. Uma entrada que não representa um número produz mensagem de erro e código de saída 1.

Leia os comentários antes de cada comando. Digite somente a linha de execução se preferir. As linhas com # também podem ser coladas no PowerShell.
