import logging
import re

from collections import defaultdict
from scipy.stats import binom
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

from configs import configure_logging
from constants import PROBABILITIES_LIST, BOT_TOKEN
from output import pretty_output
from utils import chek_list, multiple


def get_input():
    ver_list = input('Введите цепочку вероятностей через пробел: ').split()
    return ver_list

def get_probabilities(probability):
    int_test_probability = 0
    attempts = 1
    results = [('Вероятность', 'Количесво попыток')]
    probabilities = defaultdict(int)
    while int_test_probability < max(PROBABILITIES_LIST):
        distr = binom(attempts, probability)
        test_probability = 1 - distr.cdf(0)
        int_test_probability = int(test_probability * 100 // 1)
        if int_test_probability in PROBABILITIES_LIST:
            if probabilities.get(int_test_probability) is None:
                probabilities[int_test_probability] = attempts
        attempts += 1
    results.extend(probabilities.items())
    return results

async def bot_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text =('Hello. User /prob to send a list of probabilities.\n'
           'e.g.: /prob 35 30 25 20 15 50')
    await context.bot.send_message(chat_id=chat_id, text=text)

async def bot_proba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text.replace('/prob', '').strip()
    probs_list = re.findall('\d+', text)
    logging.info(probs_list)
    probabilities_list = chek_list(probs_list)
    probabilities_list = [x / 100 for x in probabilities_list]
    probability = multiple(probabilities_list)
    results = get_probabilities(probability)
    results = pretty_output(results)
    logging.info(f'Тип результата: {type(results)}')
    logging.info(results)
    await context.bot.send_message(
        chat_id, text=f'<pre>{results.get_string()}</pre>',
        parse_mode=ParseMode.HTML)

def main():
    logging.info(f'BOT_TOKEN = {BOT_TOKEN}')
    
    application = Application.builder().token(BOT_TOKEN).build()

    start_hendler = CommandHandler('start', bot_hi)
    proba_hendler = CommandHandler('prob', bot_proba)

    application.add_handler(start_hendler)
    application.add_handler(proba_hendler)
    application.run_polling(10)


if __name__ == '__main__':
    configure_logging()
    logging.info('Бот запущен.')
    main()
    logging.info('Бот завершил работу.')
