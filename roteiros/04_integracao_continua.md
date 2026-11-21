# Integração contínua e pipeline

Tempo sugerido de 12 minutos, com o repositório já preparado antes da aula.

## Preparação anterior à aula

1. No GitHub, crie um repositório vazio para esta demonstração. Escolha uma visibilidade permitida pela sua instituição. Deixe sem README, licença e gitignore iniciais, pois os arquivos estão neste pacote.
2. Copie a URL HTTPS exibida pelo GitHub.
3. Abra a raiz deste projeto no VS Code e o terminal PowerShell.

```powershell
# Confere o Git instalado. --version pede o número da versão.
git --version

# Inicia um repositório novo na raiz do projeto. -b main define a branch inicial.
git init -b main

# Define o nome de autor somente neste repositório.
# config altera a configuração local. user.name é a chave e o texto é seu valor.
git config user.name "Oswaldo Borges Peres"

# Define um e-mail de demonstração para estes commits locais.
# user.email é a chave. O endereço de exemplo será registrado como autor.
git config user.email "professor@example.com"

# Prepara os arquivos do projeto. O ponto seleciona o diretório atual.
# .gitignore exclui saídas locais como dist e arquivos de cache.
git add .

# Registra a versão inicial. -m recebe a mensagem do commit.
git commit -m "Adiciona media e testes automatizados"

# Solicita a URL do repositório criado, evitando um endereço fictício no comando.
# Read-Host recebe o texto digitado e o armazena na variável urlRepositorio.
$urlRepositorio = Read-Host 'Cole a URL HTTPS do seu repositorio GitHub'

# Associa a URL ao nome origin. remote add registra o destino remoto.
git remote add origin $urlRepositorio

# Envia a main para origin. -u registra a associação entre a branch local e a remota.
git push -u origin main
```

Se o Git abrir o navegador para autenticação, entre com sua conta e conclua o procedimento. Após o envio, abra a aba Actions. O workflow Testes e artefato da media deve executar e aprovar os 7 testes.

A pasta .github deve estar na raiz do repositório, ao lado de media.py. Se você enviar somente uma pasta externa contendo o projeto, o GitHub não encontrará o workflow no local esperado. Use o envio por Git mostrado acima para incluir também a pasta iniciada por ponto.

O workflow utiliza runners hospedados pelo GitHub. A disponibilidade de Actions, as permissões para executar e a franquia de uso dependem da conta e do repositório. Se aparecer uma solicitação de autorização de Actions, revise e habilite o workflow na sua conta. Prepare e confirme essa primeira execução antes da aula.

## Demonstração com erro e correção

Primeiro, mostre .github/workflows/ci.yml. Explique push, pull_request, workflow_dispatch, jobs, steps e runs-on. A execução obtém o código, seleciona Python, roda pipeline.py e disponibiliza o artefato aprovado.

Abra media.py. Na função calcular_media, troque somente esta linha

```python
return (primeira + segunda) / 2
```

pela linha abaixo

```python
return primeira + segunda / 2
```

Salve o arquivo. Com a precedência dos operadores, 6 e 8 passam a produzir 10. O programa continua sendo sintaticamente válido, e os testes devem identificar o erro de comportamento.

```powershell
# Executa localmente o mesmo ponto de entrada usado no GitHub Actions.
# pipeline.py executa os testes e só constrói se eles passarem.
python .\pipeline.py
```

Espere PIPELINE REPROVADO. As 7 verificações devem resultar em 4 falhas. Há falhas de unidade, integração e no percurso funcional. A linha do teste compara 10 com 7. O teste de erro de entrada e outros casos podem continuar aprovados.

```powershell
# Prepara a alteração defeituosa para registrar a demonstração.
git add media.py

# Registra o defeito didático. -m define a mensagem.
git commit -m "Demonstra falha na regra de media"

# Envia o novo commit para a branch remota já associada.
git push
```

Abra Actions e a execução correspondente a esse commit. Mostre a etapa Testar e construir reprovada e a etapa de upload ignorada. Aguarde a execução terminar antes de enviar a correção para mostrar os dois resultados separadamente.

No VS Code, recoloque os parênteses na expressão original e salve.

```powershell
# Confere localmente a versão corrigida. O argumento é o script do pipeline.
python .\pipeline.py

# Prepara o arquivo corrigido.
git add media.py

# Registra a correção. -m define a mensagem.
git commit -m "Corrige precedencia no calculo da media"

# Envia a correção e dispara uma nova execução remota.
git push
```

Espere os 7 testes aprovados e a geração de dist/media_aprovada.zip. No GitHub, abra a nova execução e compare a mensagem do commit, o resultado dos testes e o artefato.

Integração contínua envolve integrar mudanças pequenas com frequência e responder ao feedback. O workflow automatiza as verificações. A execução local é uma demonstração de pipeline e preparação antes do envio ao repositório.

O pipeline pode deixar em dist um artefato de uma execução anterior. Uma execução reprovada não gera um novo artefato. No GitHub, cada execução tem seus próprios logs e artefatos associados.
