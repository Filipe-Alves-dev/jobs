from time import sleep
from emoji import emojize
for c in range(10, -1, -1):  
    sleep(1)
    print(c)
print(emojize(':fogos_de_artifício:', language='pt'))