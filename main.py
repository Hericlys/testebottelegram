import telebot


CHAVE_API = "6247775328:AAGoX0LPEdjhRaT6CQOTDBkBSXOtfjpWLmA"

bot = telebot.TeleBot(CHAVE_API)


def verificar_mensagem_padrao(mensagem):
    return True


@bot.message_handler(commands=['start'])
def mensagem_start(mensagem):
    nome = mensagem.from_user.first_name
    msg = f"""
    olá {nome} sejá bem vindo ao bot do hericlys.
    selecione um dos comandos para começamos:
    /nos - descubra mais sobre a gente.
    /planos - descubra o melhor plano para você
    
    basta clicar em um comando.
    """
    bot.send_message(mensagem.chat.id, msg)

@bot.message_handler(func=verificar_mensagem_padrao)
def mensagem_padrao(mensagem):
    msg = """
Ops! Não conseguir entender sua mensagem.
mas não se preocupe aqui esta uma lista de comandos que pode ajudar:
/start - para iniciar a aplicação
/comandos - para obter a lista completa de comandos
    """
    print(mensagem)
    bot.reply_to(mensagem, msg)


bot.polling()
