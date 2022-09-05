#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Фракталы
"""
import turtle


def create_l_system(iters: int, axiom: str, rules: dict) -> str:
    """Создать L-систему."""
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string
    return end_string  # сгенерированная L-система


def draw_l_systems(t, instructions: str, angle: float, distance: float) -> None:
    """Нарисовать L-систему."""
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)  # ползти вперёд
        elif cmd == '+':
            t.right(angle)  # повернуть вправо
        elif cmd == '-':
            t.left(angle)  # повернуть влево


def main(title: str, iterations: int, axiom: str, rules: dict, angle: int,
         length=8, size=2, y_offset=0, x_offset=0, offset_angle=0, width=450,
         heigth=450) -> None:
    """Нарисовать фрактал с помощью черепашьей графики."""
    # набор инструкций для "черепахи"
    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()  # "черепаха"
    wn = turtle.Screen()  # окно для рисования
    wn.setup(width, heigth)  # размеры окна
    wn.title(title)  # заголовок окна

    # начальное позиционирование "черепахи"
    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_systems(t, inst, angle, length)  # нарисовать фрактал
    t.hideturtle()  # скрыть "черепаху"

    wn.ontimer(None, 3000)  # пауза
    wn.clear()  # очистить окно


# title = "Снежинка Коха"
# axiom = "F--F--F"
# rules = {"F": "F+F--F+F"}
# iterations = 4  # TOP: 7
# angle = 60
# main(title, iterations, axiom, rules, angle)

# title = "Квадратный остров Коха"
# axiom = "F+F+F+F"
# rules = {"F": "F-F+F+FFF-F-F+F"}
# iterations = 2  # TOP: 4
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Кристалл"
# axiom = "F+F+F+F"
# rules = {"F": "FF+F++F+F"}
# iterations = 3  # TOP: 6
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Квадратная снежинка"
# axiom = "F--F"
# rules = {"F": "F-F+F+F-F"}
# iterations = 4  # TOP: 6
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Фрактал Вичека"
# axiom = "F-F-F-F"
# rules = {"F": "F-F+F+F-F"}
# iterations = 4  # TOP: 6
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Кривая Леви"
# axiom = "F"
# rules = {"F": "+F--F+"}
# iterations = 10  # TOP: 16
# angle = 45
# main(title, iterations, axiom, rules, angle)

# title = "Ковёр Серпинского"
# axiom = "YF"
# rules = {"X": "YF+XF+Y", "Y": "XF-YF-X"}
# iterations = 5  # TOP: 10
# angle = 60
# main(title, iterations, axiom, rules, angle)

# title = "Решётка Серпинского"
# axiom = "FXF--FF--FF"
# rules = {"F": "FF", "X": "--FXF++FXF++FXF--"}
# iterations = 7  # TOP: 8
# angle = 60
# main(title, iterations, axiom, rules, angle)

# title = "Квадрат"
# axiom = "F+F+F+F"
# rules = {"F": "FF+F+F+F+FF"}
# iterations = 3  # TOP: 5
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Плитки"
# axiom = "F+F+F+F"
# rules = {"F": "FF+F-F+F+FF"}
# iterations = 3  # TOP: 4
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Кольца"
# axiom = "F+F+F+F"
# rules = {"F": "FF+F+F+F+F+F-F"}
# iterations = 2  # TOP: 4
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Крест-2"
# axiom = "F+F+F+F"
# rules = {"F": "F+F-F+F+F"}
# iterations = 3  # TOP: 6
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Pentaplexity"
# axiom = "F++F++F++F++F"
# rules = {"F": "F++F++F+++++F-F++F"}
# iterations = 1  # TOP: 5
# angle = 36
# main(title, iterations, axiom, rules, angle)

# title = "32-сегментная кривая"
# axiom = "F+F+F+F"
# rules = {"F": "-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
# iterations = 3  # TOP: 3
# angle = 90
# main(title, iterations, axiom, rules, angle)

title = "Кривая Пеано-Госпера"
axiom = "FX"
rules = {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}
iterations = 3  # TOP: 6
angle = 60
main(title, iterations, axiom, rules, angle)

title = "Кривая Серпинского"
axiom = "F+XF+F+XF"
rules = {"X": "XF-F+F-XF+F+XF-F+F-X"}
iterations = 3  # TOP: 8
angle = 90
main(title, iterations, axiom, rules, angle)

# title = "Анклеты Кришны"
# axiom = " -X--X"
# rules = {"X": "XFX--XFX"}
# iterations = 3  # TOP: 9
# angle = 45
# main(title, iterations, axiom, rules, angle)

# title = "Квадратный фрактал Госпера"
# axiom = "YF"
# rules = {"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
#          "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}
# iterations = 2  # TOP: 3
# angle = 90
# main(title, iterations, axiom, rules, angle)

title = "Кривая Мура"
axiom = "LFL-F-LFL"
rules = {"L": "+RF-LFL-FR+", "R": "-LF+RFR+FL-"}
iterations = 3  # TOP: 8
angle = 90
main(title, iterations, axiom, rules, angle)

title = "Кривая Гильберта"
axiom = "L"
rules = {"L": "+RF-LFL-FR+", "R": "-LF+RFR+FL-"}
iterations = 4  # TOP: 9
angle = 90
main(title, iterations, axiom, rules, angle)

# title = "Кривая Гильберта-II"
# axiom = "X"
# rules = {"X": "XFYFX+F+YFXFY-F-XFYFX", "Y": "YFXFY-F-XFYFX+F+YFXFY"}
# iterations = 3  # TOP: 6
# angle = 90
# main(title, iterations, axiom, rules, angle)

title = "Кривая Пеано"
axiom = "F"
rules = {"F": "F+F-F-F-F+F+F+F-F"}
iterations = 3  # TOP: 5
angle = 90
main(title, iterations, axiom, rules, angle)

# title = "Крест"
# axiom = "F+F+F+F"
# rules = {"F": "F+FF++F+F"}
# iterations = 3  # TOP: 6
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Треугольник"
# axiom = "F+F+F"
# rules = {"F": "F-F+F"}
# iterations = 2  # TOP: 9
# angle = 120
# main(title, iterations, axiom, rules, angle)

# title = "Кривая дракона"
# axiom = "FX"
# rules = {"X": "X+YF+", "Y": "-FX-Y"}
# iterations = 8  # TOP: 16
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Кривая Terdragon"
# axiom = "F"
# rules = {"F": "F-F+F"}
# iterations = 5  # TOP: 10
# angle = 120
# main(title, iterations, axiom, rules, angle)

# title = "Двойная кривая дракона"
# axiom = "FX+FX"
# rules = {"X": "X+YF+", "Y": "-FX-Y"}
# iterations = 6  # TOP: 16
# angle = 90
# main(title, iterations, axiom, rules, angle)

# title = "Тройная кривая дракона"
# axiom = "FX+FX+FX"
# rules = {"X": "X+YF+", "Y": "-FX-Y"}
# iterations = 7  # TOP: 15
# angle = 90
# main(title, iterations, axiom, rules, angle)

turtle.bye()  # завершить работу с "черепахой"
