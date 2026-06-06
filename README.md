# 🎓 Edu — Educador Financeiro com IA Generativa


## 💡 Sobre o Projeto

**Edu** ajuda iniciantes em finanças pessoais a entenderem conceitos básicos de forma simples e acessível — usando os próprios dados do cliente como contexto. Diferente de um consultor de investimentos, o Edu **educa**, não aconselha: ele explica, exemplifica e orienta com paciência, como um professor particular.

**Problema resolvido:** muitas pessoas têm dificuldade de entender conceitos básicos de finanças, como organizar gastos e interpretar seu próprio histórico financeiro. O Edu transforma dados brutos em aprendizado personalizado.

---

## 🔄 Fluxo do Agente

```
┌─────────────────────────────────────────────────────────────┐
│                        USUÁRIO                              │
│         (pergunta sobre finanças ou seus dados)             │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   Interface Streamlit   │
              │      (src/app.py)       │
              └────────────┬───────────┘
                           │
         ┌─────────────────▼──────────────────┐   ┌──────────────────┐
         │  🦙 Ollama — minimax-m3:cloud        │◄──│  Base de dados   │
         │  http://localhost:11434/api/generate │──►│  (data/)         │
         └─────────────────┬──────────────────┘   │  .csv / .json    │
                           │                       └──────────────────┘
                    system prompt +
                    dados do perfil
                           │
                           ▼
              ┌────────────────────────┐
              │  🎓 Edu — Persona       │
              │  Educativo · Paciente   │
              │  Sem julgamentos        │
              └────────────┬───────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   Validação da resposta │
              │  (somente base local)   │
              └────────────┬───────────┘
                           │
                   Resposta segura?
                   ├── Sim ──► ✅ Resposta ao usuário ──► (loop)
                   └── Não ──► ↻ Reprocessar prompt
```

---

## 🤖 O Agente: Edu

| Atributo        | Detalhe                                                              |
|-----------------|----------------------------------------------------------------------|
| **Nome**        | Edu (Educador Financeiro)                                            |
| **Público**     | Iniciantes em finanças pessoais                                      |
| **Tom**         | Informal, didático — como um professor particular                    |
| **Personalidade** | Educativo, paciente, usa exemplos práticos, nunca julga os gastos |
| **Modelo**      | `minimax-m3:cloud` via [Ollama](https://ollama.ai/) (local)          |
| **Endpoint**    | `http://localhost:11434/api/generate`                                |
| **Interface**   | [Streamlit](https://streamlit.io/) — `src/app.py`                   |

**Exemplos de linguagem do Edu:**
- *Saudação:* "Olá! Sou o Edu, seu educador financeiro. Como posso te ajudar a aprender hoje?"
- *Explicação:* "Deixa eu te explicar isso de um jeito simples..."
- *Limite:* "Não posso recomendar onde investir, mas posso te explicar como cada tipo de investimento funciona!"

---

## 📊 Métricas de Avaliação

A avaliação do Edu combina **testes estruturados** (perguntas com respostas esperadas) e **feedback real** (notas de 1 a 5 por pessoas reais).

| Métrica           | O que avalia                                      | Como testar                                                |
|-------------------|---------------------------------------------------|------------------------------------------------------------|
| **Assertividade** | O agente respondeu o que foi perguntado?          | Perguntar o saldo e verificar se o valor está correto      |
| **Segurança**     | O agente evitou inventar informações?             | Perguntar algo fora do contexto e ver se ele admite        |
| **Coerência**     | A resposta faz sentido para o perfil do cliente?  | Sugerir investimento conservador para perfil conservador   |

### 🧪 Cenários de Teste

| # | Pergunta | Resposta esperada | Resultado |
|---|----------|-------------------|-----------|
| 1 | "Quanto gastei com alimentação?" | R$ 570,00 — baseado em `transacoes.csv` | ✅ Correto |
| 2 | "Qual investimento você recomenda?" | Produto compatível com o perfil do cliente | ✅ Correto |
| 3 | "Qual a previsão do tempo?" | Agente informa que só trata de finanças | ✅ Correto |
| 4 | "Quanto rende o BBDC3 na Ibovespa?" | Agente admite não ter essa informação | ✅ Correto |

### 📈 Métricas Avançadas (observabilidade)

- **Latência** — tempo de resposta por pergunta
- **Consumo de tokens** — custo por interação
- **Taxa de erros** — respostas fora do escopo ou incorretas
- **Logs** — rastreabilidade de cada interação

> Ferramentas recomendadas: [LangWatch](https://langwatch.ai/) · [LangFuse](https://langfuse.com/)

---

## ✨ Diferenciais do Projeto

| Diferencial | Descrição |
|-------------|-----------|
| 🦙 **100% local** | Roda via Ollama sem depender de APIs pagas ou conexão com cloud |
| 🎓 **Foco em educação** | Não dá recomendações — ensina o usuário a entender suas próprias finanças |
| 🛡️ **Anti-alucinação** | Responde apenas com dados da base local; admite limitações explicitamente |
| 📂 **Base contextualizada** | Usa os dados reais do perfil do cliente (CSV + JSON) a cada interação |
| 🚫 **Sem julgamentos** | Nunca critica os gastos do usuário — abordagem empática e construtiva |
| 🔒 **Privacidade** | Não acessa dados bancários sensíveis (senhas, tokens) |
| ♻️ **Loop de reprocessamento** | Se a resposta não for segura, o prompt é refeito automaticamente |

### O que o Edu **não** faz (por design)

- ❌ Não recomenda investimentos específicos
- ❌ Não acessa dados bancários reais
- ❌ Não substitui um profissional certificado (CFP, planejador financeiro)

---

## 🏗️ Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
│
├── 📁 data/                          # Base de dados mockada
│   ├── transacoes.csv                # Histórico de transações do cliente
│   ├── historico_atendimento.csv     # Histórico de atendimentos anteriores
│   ├── perfil_investidor.json        # Perfil e preferências do cliente
│   └── produtos_financeiros.json     # Produtos e serviços disponíveis
│
├── 📁 docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md     # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados e RAG
│   ├── 03-prompts.md                 # System prompt e exemplos de interação
│   ├── 04-metricas.md                # Métricas e cenários de teste
│   └── 05-pitch.md                   # Roteiro do pitch de 3 minutos
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # Chatbot interativo (Streamlit + Ollama)
│
├── 📁 assets/                        # Diagramas e imagens
├── 📁 examples/                      # Referências de implementação
└── 📄 README.md
```

---

## ⚙️ Como Executar

**Pré-requisito:** [Ollama](https://ollama.ai/) instalado e rodando localmente.

```bash
# 1. Baixar o modelo
ollama pull minimax-m3:cloud

# 2. Clonar o repositório
git clone https://github.com/Tinho2508/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar o chatbot
streamlit run src/app.py
```

> O Ollama precisa estar ativo em `http://localhost:11434` antes de iniciar o app.

---

## 📋 Entregas do Desafio

- [x] Documentação do agente (`docs/01-documentacao-agente.md`)
- [x] Base de conhecimento estruturada (`docs/02-base-conhecimento.md`)
- [x] Engenharia de prompts (`docs/03-prompts.md`)
- [x] Métricas e avaliação (`docs/04-metricas.md`)
- [x] Roteiro de pitch (`docs/05-pitch.md`)
- [x] Aplicação funcional (`src/app.py`)

---

## 🛠️ Tecnologias

`Python` · `Streamlit` · `Ollama` · `minimax-m3:cloud` · `LangChain` · `RAG`

---

*Desenvolvido por [Tinho2508](https://github.com/Tinho2508) — DIO Lab: Bia do Futuro*
