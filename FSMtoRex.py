from greenery import fsm, lego

A, B, C, D = range(4)
a, b = 'a', 'b'

# Creamos el automata
automata = fsm.fsm(
    alphabet = {a, b},
    states   = {A, B, C, D},
    initial  = A,
    finals   = {C, D},
    map      = {
            A : {b: B, a: A},
            B : {a: C, b: C},
            C : {a: D, b: D},
            D : {},
    },
)

# Convertirmos el automata en expresión regular
expresionRegular = lego.from_fsm(automata)
print(automata)
print(expresionRegular)