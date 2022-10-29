import subprocess
from subprocess import Popen, PIPE
import sys
import os

# extract arguments bot_number and color
if len(sys.argv) != 3:
    print(len(sys.argv))
    print('usage: python3 play.py <bot_number> <Color>')
    sys.exit(0)

bot_number = sys.argv[1]
my_color = str(sys.argv[2]).lower()
# validity of arguments
if(my_color!='red') and (my_color!='black'):
    print("valid colors: " + str(['black', 'red']))
    sys.exit(0)
print("MyBot  : " + str(bot_number))
print("MyColor: " + str(my_color))

for i in range(51):

    if(i==5 or i==4 or i==bot_number): # bad bots
        continue

    print(f'Playing as '+str(my_color)+ f' with {i}.so ...',end="\t")


    bot1 = f'./so_bots/{i}.so'
    bot2 = f'./so_bots/{bot_number}.so'
    if(my_color == "black"):
        bot2,bot1 = bot1, bot2
    
    # play!
    session = subprocess.Popen(['./bin/Desdemona', f'{bot1}', f'{bot2}'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    with open(f"stats/{my_color}/{i}", 'w') as file:
        file.write(stderr.decode())
        file.write(stdout.decode())

    # who won?
    session = subprocess.Popen(['python3', f'stats/stats.py', f'stats/{my_color}/{i}', f'{my_color}'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    print(stdout.decode(), flush=True)

    

