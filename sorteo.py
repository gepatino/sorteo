quienes = ['Alfredo', 'Leonardo', 'Pablo', 'Gustavo', 'Gabriel']
max_score = 5

import random
import time

resultados = {}
winner = None

print 'Gana el que llegue a %d' % max_score
time.sleep(2)
while winner is None:
    random.shuffle(quienes)
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
