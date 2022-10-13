import subprocess
import sys

# extract arguments bot_number and color
if len(sys.argv) != 3:
    print(len(sys.argv))
    print('usage: python3 doc.py <bot_number> <Color>')
    sys.exit(0)
bot_number = sys.argv[1]
my_color = sys.argv[2]
if(str(my_color) not in ['BLACK','Black','RED','Red']):
    print("valid colors: " + str(['BLACK','Black','RED','Red']))
    sys.exit(0)
print("MyBot  : " + str(bot_number))
print("MyColor: " + str(my_color))

# game results outfile
outfile = str(my_color)+".txt"
f = open(outfile,'w')
f.close()

import os

for i in range(51):
    # skip these bots
    if(i==5 or i==4 or i==bot_number):
        continue
    print(f'Playing as '+str(my_color)+ f' with {i}.so ...',end="\t")
    # default play as RED
    bot1 = f'./so_bots/{i}.so'
    bot2 = f'./so_bots/{bot_number}.so'
    if(my_color == "Black" or my_color == "BLACK"):
        bot2,bot1 = bot1, bot2
    
    proc = subprocess.Popen(['./bin/Desdemona', bot1, bot2], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    stdout, stderr = proc.communicate()
    print('Game Over')
    
    with open(outfile, 'a') as g:
        g.write(stdout.decode())

    if(i%5==0):
        os.system(f'python3 stats.py {my_color}.txt {my_color}')

    

