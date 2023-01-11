import telebot

CHAVE_API = "5898273580:AAF9nnZvRyFQ_w-phghc5T01Di35g3xeKd0"

bot = telebot.TeleBot(CHAVE_API) 

#Opções da escolha da opção de fazer um pedido

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa: Tempo de espera 20min")
@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o hamburguer para sua casa: Tempo de espera 20min")
@bot.message_handler(commands=["salada"])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a salada para sua casa: Tempo de espera 20min")


#Menu de Opções Iniciais

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você deseja? (Clique em uma opção)
        /pizza Pizza
        /hamburguer Hamburguer
        /salada Salada
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, mande um e-mail para reclamação@abacaxi123.com")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Valeu!! Wallas mandou um abraço de volta")


#Menu Inicial 

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma oção para continuar (Clique no item):
        
        /opcao1 Fazer Pedido
        /opcao2 Reclamar de um pedido
        /opcao3 Mandar um abraço para o Wallas

    Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(mensagem, "Olá!! O que deseja")

bot.polling()