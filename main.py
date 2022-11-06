from telegram.ext import *
import requests as r
from bs4 import BeautifulSoup as bs
import time

print("bot started")
def start_track(input_text):
    url=str(input_text)
    page = r.get(url)
    full_content = bs(page.text,"html.parser")
    price=full_content.find("div",{"class":"_30jeq3"}).text
    item_name=full_content.find("span",{"class":"B_NuCI"}).text
    price=price[1:]
    price_3=price.split(",")
    price="".join(price_3)
    price=int(price)
    
def start_commamnd(update,context):
    update.message.reply_text("Welcome to Flipcart Price Tracking bot. Click on /track to Track Price drop of a Flipcart Product.")

def help_commamnd(update,context):
    update.message.reply_text("""Welcome to the help section (^._.^) For any further help on using this bot or For any bussiness aproches contact the developer in following id:
    @Lugell""")

def trackmessage(update,context):
    update.message.reply_text("Paste the Product Link to Start tracking.")
    
#after /track command (1)
def handle_input(update,context):
    url=str(update.message.text)

    page = r.get(url)
    full_content = bs(page.text,"html.parser")
    price=full_content.find("div",{"class":"_30jeq3"}).text
    global item_name
    item_name=full_content.find("span",{"class":"B_NuCI"}).text
    price=str(price)
    item_name=str(item_name)

    string = "The prodect is ",item_name," and the current price is  ",price," Take some rest. I have started to Track the price. Once it's drops i'll notify you :) "
    string=list(string)
    string="".join(string)
    update.message.reply_text(string)
    price=price[1:]
    price_3=price.split(",")
    price="".join(price_3)
    #drop tracker(2)
    b=int(price)
    while True:
        page = r.get(url)
        full_content = bs(page.text,"html.parser")
        price=full_content.find("div",{"class":"_30jeq3"}).text
        price=price[1:]
        price_3=price.split(",")
        price="".join(price_3)
        price=int(price)
        if price<b:
            differnce_amount=b-price
            diff_percent=(differnce_amount/b)*100
            diff_percent=round(diff_percent,2)
            diff_percent=str(diff_percent)
            differnce_amount=str(differnce_amount)
            price=str(price)
            strr = "Good news for you!!! Your ",item_name,"'s Price was dropped by ",diff_percent,"% now the price is Rs.",price," You can save Rs.",differnce_amount," by buying the item now !   to keep tracking this product click on /track ."
            strr= "".join(strr)
            update.message.reply_text(strr)
            break
        time.sleep(3600)

def error(update,context):
    print(f"update {update} caused error {context.error}")

def main():
    updater=Updater("5697999234:AAGMXlLWwo-nzrgr08OemvKemu0KxjOfqPA", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_commamnd))
    dp.add_handler(CommandHandler("help",help_commamnd))
    dp.add_handler(CommandHandler("track",trackmessage))
    dp.add_handler(MessageHandler(Filters.text ,handle_input))
    dp.add_error_handler(error)
    updater.start_polling(3)
    updater.idle()
main()

