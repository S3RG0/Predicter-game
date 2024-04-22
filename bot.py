from  telebot import types
import telebot
import main
from dotenv import load_dotenv
import os
import schedule time

load_dotenv()

bot = telebot.TeleBot(os.getenv("Bot_Token"))

fortune_teller = main.FortuneTeller()

# Словарь для отслеживания количества запросов от каждого пользователя

user_requests = {}

# Функция для обнуления счетчика user_requests
def reset_user_requests():
    global user_requests
    user_requests = {}

# Планирование выполнения функции reset_user_requests() каждый день в полночь
schedule.every().day.at("00:00").do(reset_user_requests)

# Цикл для выполнения планированных задач
while True:
    schedule.run_pending()
    time.sleep(1)

# Список пользователей с неограниченными предсказаниями (администраторы)
admins = [290375421]

keyboard = types.ReplyKeyboardMarkup(row_width=1)
button = types.KeyboardButton("Получить предсказание")
keyboard.add(button)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = telebot.types.KeyboardButton("Получить предсказание")
    markup.add(item)
    bot.send_message(message.chat.id, "Приветствую, странник. Постучись, и врата предсказаний откроются. Но помни, лишь три вопроса в день мудрецу дозволено.", reply_markup=markup)

# Обработчик кнопки "Получить предсказание"
@bot.message_handler(func=lambda message: message.text == "Получить предсказание")
def get_prediction(message):
    user_id = message.chat.id
    # Проверяем, является ли пользователь администратором
    if user_id in admins:
        prediction = fortune_teller.get_fortune()
    else:
        # Проверяем, сколько запросов уже было сделано пользователем
        if user_id in user_requests:
            if user_requests[user_id] >= 3:
                bot.send_message(message.chat.id, "Прости, мой друг, но три предсказания в день - исходя из моей мудрости, дозволено.")
                return
            else:
                user_requests[user_id] += 1
        else:
            user_requests[user_id] = 1
        prediction = fortune_teller.get_fortune()
    bot.send_message(message.chat.id, prediction)
    
# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Напишите /start, чтобы начать.")

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
