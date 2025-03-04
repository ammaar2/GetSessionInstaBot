#Code Write : @jokerpython3
import requests
import time
import telebot
from telebot.types import InlineKeyboardButton as btn
from telebot.types import InlineKeyboardMarkup as mk
from user_agent import generate_user_agent as gen
class S1:
    def __init__(self, user, pas):

        self.ses = None
        self.tr = None
        self.id = None
        self.mid = None
        self.ig = None

        self.kse = requests.Session()  
        response = self.kse.get('https://www.instagram.com/api/graphql') 
        crf = response.cookies.get('csrftoken')
        tim = str(time.time()).split('.')[1]
        headers = {
            'user-agent': str(gen()),
            'x-csrftoken': crf,
        }
        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{pas}',
            'username': user,
        }
        response = self.kse.post(
            'https://www.instagram.com/api/v1/web/accounts/login/ajax/', 
            headers=headers, 
            data=data
        )
        t = self.kse.cookies.get_dict()
        try:
   
   
            self.ses = t['sessionid']
            self.tr = t['csrftoken']
            self.id = t['ds_user_id']
            self.mid = t['mid']
            self.ig = t['ig_did']
        except Exception as e:

            pass

    def __str__(self):
        return str({
            'ses': self.ses,
            'crfton': self.tr,
            'id': self.id,
            'mid': self.mid,
            'ig_did': self.ig
        })

    def __getitem__(self, key):
        mapping = {
            'ses': self.ses,
            'crfton': self.tr,
            'id': self.id,
            'mid': self.mid,
            'ig_did': self.ig
        }
        return mapping[key]

tok = "7229675132:AAHDvs6KnAvNEQf10lEw9e9-O64L9k7objg"
bot = telebot.TeleBot(tok)
print('روح للبوت ودز /start')

def main_keyboard():
    keyboard = mk(row_width=1)
    dev_button = btn("Dev", url="https://t.me/jokerpython3")#لاتخمط
    start_button = btn("Start", callback_data="st")
    keyboard.add(dev_button, start_button)
    return keyboard

@bot.message_handler(commands=['start'])
def start_message(mes):
    keyboard = main_keyboard()
    bot.send_message(
        mes.chat.id, 
        text="ه ه هذا بوت استخراج سيشن ايدي حساب انسته وحبشتكنات مثل mid  وقيرها ", 
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "st")
def start_handler(call):
    bot.answer_callback_query(call.id)
    back_button = btn("رجوع", callback_data="Back")
    keyboard = mk(row_width=1)
    keyboard.add(back_button)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="هيج دز يوزر:باسورد",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: call.data == "Back")
def back_handler(call):
    bot.answer_callback_query(call.id)
    keyboard = main_keyboard()
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="ه ه هذا بوت استخراج سيشن ايدي حساب انسته وحبشتكنات مثل mid  وقيرها ",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: ":" in m.text)
def credential_handler(m):
    try:
        user, pas = m.text.split(":", 1)
    except ValueError:
        bot.send_message(m.chat.id, 'وين فاصله')
        return

    oq = S1(user, pas)
    print(oq)
    try:
        if oq.ses is None:
            bot.send_message(m.chat.id, 'يوزر وباسورد خطا')
            return
    except AttributeError:
        bot.send_message(m.chat.id, 'يوزر وباسورد خطا')
        return

    so = oq["ses"]
    crf = oq["crfton"]
    id = oq["id"]
    mi = oq["mid"]
    oao = oq["ig_did"]

    bot.send_message(
        m.chat.id,
        text=f"""<strong>
Session - <code>{so}</code>
Crf - <code>{crf}</code>
Id - <code>{id}</code>
Mid - <code>{mi}</code>
ig_idi - <code>{oao}</code>
By : @jokerpython3 ه ه
</strong>""",
        parse_mode="HTML"
    )

bot.infinity_polling()
