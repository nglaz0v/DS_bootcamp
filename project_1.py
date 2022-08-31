# -*- coding: utf-8 -*-
"""
Разработайте класс Logger, который:

1. Создаёт файл лога при инициализации объекта (по указанному пути или по
   умолчанию в корневой папке).
  *Обеспечить существование только одного объекта этого класса (паттерн
   Singleton)
2. Название файла должно иметь формат log_dd.mm.yy.
3. Внутри должен быть приватный метод, который возвращает текущую дату.
4. Все события одного дня должны писаться в один файл. Если день меняется,
   должен создаваться новый файл при записи в лог по шаблону из п.2
5. Поддерживает метод write_log(), записывающий событие в правильный файл дня в
   формате: [06:23:15] Произошедшее событие
6. Поддерживает метод clear_log(), который удаляет записи в файле текущего дня.
7. Поддерживает метод get_logs(), возвращающий записи из файла текущего дня в
   виде списка (один элемент списка — запись одного события).
8. Поддерживает метод get_last_event(), который возвращает запись о последнем
   событии.
9. Поддерживает метод get_all_logs(), который возвращает список всех файлов
   лога.
Предусмотреть крайние ситуации при которых возможен вылет. Исключить возможные
ошибки конструкциями try-except и raise exception.
"""

import datetime
# import io
import os
import re
import sys


class LoggerException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Logger:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def __init__(self, path="./"):
        if not (os.path.exists(path) and os.path.isdir(path)):
            raise LoggerException(f"invalid path: {path}")
        self.__path = path
        self.__last_event = ''
        try:
            f = open(self.__log_name(), 'a')
        except IOError:
            raise LoggerException(f"problem in {sys._getframe().f_code.co_name}")
        finally:
            f.close()

    def __log_name(self):
        """полное имя лога."""
        return os.path.join(self.__path, f"log_{Logger.__current_date()}")

    @staticmethod
    def __current_date():
        """текущая дата."""
        now = datetime.datetime.now()
        return now.strftime("%d.%m.%y")

    def write_log(self, event):
        """записать событие в файл."""
        now = datetime.datetime.now()
        mark = now.strftime("%H:%M:%S")
        self.__last_event = event
        try:
            with open(self.__log_name(), 'a') as f:
                f.write(f"[{mark}] {self.__last_event}\n")
        except IOError:
            raise LoggerException(f"problem in {sys._getframe().f_code.co_name}")

    def clear_log(self):
        """удалить записи в файле текущего дня."""
        try:
            f = open(self.__log_name(), 'w')
            # f.truncate(0)
        except IOError:
            raise LoggerException(f"problem in {sys._getframe().f_code.co_name}")
        finally:
            f.close()

    def get_logs(self):
        """вернуть записи из файла текущего дня в виде списка (один элемент списка — запись одного события)."""
        events = []
        p = re.compile(r"\[(\d\d\:\d\d\:\d\d)\] (\w+)")
        try:
            with open(self.__log_name(), 'r') as f:
                # f.seek(0, io.SEEK_SET)
                content = '\n'.join(f.readlines())
                # f.seek(0, io.SEEK_END)
                events = p.findall(content)
        except IOError:
            raise LoggerException(f"problem in {sys._getframe().f_code.co_name}")
        return events

    def get_last_event(self):
        """вернуть запись о последнем событии."""
        return self.__last_event

    def get_all_logs(self):
        """вернуть список всех файлов лога."""
        return [fname for fname in os.listdir(path=self.__path) if fname.startswith("log_")]


logger = Logger()
logger.write_log("test1")
logger.write_log("test2")
logger.write_log("test3")
print(logger.get_logs())
logger.clear_log()
logger.write_log("test")
print(logger.get_last_event())
print(logger.get_all_logs())
