from telegram.ext import Filters
from telegram import Message

YES_WORDS = ['да', 'ага', 'конечно', 'пожалуй']
NO_WORDS = ['нет', 'нет, конечно', 'ноуп', 'найн']


class YesFilter(Filters.text):
    def filter(self, message: Message) -> bool:
        print(message.text)
        if self.strings is None:
            return bool(message.text)
        return message.text in self.strings if message.text in YES_WORDS else False
    

class NoFilter(Filters.text):
    def filter(self, message: Message) -> bool:
        if self.strings is None:
            return bool(message.text)
        return message.text in self.strings if message.text in NO_WORDS else False

