# Definição de ambiente em código

Tempo sugerido de 3 minutos. Abra infra/ambiente.json e mostre a lista entrada, saida e logs. A definição descreve o estado pretendido de um pequeno ambiente local.

```powershell
# Aplica a definição do ambiente. O argumento aponta para o script de provisionamento.
python .\infra\provisionar.py

# Exibe as pastas criadas. -LiteralPath define a pasta base e -Name mostra os nomes.
Get-ChildItem -LiteralPath '.\ambiente_local' -Name

# Reaplica a mesma definição para observar as pastas mantidas.
python .\infra\provisionar.py
```

Na primeira execução, as três pastas aparecem como Criada. Na segunda, aparecem como Mantida. O script não precisa duplicar os diretórios para atender à mesma definição.

Edite infra/ambiente.json e acrescente temporarios como um quarto item da lista. Salve e execute novamente o comando de provisionamento. O ambiente recebe a pasta nova.

O JSON expressa a configuração desejada, e o script aplica essa configuração ao sistema de arquivos. Essa miniatura executável ilustra definição versionada e aplicação repetível. Ferramentas de infraestrutura como código também administram recursos como máquinas, redes e serviços. Este exercício atua somente em pastas locais e acrescenta os diretórios declarados, sem realizar a remoção de itens que saiam da lista.

```powershell
# Mostra a alteração na definição do ambiente.
# --no-pager mantém a saída no terminal. diff compara o arquivo modificado.
# -- encerra as opções e o caminho seleciona a definição.
git --no-pager diff -- infra/ambiente.json
```

O último comando pressupõe o repositório criado no roteiro 4. Relacione a alteração ao processo de revisão. O exemplo permite discutir infraestrutura como código sem instalar ferramentas adicionais na aula.
