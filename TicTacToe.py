#Code that runs TicTacToe
#Written in Python 3 using Pycharm editor

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
game_matrix = [str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h), str(i)]
print("Welcome to Noughts and Crosses, below is the game grid...")
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
m = input("Player one (Crosses), please enter the number which you would like to claim. ")
while m not in game_matrix:
    m = input("Try again: ")
if m == str(a):
    game_matrix.remove(str(a))
    a = "X"
if m == str(b):
    game_matrix.remove(str(b))
    b = "X"
if m == str(c):
    game_matrix.remove(str(c))
    c = "X"
if m == str(d):
    game_matrix.remove(str(d))
    d = "X"
if m == str(e):
    game_matrix.remove(str(e))
    e = "X"
if m == str(f):
    game_matrix.remove(str(f))
    f = "X"
if m == str(g):
    game_matrix.remove(str(g))
    g = "X"
if m == str(h):
    game_matrix.remove(str(h))
    h = "X"
if m == str(i):
    game_matrix.remove(str(i))
    i = "X"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
n = input("Player two (Noughts), please enter the number which you would like to claim. ")
while n not in game_matrix:
    n = input("Try again ")
if n == str(a):
    game_matrix.remove(str(a))
    a = "O"
if n == str(b):
    game_matrix.remove(str(b))
    b = "O"
if n == str(c):
    game_matrix.remove(str(c))
    c = "O"
if n == str(d):
    game_matrix.remove(str(d))
    d = "O"
if n == str(e):
    game_matrix.remove(str(e))
    e = "O"
if n == str(f):
    game_matrix.remove(str(f))
    f = "O"
if n == str(g):
    game_matrix.remove(str(g))
    g = "O"
if n == str(h):
    game_matrix.remove(str(h))
    h = "O"
if n == str(i):
    game_matrix.remove(str(i))
    i = "O"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
m = input("Player one (Crosses), please enter the number which you would like to claim. ")
while m not in game_matrix:
    m = input("Try again: ")
if m == str(a):
    game_matrix.remove(str(a))
    a = "X"
if m == str(b):
    game_matrix.remove(str(b))
    b = "X"
if m == str(c):
    game_matrix.remove(str(c))
    c = "X"
if m == str(d):
    game_matrix.remove(str(d))
    d = "X"
if m == str(e):
    game_matrix.remove(str(e))
    e = "X"
if m == str(f):
    game_matrix.remove(str(f))
    f = "X"
if m == str(g):
    game_matrix.remove(str(g))
    g = "X"
if m == str(h):
    game_matrix.remove(str(h))
    h = "X"
if m == str(i):
    game_matrix.remove(str(i))
    i = "X"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
n = input("Player two (Noughts), please enter the number which you would like to claim. ")
while n not in game_matrix:
    n = input("Try again ")
if n == str(a):
    game_matrix.remove(str(a))
    a = "O"
if n == str(b):
    game_matrix.remove(str(b))
    b = "O"
if n == str(c):
    game_matrix.remove(str(c))
    c = "O"
if n == str(d):
    game_matrix.remove(str(d))
    d = "O"
if n == str(e):
    game_matrix.remove(str(e))
    e = "O"
if n == str(f):
    game_matrix.remove(str(f))
    f = "O"
if n == str(g):
    game_matrix.remove(str(g))
    g = "O"
if n == str(h):
    game_matrix.remove(str(h))
    h = "O"
if n == str(i):
    game_matrix.remove(str(i))
    i = "O"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
m = input("Player one (Crosses), please enter the number which you would like to claim. ")
while m not in game_matrix:
    m = input("Try again: ")
if m == str(a):
    game_matrix.remove(str(a))
    a = "X"
if m == str(b):
    game_matrix.remove(str(b))
    b = "X"
if m == str(c):
    game_matrix.remove(str(c))
    c = "X"
if m == str(d):
    game_matrix.remove(str(d))
    d = "X"
if m == str(e):
    game_matrix.remove(str(e))
    e = "X"
if m == str(f):
    game_matrix.remove(str(f))
    f = "X"
if m == str(g):
    game_matrix.remove(str(g))
    g = "X"
if m == str(h):
    game_matrix.remove(str(h))
    h = "X"
if m == str(i):
    game_matrix.remove(str(i))
    i = "X"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
if a == "X" and b == "X" and c == "X":
    print("Player one wins!!")
    exit()
if a == "X" and d == "X" and g == "X":
    print("Player one wins!!")
    exit()
if a == "X" and e == "X" and i == "X":
    print("Player one wins!!")
    exit()
if d == "X" and e == "X" and f == "X":
    print("Player one wins!!")
    exit()
if g == "X" and h == "X" and i == "X":
    print("Player one wins!!")
    exit()
if b == "X" and e == "X" and h == "X":
    print("Player one wins!!")
    exit()
if c == "X" and f == "X" and i == "X":
    print("Player one wins!!")
    exit()
if c == "X" and e == "X" and g == "X":
    print("Player one wins!!")
    exit()
n = input("Player two (Noughts), please enter the number which you would like to claim. ")
while n not in game_matrix:
    n = input("Try again ")
if n == str(a):
    game_matrix.remove(str(a))
    a = "O"
if n == str(b):
    game_matrix.remove(str(b))
    b = "O"
if n == str(c):
    game_matrix.remove(str(c))
    c = "O"
if n == str(d):
    game_matrix.remove(str(d))
    d = "O"
if n == str(e):
    game_matrix.remove(str(e))
    e = "O"
if n == str(f):
    game_matrix.remove(str(f))
    f = "O"
if n == str(g):
    game_matrix.remove(str(g))
    g = "O"
if n == str(h):
    game_matrix.remove(str(h))
    h = "O"
if n == str(i):
    game_matrix.remove(str(i))
    i = "O"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
if a == "O" and b == "O" and c == "O":
    print("Player two wins!!")
    exit()
if a == "O" and d == "O" and g == "O":
    print("Player two wins!!")
    exit()
if a == "O" and e == "O" and i == "O":
    print("Player two wins!!")
    exit()
if d == "O" and e == "O" and f == "O":
    print("Player two wins!!")
    exit()
if g == "O" and h == "O" and i == "O":
    print("Player two wins!!")
    exit()
if b == "O" and e == "O" and h == "O":
    print("Player two wins!!")
    exit()
if c == "O" and f == "O" and i == "O":
    print("Player two wins!!")
    exit()
if c == "O" and e == "O" and g == "O":
    print("Player two wins!!")
    exit()
m = input("Player one (Crosses), please enter the number which you would like to claim. ")
while m not in game_matrix:
    m = input("Try again: ")
if m == str(a):
    game_matrix.remove(str(a))
    a = "X"
if m == str(b):
    game_matrix.remove(str(b))
    b = "X"
if m == str(c):
    game_matrix.remove(str(c))
    c = "X"
if m == str(d):
    game_matrix.remove(str(d))
    d = "X"
if m == str(e):
    game_matrix.remove(str(e))
    e = "X"
if m == str(f):
    game_matrix.remove(str(f))
    f = "X"
if m == str(g):
    game_matrix.remove(str(g))
    g = "X"
if m == str(h):
    game_matrix.remove(str(h))
    h = "X"
if m == str(i):
    game_matrix.remove(str(i))
    i = "X"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
if a == "X" and b == "X" and c == "X":
    print("Player one wins!!")
    exit()
if a == "X" and d == "X" and g == "X":
    print("Player one wins!!")
    exit()
if a == "X" and e == "X" and i == "X":
    print("Player one wins!!")
    exit()
if d == "X" and e == "X" and f == "X":
    print("Player one wins!!")
    exit()
if g == "X" and h == "X" and i == "X":
    print("Player one wins!!")
    exit()
if b == "X" and e == "X" and h == "X":
    print("Player one wins!!")
    exit()
if c == "X" and f == "X" and i == "X":
    print("Player one wins!!")
    exit()
if c == "X" and e == "X" and g == "X":
    print("Player one wins!!")
    exit()
n = input("Player two (Noughts), please enter the number which you would like to claim. ")
while n not in game_matrix:
    n = input("Try again ")
if n == str(a):
    game_matrix.remove(str(a))
    a = "O"
if n == str(b):
    game_matrix.remove(str(b))
    b = "O"
if n == str(c):
    game_matrix.remove(str(c))
    c = "O"
if n == str(d):
    game_matrix.remove(str(d))
    d = "O"
if n == str(e):
    game_matrix.remove(str(e))
    e = "O"
if n == str(f):
    game_matrix.remove(str(f))
    f = "O"
if n == str(g):
    game_matrix.remove(str(g))
    g = "O"
if n == str(h):
    game_matrix.remove(str(h))
    h = "O"
if n == str(i):
    game_matrix.remove(str(i))
    i = "O"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
if a == "O" and b == "O" and c == "O":
    print("Player one wins!!")
    exit()
if a == "O" and d == "O" and g == "O":
    print("Player two wins!!")
    exit()
if a == "O" and e == "O" and i == "O":
    print("Player two wins!!")
    exit()
if d == "O" and e == "O" and f == "O":
    print("Player two wins!!")
    exit()
if g == "O" and h == "O" and i == "O":
    print("Player two wins!!")
    exit()
if b == "O" and e == "O" and h == "O":
    print("Player two wins!!")
    exit()
if c == "O" and f == "O" and i == "O":
    print("Player two wins!!")
    exit()
if c == "O" and e == "O" and g == "O":
    print("Player two wins!!")
    exit()
m = input("Player one (Crosses), please enter the number which you would like to claim. ")
while m not in game_matrix:
    m = input("Try again: ")
if m == str(a):
    game_matrix.remove(str(a))
    a = "X"
if m == str(b):
    game_matrix.remove(str(b))
    b = "X"
if m == str(c):
    game_matrix.remove(str(c))
    c = "X"
if m == str(d):
    game_matrix.remove(str(d))
    d = "X"
if m == str(e):
    game_matrix.remove(str(e))
    e = "X"
if m == str(f):
    game_matrix.remove(str(f))
    f = "X"
if m == str(g):
    game_matrix.remove(str(g))
    g = "X"
if m == str(h):
    game_matrix.remove(str(h))
    h = "X"
if m == str(i):
    game_matrix.remove(str(i))
    i = "X"
print("")
print([str(a), str(b), str(c)])
print([str(d), str(e), str(f)])
print([str(g), str(h), str(i)])
print("")
if a == "X" and b == "X" and c == "X":
    print("Player one wins!!")
    exit()
if a == "X" and d == "X" and g == "X":
    print("Player one wins!!")
    exit()
if a == "X" and e == "X" and i == "X":
    print("Player one wins!!")
    exit()
if d == "X" and e == "X" and f == "X":
    print("Player one wins!!")
    exit()
if g == "X" and h == "X" and i == "X":
    print("Player one wins!!")
    exit()
if b == "X" and e == "X" and h == "X":
    print("Player one wins!!")
    exit()
if c == "X" and f == "X" and i == "X":
    print("Player one wins!!")
    exit()
if c == "X" and e == "X" and g == "X":
    print("Player one wins!!")
    exit()
print("Draw. To rematch, restart the console! ")
