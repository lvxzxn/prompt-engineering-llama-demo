# prompt-engineering-llama-demo

Demo do LLaMA 3 usando a API do Ollama para execução local de prompts.  
Simula um assistente inteligente tipo WhatsApp com chamadas de função baseadas em JSON e lógica condicional.  
Útil para testar engenharia de prompt, respostas `function_call` e automação local com LLMs, sem depender da API da OpenAI.

---

## Requisitos

- [Ollama](https://ollama.com) instalado localmente (compatível com macOS, Windows e Linux)

---

## Instalação do Ollama

1. Acesse o site oficial e baixe o instalador para seu sistema operacional:  
   [https://ollama.com/download](https://ollama.com/download)

2. Siga as instruções de instalação específicas para seu SO.

3. Verifique a instalação executando no terminal:  
   ```bash
   ollama --version
   ```
   Deve mostrar a versão instalada do Ollama.

---

# Executando o projeto

### 1. Inicie o servidor Ollama em um terminal separado

No terminal, rode:  
ollama serve

Esse comando inicia o servidor local da API do Ollama para que o projeto possa se comunicar com o modelo LLaMA 3 localmente.

---

### 2. Execute o script do projeto

Em outro terminal, dentro da pasta do projeto, rode:  
`python main.py` ou simplesmente `main.py`

> Substitua `main.py` pelo nome do arquivo principal do seu projeto.

---

## Exemplo de mensagens e respostas

> Imagem exemplo 1: Mensagem do usuário  
![image](https://github.com/user-attachments/assets/47726176-8544-4b77-8d4f-28dfa1cb17ee)

> Imagem exemplo 2: Resposta do modelo  
![image](https://github.com/user-attachments/assets/67faa181-4fbe-4ab2-a8d3-574c72519749)

---

## Funcionalidades

- Utiliza LLaMA 3 via Ollama API local  
- Simula um assistente inteligente estilo WhatsApp  
- Suporte a chamadas de função via JSON  
- Teste rápido de engenharia de prompt e automação local sem precisar de API da OpenAI


## Referências

- [Ollama Documentation](https://ollama.com/docs)  

---
