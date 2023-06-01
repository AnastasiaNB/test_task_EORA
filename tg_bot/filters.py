from typing import List, Tuple, Union

from telegram import Message, Update
from telegram.ext.filters import MessageFilter

YES_WORDS = ['да', 'ага', 'конечно', 'пожалуй']
NO_WORDS = ['нет', 'нет, конечно', 'ноуп', 'найн']


class YesFilter(MessageFilter):
    __slots__ = ()
    name = 'Filters.text'

    class _TextStrings(MessageFilter):
        __slots__ = ('strings',)

        def __init__(self, strings: Union[List[str], Tuple[str]]):
            self.strings = strings
            self.name = f'Filters.text({strings})'

        def filter(self, message: Message) -> bool:
            if message.text:
                return message.text in self.strings
            return False

    def __call__(
        self, update: Union[Update, List[str], Tuple[str]]
    ) -> Union[bool, '_TextStrings']:
        if isinstance(update, Update):
            return self.filter(update.effective_message)
        return self._TextStrings(update)

    def filter(self, message: Message) -> bool:
        text = message.text.lower()
        return text if text in YES_WORDS else False


class NoFilter(MessageFilter):
    __slots__ = ()
    name = 'Filters.text'

    class _TextStrings(MessageFilter):
        __slots__ = ('strings',)

        def __init__(self, strings: Union[List[str], Tuple[str]]):
            self.strings = strings
            self.name = f'Filters.text({strings})'

        def filter(self, message: Message) -> bool:
            if message.text:
                return message.text in self.strings
            return False

    def __call__(
        self, update: Union[Update, List[str], Tuple[str]]
    ) -> Union[bool, '_TextStrings']:
        if isinstance(update, Update):
            return self.filter(update.effective_message)
        return self._TextStrings(update)

    def filter(self, message: Message) -> bool:
        text = message.text.lower()
        return text if text in NO_WORDS else False
