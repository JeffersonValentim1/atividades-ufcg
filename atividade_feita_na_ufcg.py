"""
descrição
"""

def mensagem(remetente, destinatario):
    msg  = f"---" + "\n"
    msg += f"Olá {destinatario},\n" + "\n"
    msg += f"Este é um exemplo simples de mala direta.\n" + "\n"
    msg += f"Abraços,\n\n{remetente}."
    return msg
def main():
    remetente = input("Remetente? ")
    destinatario = input("Destinatário? ")
    msg = mensagem(remetente, destinatario)
    print(msg)
main()
