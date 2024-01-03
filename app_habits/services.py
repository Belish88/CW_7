import smtplib

from datetime import time, datetime, date, timedelta

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


from app_habits.models import Habit
from config import settings


class TgBot:
    URL = "https://api.telegram.org/bot"
    TOKEN = settings.TELEGRAM_BOT_TOKEN

    def __init__(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': self.chat_id,
                'text': text
            }
        )


def checking_readiness():
    tasks = Habit.objects.filter(is_nice=False)
    print('проверка началась')
    now_d = date.today()
    print(now_d)
    now_h = datetime.now().hour
    now_m = datetime.now().minute
    for task in tasks:
        if now_d == task.start_date:
            if now_h == task.start_time.hour:
                if now_m == task.start_time.minute:
                    task.start_date = task.start_date + timedelta(days=int(task.periodic))
                    task.save()
                    user_id = task.owner.telegram_id
                    send_message_to_telegram(user_id, task)


def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(checking_readiness, 'interval', minutes=1)
    scheduler.start()
    print('sheduler')
    return True


def send_message_to_telegram(user_id, task):
    """ Отправка сообщения """
    chat_id = user_id
    start_time = task.start_time
    task_task = task.task
    location = task.location
    time_to_complete = task.time_to_complete
    reward = task.reward
    related = task.related

    # Формирование основного текста
    text = (
        f'Я буду {task_task} в {start_time} {location} '
        f'в течении {time_to_complete} секунд.'
    )
    # Формирование текста вознаграждения при наличии
    reward = f'\nЗа это, я {reward}.' if reward else ''
    # Формирование текста связанной привычки при наличии
    related = (f'\nПосле этого я {related.get("task")}'
                     f' {related.get("location")} '
                     f'в течении {related.get("time_to_complete")} секунд.') if related else ''

    # Отправка сообщения
    tg_bot = TgBot(chat_id)
    message = text + reward + related
    tg_bot.send_message(message)

    # Для тестирования добавляем возврат сформированного сообщения
    return message
