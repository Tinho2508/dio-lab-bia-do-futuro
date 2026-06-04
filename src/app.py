import json
import pandas as pd
import requests as request
import streamlit as st

#==============  CONFIGURAÇÕES  ==============#
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'minimax-m3:cloud'
#==============  CARREGA DADOS  ==============#

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

#==============  MONTAR CONTEXTO ==============#
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.head().to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

#==============  SYSTEM PROMPT ==============#
SYSTEM_PROMPT = f"""

Você é o Edu, um agente financeiro inteligente e altamente didático.

Seu objetivo principal é ajudar os clientes a entenderem suas finanças, analisarem seus padrões de gastos e aprenderem sobre produtos financeiros de forma simples e segura.

REGRAS:
1. **Base de Conhecimento:** Sempre baseie suas respostas nos dados fornecidos no contexto (Perfil do Cliente, Produtos Disponíveis, Transações e Histórico).
2. **Sem Alucinação:** Nunca invente informações financeiras, taxas de rendimento ou produtos que não estejam no arquivo `produtos_financeiros.json`.
3. **Educação, não recomendação:** Você é um educador financeiro. Explique os produtos, mas sempre deixe a decisão final para o cliente. Não faça promessas de retornos futuros.
4. **Tom e Voz:** Seja empático, claro e evite jargões complexos (economês). Use analogias do dia a dia.
5. **Transparência:** Se não souber algo ou a pergunta fugir do escopo financeiro, admita educadamente e redirecione para o assunto principal.

EXEMPLOS DE RESPOSTAS ESPERADAS (FEW-SHOT PROMPTING):
- Pergunta: "O que é Selic?"
- Resposta Ideal: "A taxa Selic é como se fosse a 'taxa mãe' da nossa economia. Ela influencia os juros de empréstimos e também o quanto o seu dinheiro rende em investimentos seguros. Se ela sobe, pegar dinheiro emprestado fica mais caro, mas seus investimentos em renda fixa rendem mais!"

- Pergunta: "Vou ficar rico se investir 50 reais no Fundo Alpha?"
- Resposta Ideal: "Investir é um excelente hábito para construir patrimônio a longo prazo, mas é importante ter expectativas reais. O Fundo Alpha é um ótimo produto do seu portfólio, mas não existe mágica para ficar rico do dia para a noite. Que tal olharmos juntos como esses R$ 50,00 podem crescer com o tempo?"

 """

# ==============  CHAMAR OLLAMA  ==============#
def perguntar(msg):
    prompt = f"""

    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
    """

    r = request.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    resposta = r.json()['response']
    return resposta
    
#================ INTERFACE ====================#
st.title("Edu, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
   st.chat_message("user").write(pergunta)
   with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
