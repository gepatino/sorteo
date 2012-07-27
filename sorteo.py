quienes = ['Leonardo', 'Pablo', 'Gustavo', 'Gabriel']
max_score = 3

import random
import time

random.shuffle(quienes)
resultados = {}
winner = None

print 'Gana el que llegue a %d' % max_score
time.sleep(2)
while winner is None:
    c = random.choice(quienes)
    if c not in resultados:
        resultados[c] = 0
    resultados[c] += 1

    if resultados[c] == max_score:
        winner = c

    print '%s (%d)' % (c, resultados[c])
    time.sleep(2)

print
print 'El ganador es %s' % winner
