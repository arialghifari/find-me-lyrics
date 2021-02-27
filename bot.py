import telebot
from scrape import lyrics

token = ""; #insert your token inside ""
bot = telebot.TeleBot(token=token, threaded=False)

@bot.message_handler(commands=["start"])
def welcome(message):
  name = message.from_user.first_name
  messages = f"Hello {name}, welcome..\nfor finding lyrics you can type, for example : \n'/lyrics hello'"
  bot.send_message(message.chat.id, messages)

@bot.message_handler(commands=["help"])
def help(message):
  messages = "for finding lyrics you can type, for example : \n'/lyrics hello'"
  bot.reply_to(message, messages)

@bot.message_handler(commands=["lyrics"])
def lirik(message):
  textReplace = message.text.replace("/lyrics", "")
  result = lyrics(textReplace)

  if result is None:
    messages = "Sorry We Cannot Find The Lyrics, Try Another Song Title"
  else:
    replace = result[0].replace("/", "by")
    messages = f"Song Title : \n<b><i>{replace}</i></b>\n\nLyrics :\n{result[1]}"
    
  bot.reply_to(message, messages,parse_mode="HTML")

print("Running..")
bot.polling()