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

## Executando o projeto

### 1. Inicie o servidor Ollama em um terminal separado

```bash
ollama serve
```

Esse comando inicia o servidor local da API do Ollama para que o projeto possa se comunicar com o modelo LLaMA 3 localmente.

---

### 2. Execute o script do projeto

Em outro terminal, dentro da pasta do projeto:

```bash
node seu-script.js
```

> Substitua `seu-script.js` pelo nome do arquivo principal do seu projeto.

---

## Exemplo de mensagens e respostas

> Imagem exemplo 1: Mensagem do usuário  
> ![Exemplo mensagem usuário](./path/to/user-message.png)

> Imagem exemplo 2: Resposta do modelo  
> ![Exemplo resposta modelo](./path/to/model-response.png)

---

## Funcionalidades

- Utiliza LLaMA 3 via Ollama API local  
- Simula um assistente inteligente estilo WhatsApp  
- Suporte a chamadas de função via JSON  
- Lógica condicional para respostas dinâmicas  
- Teste rápido de engenharia de prompt e automação local sem precisar de API da OpenAI

---

## Observações

- Certifique-se de que o servidor Ollama está rodando antes de executar o script, para evitar erros de conexão.  
- Requer que o modelo LLaMA 3 esteja disponível localmente via Ollama (ou outro modelo configurado).  

---

## Referências

- [Ollama Documentation](https://ollama.com/docs)  
- [LLaMA Models](https://ai.facebook.com/blog/large-language-model-llama-meta-ai)  

---

Se tiver dúvidas ou quiser contribuir, fique à vontade para abrir issues ou pull requests!
