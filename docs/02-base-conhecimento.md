# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e conhecer o histórico do cliente. |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e guiar as necessidades de aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Mapear os produtos disponíveis para que possam ser recomendados e explicados de forma didática. |
| `transacoes.csv` | CSV | Analisar o padrão de gastos do cliente e usar essas informações como exemplos práticos. |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não houve alteração ou expansão dos dados originais fornecidos na pasta `02-base-conhecimento.md`.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados podem ser integrados de duas maneiras principais:
1. **Estática:** Através da injeção manual das informações diretamente no prompt (copiando o conteúdo estruturado dos arquivos e colando no chat).
2. **Dinâmica (via Código):** Os arquivos CSV e JSON são lidos por um script de backend, que extrai as informações em formato de texto e as injeta automaticamente no contexto do agente antes de enviar a requisição para a LLM.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são divididos de forma estratégica na estrutura do prompt para garantir respostas mais precisas:
- **System Prompt (Contexto Base):** Recebe os dados de regras de negócio e limites de atuação, como o `produtos_financeiros.json` (o que o agente pode oferecer) e o `perfil_investidor.json` (para calibrar o tom de voz e o nível técnico da explicação).
- **User Prompt (Contexto Dinâmico):** Dados temporais e situacionais, como `transacoes.csv` e `historico_atendimento.csv`, são injetados junto à mensagem do usuário. Isso permite que o agente analise gastos recentes e resgate o contexto de interações passadas para formular uma resposta altamente personalizada.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
 text
Você é o Edu, um assistente financeiro didático. Use os dados abaixo para guiar seu atendimento:

[PERFIL DO CLIENTE - JSON]
- Nome: João Silva
- Perfil de Investidor: Moderado (Explique conceitos de renda variável com cautela)
- Necessidade de aprendizado: Entender como proteger o patrimônio da inflação.
- Saldo disponível: R$ 5.000,00

[PRODUTOS FINANCEIROS DISPONÍVEIS - JSON]
- CDB Liquidez Diária: Rende 100% do CDI, ideal para reserva de emergência.
- Fundo Multimercado Alpha: Risco Moderado, aplicação mínima de R$ 1.000,00.

[ÚLTIMAS TRANSAÇÕES - CSV]
- 01/11: Supermercado - R$ 450,00
- 03/11: Assinatura Streaming - R$ 55,00
- 05/11: Fast Food - R$ 120,00

[HISTÓRICO DE ATENDIMENTO - CSV]
- 15/10: Cliente perguntou sobre a diferença entre CDB e Poupança. Edu explicou de forma simplificada usando a analogia de "emprestar dinheiro para o banco".

Pergunta atual do usuário: "O que eu poderia fazer com os R$ 1.200,00 que sobraram na conta este mês sem correr muito risco?"
```
