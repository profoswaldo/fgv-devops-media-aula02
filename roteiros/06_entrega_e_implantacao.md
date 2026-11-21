# Aprovação manual e publicação automática

Tempo sugerido de 4 minutos. Estas demonstrações publicam em pastas locais. O processo executa testes, constrói e extrai o pacote aprovado. A verificação final executa a versão extraída com notas.json.

```powershell
# Simula a entrega pronta para publicação com uma decisão manual.
# demonstrar_entrega.py é o script. manual seleciona a aprovação digitada.
python .\demonstrar_entrega.py manual
```

Após os testes aprovados, aparece Artefato pronto. Digite PUBLICAR para aprovar.
Primeiro pressione Enter sem digitar. O resultado indica que a entrega está preparada e aguarda uma decisão. A pasta publicacoes/manual ainda não é criada nesta primeira execução.

Execute o mesmo comando novamente. Quando a pergunta aparecer, digite PUBLICAR e pressione Enter. A aplicação é extraída em publicacoes/manual/versao_ seguida de um identificador e executa com resultado Média: 7.

```powershell
# Simula publicação automática após a aprovação dos testes.
# automatico seleciona o fluxo que avança diretamente para a extração e conferência.
python .\demonstrar_entrega.py automatico
```

Resultado esperado, testes aprovados, criação do ZIP, publicação em publicacoes/automatico/versao_ seguida de um identificador e Média: 7. Nesta execução, a aprovação decorre das verificações definidas e o script avança sem solicitar uma decisão humana.

Na entrega contínua, as mudanças aprovadas ficam prontas para liberação. Na implantação contínua, as mudanças que atendem às verificações seguem automaticamente para produção. Aqui, a pasta local representa o destino de publicação da simulação. Em um ambiente real, esse destino pode ser um servidor ou serviço de hospedagem.

O workflow incluído em .github/workflows realiza CI e disponibiliza um artefato. As duas políticas de publicação são demonstradas por este script local, de modo que você pode compará-las sem configurar um provedor de hospedagem.
