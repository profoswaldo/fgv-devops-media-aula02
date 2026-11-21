# Quadrantes de testes

Tempo sugerido de 4 minutos. A classificação considera o propósito do teste.

| Perspectiva | Apoiam o desenvolvimento | Avaliam o produto |
| --- | --- | --- |
| Negócio | Q2, exemplos de aceitação como notas 6 e 8 produzirem média 7 | Q3, exploração e clareza das mensagens para o aluno |
| Tecnologia | Q1, verificações pequenas da função e da integração técnica | Q4, desempenho e comportamento sob carga |

Q1 é usualmente representado no canto inferior esquerdo, Q2 no superior esquerdo, Q3 no superior direito e Q4 no inferior direito.

1. Mostre a expectativa de média 7. Como exemplo de aceitação compreensível pelo usuário, ela pode orientar Q2. Sua implementação em uma função de teste de unidade também fornece suporte técnico em Q1. O objetivo ajuda a escolher a classificação.
2. Peça a alguém para observar a mensagem Primeira nota. Ela explica se aceita vírgula decimal? O programa aceita, mas a facilidade de descobrir isso pode ser discutida em uma avaliação de usabilidade, associada a Q3.
3. Pergunte como avaliar muitas solicitações simultâneas em uma aplicação web. Essa preocupação conduz à discussão de desempenho, em Q4. Este programa de terminal permite discutir o conceito, e a verificação de carga exigiria um cenário apropriado.
4. Explique que há automação possível em diferentes quadrantes e que a exploração humana complementa os testes executáveis.

Os quadrantes organizam perspectivas e objetivos. Eles não definem uma ordem obrigatória de execução.
