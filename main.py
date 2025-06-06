import re
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT = """
Você é um atendente inteligente de WhatsApp para uma loja de eletrônicos. Seu trabalho é interpretar a intenção da mensagem do cliente e responder adequadamente.

Se o cliente estiver relatando um problema, erro ou precisando de suporte técnico, responda utilizando a seguinte estrutura JSON:

{
  "function_call": {
    "name": "sendFastMessage",
    "arguments": {
      "phone": "559999999999",
      "message": "Mensagem empática e orientada ao suporte aqui"
    }
  }
}

Se a mensagem do cliente for sobre interesse em produtos, perguntas comerciais, ou se ele for um novo cliente, apenas responda com uma frase amigável e informativa sobre promoções e produtos. Não retorne JSON neste caso.

Sempre seja educado, direto e eficiente.
"""

def sendFastMessage(phone, message):
    print(f"\n[ENVIANDO MENSAGEM - SIMULADO]\nPara: {phone}\nMensagem: {message}\n")

def main():
    user_message = input("\nDigite a mensagem do cliente: ")

    response = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "prompt": PROMPT + f"\nCliente: {user_message}\n",
        "stream": False
    })

    data = response.json()
    raw_output = data.get("response", "")
    print("\n[RESPOSTA DO MODELO]\n", raw_output)

    try:
        match = re.search(r"\{.*\}", raw_output, re.DOTALL)
        if match:
            json_data = json.loads(match.group())
            args = json_data.get("function_call", {}).get("arguments", {})
            if args:
                sendFastMessage(**args)
            else:
                print("\nNenhuma função encontrada na resposta.")
        else:
            print("\nResposta comum sem função estruturada.")
    except Exception as e:
        print("\nErro ao interpretar JSON:", e)

if __name__ == "__main__":
    main()