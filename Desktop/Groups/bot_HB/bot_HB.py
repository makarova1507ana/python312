import telebot
import random
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot("6742117076:AAH9m0ljmeKKmZX2Wq1eGUozrL1oD4ueTrE")



@bot.message_handler(commands=['start'])
def get_message(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="🎉Поздравь меня!🎉", callback_data="1")

    button3 = types.InlineKeyboardButton(text="🎤ПЕСНЯ!🎵", callback_data="3")
    button4 = types.InlineKeyboardButton(text="🤡ШУТКА🤡", callback_data="4")
    button5 = types.InlineKeyboardButton(text="📸ФОТО!📸", callback_data="5")
    button6 = types.InlineKeyboardButton(text="🎮ИГРА🎮", callback_data="6")
    keyboard.add(button1)

    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    keyboard.add(button6)
    photo = open('bot_HB/we.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id,text="""Привет! Этот бот мы с Ильей создали специально для тебя! Он будет доступен тебе всегда по твоему желанию! (Надо Илье сказать и он все сделает)

Тебе доступны следующие возможности:
    🎉Поздравь меня!🎉

    🎥ФИЛЬМ🎞 

    🎤ПЕСНЯ🎵

    🤡ШУТКА🤡

    📸ФОТО📸

    🎮ИГРА🎮

    в крайнем случае можно нажать сюда /help
    """.format(message.from_user), reply_markup=keyboard)

@bot.message_handler(regexp='(/help)|(Нет! Давай по новой!)')
def get_message(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="🎉Поздравь меня!🎉", callback_data="1")

    button3 = types.InlineKeyboardButton(text="🎤ПЕСНЯ!🎵", callback_data="3")
    button4 = types.InlineKeyboardButton(text="🤡ШУТКА🤡", callback_data="4")
    button5 = types.InlineKeyboardButton(text="📸ФОТО!📸", callback_data="5")
    button6 = types.InlineKeyboardButton(text="🎮ИГРА🎮", callback_data="6")
    keyboard.add(button1)

    keyboard.add(button3)
    keyboard.add(button4)
    keyboard.add(button5)
    keyboard.add(button6)
    bot.send_message(message.chat.id, text="""
    Тебе доступны следующие возможности:
        """.format(message.from_user), reply_markup=keyboard)

# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # 🎉Поздравь
    # меня!🎉
    #
    # 🎥ФИЛЬМ🎞
    #
    # 🎤ПЕСНЯ🎵
    #
    # 🤡ШУТКА🤡

        if call.data == "1":
            texts = ['''
Пусть иногда мне не хватает слов,
Не думай, что тебя не уважаю,
Что не ценю я всех твоих трудов,
Что никогда и ничего не замечаю.

За все слова, что я не говорю,
Я у тебя прошу сейчас прощения!
Ты знай, что я тебя очень люблю.
Моя мамуля. Мама, с днем рождения.

Пусть каждый день приносит тебе радость.
Здоровья, счастья я желаю и любви.
Пусть ангелы тебя оберегают
На ждущем впереди тебя пути.



''',
'''
Мамочка, добрая и дорогая,
Неповторимая, сердцу родная,
Ни для кого пусть не будет секретом —
Ты самая лучшая мама на свете!

Спасибо тебе за бессонные ночи,
Мы ценим и любим тебя очень-очень!
Желаем тебе в день волшебный рождения
Веселья, удачи, любви и везения.

Будь самой красивой, счастливой и нежной,
Во всем мы поможем, поддержим, конечно.
Пусть будет здоровье, достаток и счастье,
Всегда полагайся на наше участие.

И помни, мамуля, и верь, что на свете
Тебя обожают любимые дети!


''',
'''
С днем рождения, мамочка! Желаю тебе в первую очередь огромного здоровья, исполнения всех желаний, счастья, долгих лет жизни! Пусть все невзгоды обходят тебя стороной, не огорчайся по пустякам и не нервничай без повода! Безумно люблю, ценю и уважаю тебя, моя самая родная и близкая! Спасибо тебе за жизнь и воспитание! Ты самая лучшая!


''',
'''
Сегодня, мама, праздник твой!
Хочу сказать со всей душой:
Роднее нет тебя на свете!
Прими же поздравления эти.

Живи без горя, не старей,
Пускай не будет грустных дней.
Почаще смейся, улыбайся,
Такой же доброй оставайся.

Болезни смело прочь гони,
Пускай в глазах горят огни.
Желаю света и тепла,
Чтоб ты счастливою была!



''',
'''
Мамочка любимая, с праздником тебя,
Поздравляем, милая, с днем рождения.
Желаем лишь здоровья, бодрости и сил,
И каждый чтоб денечек радость приносил.
Тебя мы очень любим, тобою дорожим,
За все тебе спасибо, мамуля, говорим.

''',
'''Мамочка, самый светлый и родной человек в моей жизни. Как бы женщины не печалились, что с годами их молодость уходит, для меня твой День Рождения – всегда будет лучшим и главным праздником! Весь это тот самый день, когда на свет появился человек, без которого мое существование было бы невозможно. Я желаю тебе крепкого здоровья, потому что все остальное у тебя есть – твои дети, твое счастье, красота, которая живет в каждом, богатство – твоя семья и близкие. Мы всегда будем рядом, радовать тебя, поддерживать во всем и любить. Сияй в свой праздник, мы все тебя искренне поздравляем! Пусть сегодня у тебя будет только хорошее настроение, ароматные цветы и теплые слова!''']

            bot.send_message(call.message.chat.id, random.choice(texts))
            try:
                photo = open(f'bot_HB/foto/{random.randint(1, 10)}.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
            except:
                bot.send_message(call.message.chat.id, "Извини, наш бот немного поддуривает")

        if call.data == "3":
            bot.send_message(call.message.chat.id, """Извини, наш бот немного поддуривает. Придется, подождать 
🎵Слушай! Все для тебя❤️""")
            m= [
                """bot_HB/Любимая_песня_1.mp3""",
                """bot_HB/Максим Фадеев & Наргиз-С любимыми не расставайтесь.mp3""",
                """bot_HB/Наргиз feat Максим Фадеев-Ты моя нежность.mp3"""
            ]
            music = open(random.choice(m), 'rb')
            bot.send_audio(call.message.chat.id, music)
        if call.data == "4":
            jokes =[
'''
У старого Мойше спросили:
— Вы верите в приметы?
— Смотря какие.
— Ну, например, вы проснулись утром, и встали не с той ноги…
— Милочка, в моем возрасте проснуться утром – это уже хорошая примета!

''','''

Письмо из Тель-Авива в Одессу: «Сынок, высылaем тебе 20 доллaров, кaк ты и просил… Но хотим нaпомнить, что 20 доллaров пишется не с тремя нулями, a с одним!»

 ''','''

Летит самолет Аэрофлот из Тель-Авива. Стюардесса спрашивает пассажира:
— Кушать будете?
Тот:
— А какой у меня выбор?
Стюардесса:
— Таки да или таки нет!

 ''','''

Во время праздника одна парочка уединилась в темной спальне. Шепот, шорохи, сдержанные крики, рыдания…
— Ах, Яша, почему же ты раньше не любил меня так страстно, как сегодня?! Наверное, потому, что сегодня праздник?
— Нет, наверное, это потому, что я – не Яша!

''','''

Вопрос «Есть ли евреи на других планетах?» очень интересовал доктора астрономии и члена-корреспондента Академии Наук Семёна Каца.
Когда все ушли с работы, он отправил в космос сообщение:
— Ну?
Ответ пришел через 5 минут:
— Сёма, не морочьте нам голову…

 ''','''

— Рабинович, у вас алиби есть?
— А шо это такое?
— Ну, видел ли вас кто-нибудь во время убийства?
— Слава Богу, нет.

 ''','''

— Ребе, тут в Торе пропуск!
— Не говори чепуху!
— Посмотрите сами, тут написано: не пожелай жены ближнего своего. А почему нигде нет: не пожелай мужа ближней своей?
— Ну-уу… Пускай она даже пожелает - ему-то все равно нельзя!

 ''','''

— Яша, я уже вышла из ванны и жду неприличных предложений…
— Софочка, а давай заправим оливье кетчупом.
— Нет, Яша, это уже перебор!

 ''','''

— Моня, почему ты не даришь мне цветы?
— Циля, я подарил тебе весь мир! Иди нюхай цветы на улицу!..

 ''','''

— Беня, я гарантирую вам, шо через пять лет мы будем жить лучше, чем в Европе!
— А шо у них случится?

 ''','''

— Семочка, если будешь хорошо себя вести, купим тебе велосипед!
— А если плохо?
— Пианино!

 ''','''

— Сара, выполни мою последнюю просьбу! Сожги мое тело в крематории! Прах положи в конверт, напиши там: «ТЕПЕРЬ ВЫ ПОЛУЧИЛИ С МЕНЯ ВСЁ», и отправь в налоговую.

 ''','''

— Фирочка, а чем вы увлекаетесь?
— Рисованием и верховой ездой. А вы, Боря?
— Таки не поверите… Художницами и наездницами!

 ''','''

— Рабинович, а шо вы имеете сказать за старость?
— Старость – это когда из половых органов остались одни глаза.
— А чтобы пооптимистичнее?
— Но взгляд твердый!

 ''','''

Германия. Автобус с туристами из Одессы. Экскурсовод просит каждого посмотреть, все ли его соседи сели в автобус. Закрывается дверь, автобус уезжает. Километров через десять его догоняет полицейская машина. В дверь заходит женщина средних лет и с характерным акцентом восклицает:
— Моня, не с твоим щастьем!

 ''','''

— Абраша, милый, что ты посоветуешь мне почитать?
— Сарочка! Почитай молитву, пока я дочитываю переписку в твоем телефоне!

 ''','''

Бабушка поспорила с Семой, что он не съест ее 25 пельменей на то, что он уберет в квартире. И вот Сема доедает 24-й пельмень и понимает, что 25-го в тарелке нет. Это все, что нужно знать о составлении договоров.

 ''','''

— Фирочка, я устал. Можно, я уже пойду домой?
— Нюма, перестань ныть! Муж вернётся только через неделю!

''','''

— Мамочка, почему Соломон был такой мудрый?
— Потому, сынок, что у него было много жен и он со всеми советовался…

''','''

— Доктор, скажите шо мне делать с теми двумя зубами, которые болят?
— Только удалять!
— И шо мне это будет стоить?
— 150 долларов.
— Ничего себе! 150 долларов за две минуты работы?!
— Хорошо… я буду тащить медленно….

''','''

— Раечка! Что у нaс нa обед?
— Фaсолевый суп.
— А нa второе?
— Активировaнный уголь.

 ''','''

Совесть есть, но с собой не ношу, боюсь потерять.

 ''','''

Хоронят известного одесского врача.
Люди подходят, бросают пригоршню земли.
Вдруг всех расталкивает Кацман и устремляется к могиле.
— Яша, вы шо, дикий? Станьте в очередь!
— Ой, та я только спросить!

 ''','''

Почему в Израиле нельзя заниматься сексом на газоне?
— Потому что прохожие замучают советами.

 ''','''

— Что такое одесский анекдот?
— Это то, что приезжий не поймёт, а одессит уже слышал вчера…

 ''','''

К мудрому царю Соломону пришли две крикливые тетки и привели юношу.
— Он женится на моейr дочери! - вопит одна.
— Нет, на моей! - орет вторая.
Царь подумал и говорит:
— Принесите пилу. Распилим его пополам и каждой половину. Согласны?
Первая баба:
— Согласна, о мудрейший из мудрейших!
Вторая тетка (подумав):
— Да зачем же невинную душу губить?..
Тогда царь Соломон сказал:
— Он женится на дrочери первой женщины.
Вторая баба:
— Но ведь она только что хотела его распилить?!
Соломон:
— Вот, вот. Она и есть настоящая ТЁЩА!

 ''']

            if random.randint(0,1) == 0:
                try:
                    photo = open(f'bot_HB/foto/{random.randint(11, 18)}.jpg', 'rb')
                    bot.send_photo(call.message.chat.id, photo)
                except:
                    bot.send_message(call.message.chat.id, "Извини, наш бот немного поддуривает")
            else:
                bot.send_message(call.message.chat.id, random.choice(jokes))

        if call.data == "5":
            try:
                photo = open(f'bot_HB/foto/{random.randint(1,10)}.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo)
            except:
                bot.send_message(call.message.chat.id, "Извини, наш бот немного поддуривает")
        if call.data == "6":
            start_game(call.message)


        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="🎉Поздравь меня!🎉", callback_data="1")

        button3 = types.InlineKeyboardButton(text="🎤ПЕСНЯ!🎵", callback_data="3")
        button4 = types.InlineKeyboardButton(text="🤡ШУТКА🤡", callback_data="4")
        button5 = types.InlineKeyboardButton(text="📸ФОТО!📸", callback_data="5")
        button6 = types.InlineKeyboardButton(text="🎮ИГРА🎮", callback_data="6")
        keyboard.add(button1)

        keyboard.add(button3)
        keyboard.add(button4)
        keyboard.add(button5)
        keyboard.add(button6)
        bot.send_message(call.message.chat.id, text="""
                Тебе доступны следующие возможности:
                    """.format(call.message.chat.id), reply_markup=keyboard)

# @bot.message_handler(regexp='🎉Поздравь меня!🎉')
# def message_reply(message):
#     l = ["""""",]
#     message = bot.reply_to(message, random.choice(l))
# @bot.message_handler(regexp='🎥ФИЛЬМ🎞')
# def message_reply(message):
#     pass
#
# @bot.message_handler(regexp='🎤ПЕСНЯ🎵')
# def message_reply(message):
#     pass
#
# @bot.message_handler(regexp='🤡ШУТКА🤡')
# def message_reply(message):
#     l = ["""""", ]
#     message = bot.reply_to(message, random.choice(l))
#
# @bot.message_handler(regexp='📸ФОТО📸')
# def message_reply(message):
#     photo = open('путь_к_фото', 'rb')
#     bot.send_photo(message.chat.id, photo)

@bot.message_handler(regexp='(🎮ИГРА🎮)|(Играть еще раз!)')
def start_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton("Камень 🗿")
    btn5 = types.KeyboardButton("Ножницы ✂")
    btn6 = types.KeyboardButton("Бумага ▧")
    markup.add(btn4, btn5, btn6)
    message = bot.send_message(message.chat.id, """Привет, это игра камень, ножницы, бумага! Сделай свой ход!""",
                           reply_markup=markup)
    bot.register_next_step_handler(message, ww)

def ww(message):
    ran = random.randint(0, 2)
    sp = ["Камень 🗿", "Ножницы ✂", "Бумага ▧"]
    if message.text == sp[ran]:
        bot.send_message(message.chat.id, sp[ran])
        bot.send_message(message.chat.id, "Ничья!")
    elif message.text == "Камень 🗿" and sp[ran] == "Ножницы ✂":
        bot.send_message(message.chat.id, sp[ran])
        bot.send_message(message.chat.id, "Победа игрока!")
    elif message.text == "Ножницы ✂" and sp[ran] == "Бумага ▧":
        bot.send_message(message.chat.id, sp[ran])
        bot.send_message(message.chat.id, "Победа игрока!")
    elif message.text == "Бумага ▧" and sp[ran] == "Камень 🗿":
        bot.send_message(message.chat.id, sp[ran])
        bot.send_message(message.chat.id, "Победа игрока!")
    else:
        bot.send_message(message.chat.id, sp[ran])
        bot.send_message(message.chat.id, "Победа компьютера!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn6 = types.KeyboardButton("Играть еще раз!")
    btn7 = types.KeyboardButton("Нет! Давай по новой!")
    markup.add(btn6, btn7)
    bot.send_message(message.chat.id, text="Хочешь сыграть еще раз?", reply_markup= markup)


@bot.message_handler()
def message_reply(message):
    if message.text == "Привет!" or message.text == "привет!"or message.text == "привет" or message.text == "Привет":
        bot.send_message(message.chat.id, "Привет!")
    elif message.text == "Что ты умеешь?" or message.text == "Что ты можешь?":
        bot.send_message(message.chat.id, "Выбери команду /help")
    elif message.text == "❤️":
        bot.send_message(message.chat.id, "❤️")
    else:
        l = ["ой кажется я тебя не понял 😔", "Я еще учусь и не на все могу ответить", "извини, я пока знаю не так много 😔", "Попробуй использовать кнопки, кажется, я не знаю как тебе помочь 😔"]
        bot.send_message(message.chat.id,random.choice(l))
bot.polling(none_stop=True, interval=0)