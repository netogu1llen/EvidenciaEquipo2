"""Tic Tac Toe

Juego base modificado:
1. Cambio de tamanio en simbolos
2. Cambio de color en simbolos
3. Centrar simbolos
4. Validar si una casilla ya esta ocupada
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    """color cambia el color de la linea"""
    color('red')
    """Change number values for width and position"""
    line(x + 100, y + 33, x + 33, y + 100)
    line(x + 100, y + 100, x + 33, y + 33)


def drawo(x, y):
    """Draw O player."""
    up()
    """Change goto values for position"""
    goto(x + 67, y + 33)
    down()
    """color cambia el color de la linea"""
    color('blue')
    """Change circle value for width"""
    circle(31)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
