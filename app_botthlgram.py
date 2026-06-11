import telebot
import base
import app_api


bot  = telebot.TeleBot(base.TOKEN)

print('bot created')

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id,  text='به بات آموزشی خوش آمدید')


@bot.message_handler(commands=['help', 'contact'])
def support(message):
    bot.reply_to(message,'در صورت نیاز به پشتیبانی با آیدی @help در تماس باشید')


@bot.message_handler(commands=['news'])
def get_news(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn1 = telebot.types.InlineKeyboardButton(text='اخبار ورزشی', url='https://varzesh3.com')
    btn2 = telebot.types.InlineKeyboardButton(text='اخبار عمومی', url='https://entekhab.ir')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='یکی از گزینه زیر را انتخاب کنید', reply_markup=markup)


@bot.message_handler(commands=['movie'])
def get_movie_info(message):
    msg = bot.send_message(message.chat.id, text= 'name of movie?')
    bot.register_next_step_handler(msg, get_movie_info_by_name)


def get_movie_info_by_name(message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    title = result[0]
    year = result[1]
    country = result[2]
    imdb_rate = result[3]
    info =f'title: {title}, year: {year}, country: {country}, imdb_rate: {imdb_rate}'
    bot.send_message(message.chat.id, text=info)

    




@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton(text='تماس با ما')
    btn2 = telebot.types.KeyboardButton(text='درباره ما')
    btn3 = telebot.types.KeyboardButton(text='بازگشت')
    markup.add(btn1, btn2 , btn3)
    bot.send_message(message.chat.id, text='یکی از گزینه زیر را انتخاب کنید', reply_markup=markup)
 
@bot.message_handler(func=lambda message: True)
def answer_to_all(message):
    if message.text == 'تماس با ما':
        mobile = '09167419245'
        email = 'hotoke591@gmail.com'
        info = f'mobail: {mobaile} , email: {email}'
        bot.send_message(message.chat.id, text=info)

    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, 'ما یک گروه اموزشی هستیم')
    
    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardMarkup()
        bot.send_message(message.chat.id, 'بازگشت', reply_markup=markup)




if __name__ == '__main__':
    bot.infinity_polling()