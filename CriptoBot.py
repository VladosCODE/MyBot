import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
bot = telebot.TeleBot('1568111312:AAFDLr5-uhe-xdNJDKCk0CM64FOY55bROFA')
DRIVER = 'D:\chromeDriver\chromedriver'
driver = webdriver.Chrome(DRIVER)
@bot.message_handler(commands=['start'])
def start(message):
    #Кнопки для бота
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width=2)
    btn1 = types.KeyboardButton("bitcoin")
    btn2 = types.KeyboardButton("ethreum")
    btn3 = types.KeyboardButton("xrp")
    btn4 = types.KeyboardButton("cardano")
    markup.add(btn1,btn2,btn3,btn4)
    send_mess = f"<b>Здравствуйте {message.from_user.first_name}</b>\nНазвание криптавалюты"
    bot.send_message(message.chat.id, send_mess,parse_mode = 'html',reply_markup=markup)
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "bitcoin":
        Bitcoin = 'https://ru.investing.com/indices/investing.com-btc-usd'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        full_page = requests.get(Bitcoin,headers = header)
        soup = BeautifulSoup(full_page.content,'html.parser')
        convert = soup.findAll("span",{"class": "arial_26 inlineblock pid-1057391-last","id":"last_last"})
        final_message = f"1 Bitcoin = {convert[0].text} $."
        driver.get('https://www.binance.com/ru/trade/BTC_BUSD')
        element = driver.save_screenshot("bitcoin.png")
        bot.send_photo(message.chat.id,open('bitcoin.png','rb'))
    elif get_message_bot == "ethreum":
        Ethreum = 'https://ru.investing.com/crypto/ethereum/eth-usd?cid=997650'
        header_1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        full_page_1 = requests.get(Ethreum, headers=header_1)
        soup_1 = BeautifulSoup(full_page_1.content, 'html.parser')
        convert_1 = soup_1.findAll("span", {"class": "arial_26 inlineblock pid-997650-last","id":"last_last"})
        final_message = f"1 Ethreum = {convert_1[0].text} $"
        driver.get('https://www.binance.com/ru/trade/ETH_BUSD')
        element = driver.save_screenshot("ethreum.png")
        bot.send_photo(message.chat.id, open('ethreum.png', 'rb'))
    elif get_message_bot == "xrp":
        XRP = 'https://ru.investing.com/crypto/xrp/xrp-usd'
        header_2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        full_page_2 = requests.get(XRP, headers=header_2)
        soup_2 = BeautifulSoup(full_page_2.content, 'html.parser')
        convert_2 = soup_2.findAll("span", {"class": "arial_26 inlineblock pid-1118146-last","id":"last_last"})
        final_message = f"1 XRP = {convert_2[0].text} $"
        driver.get('https://www.binance.com/ru/trade/XRP_BUSD?layout=pro')
        element = driver.save_screenshot("xrp.png")
        bot.send_photo(message.chat.id, open('xrp.png', 'rb'))
    elif get_message_bot == "cardano":
        Cardano = 'https://ru.investing.com/crypto/cardano/ada-usd'
        header_3 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        full_page_3 = requests.get(Cardano, headers=header_3)
        soup_3 = BeautifulSoup(full_page_3.content, 'html.parser')
        convert_3 = soup_3.findAll("span", {"class": "arial_26 inlineblock pid-1073899-last","id":"last_last"})
        final_message = f"1 Cardano = {convert_3[0].text} $"
        driver.get('https://www.binance.com/ru/trade/ADA_BUSD?layout=pro')
        element = driver.save_screenshot("cardano.png")
        bot.send_photo(message.chat.id, open('cardano.png', 'rb'))
    else:
        final_message = f"<u>Курс данной криптовалюты отсутствует в боте</u>"
    bot.send_message(message.chat.id,final_message,parse_mode="html")
bot.polling(none_stop=True)