# Passo a Passo de Execução



## setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo livre
ollama pull minimax-m3:cloud
# 3. Testar se funciona
ollama run minimax-m3 "Olá"
```



## Código Completo

Todo omcódigo-fonte esta no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run app.py
```
## Evidências de Execução

<img width="628" height="976" alt="image" src="https://github.com/user-attachments/assets/cab8794c-c869-490d-b974-2b9fc0ce3d48" />
