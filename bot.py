import telebot
from telebot import types


bot = telebot.TeleBot('894084233:AAG7DVV-WvuyYscef-pRAs4hw9XtGxtrbGw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Hello', 'Goodbye')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello you wrote me /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello My Master')
    elif message.text.lower() == 'goodbye':
        bot.send_message(message.chat.id, 'Goodbye My Master')
    elif message.text.lower() == 'i love you' or '❤':
        bot.send_sticker(message.chat.id, 'CAADAgADGQMAAsSraAvz7mBcPaa0DAI')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write hello")
    else:
        bot.send_message(message.from_user.id, "I don't andertand you. Pleace write /help.")

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message (message.from_user_id, "What is ur name?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Write /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'What is your surname?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'How is old are u?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except:
            bot.send_message(message.from_user.id, 'Digit`s pleace')
    bot.send_message(message.from_user.id, 'Are U '+str(age)+' years old, and ur name is '+name+' '+surname+'?')

#keyboard = types.InlineKeyboardMarkup() #наша клавиатура
 #   key_yes = types.InlineKeyboardButton(text='YES', callback_data='yes') #кнопка «Да»
  #  keyboard.add(key_yes) #добавляем кнопку в клавиатуру
   # key_no= types.InlineKeyboardButton(text='NO', callback_data='no')
    #keyboard.add(key_no)
    #question = 'Are U ' + str(age) + ' years old, and ur name is '+ name +' ' + surname + '?'
#bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

#@bot.callback_query_handler(func=lambda call: True)
#def callback_worker(call):
    #if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
   #     .... #код сохранения данных, или их обработки
  #      bot.send_message(call.message.chat.id, 'Запомню : )')
 #   elif call.data == "no":
#         ... #переспрашиваем

bot.polling(none_stop=True, interval=0)



