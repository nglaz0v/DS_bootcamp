#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создайте класс User и и его наследника класс SuperUser, которые описывают пользователя и супер-пользователя.
В классе User необходимо описать:
* Конструктор, который принимает в качестве параметров значения для атрибутов name, login и password;
* Методы для изменения и получения значений атрибутов;
* Метод show_info, который печатает в произвольном формате значения атрибутов name и login;
* Атрибут класса count для хранения количества созданных экземпляров класса User.
Необходимые условия, которые надо учесть после создания объекта:
* Атрибут name доступен и для чтения, и для изменения;
* Атрибут login доступен только для чтения;
* Атрибут password доступен только для изменения.
В классе SuperUser необходимо описать:
* Конструктор, который принимает в качестве параметров значения для атрибутов name, login, password и role;
* Метод для изменения и получения значения атрибута role;
* Метод show_info, который печатает в произвольном формате значения атрибутов name, login и role;
* Атрибут класса count для хранения количества созданных экземпляров класса SuperUser.
"""


class User:
    count = 0

    def __init__(self, name, login, password):
        self._name = name
        self._login = login
        self._password = password
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    def _set_password(self, value):
        self._password = value
    password = property(fset=_set_password)

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}")


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self._role = role
        User.count -= 1
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}, Role: {self._role}")
