from random import randint
from time import sleep
print('\033[1;33m¨_-\033[m' * 20)
print('\033[34mVou pensar em um número de 0 a 5, tente adivinhar...\033[m')
print('\033[1;33m¨_-\033[m' * 20)
valor = randint(0, 5)
sleep(1)
n1 = int(input('\033[34mEm qual numero eu pensei?\033[m\n'))
print('\033[1mPROCESSANDO...')
sleep(1)
if n1 == valor:
    print('\033[1;32mVocê venceu!!\nEscolhi o número\033[m \033[34m{}'.format(valor))
else:
    print('\033[31mVocê perdeu!!\nEscolhi o número\033[m \033[1;36m{}'.format(valor))
