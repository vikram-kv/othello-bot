import sys

if (len(sys.argv) < 3):
    print("[Usage]: python3 stats.py <input_file> <your_bot_color>", flush=True)
    sys.exit(0)
file_name = sys.argv[1]
my_color = str(sys.argv[2])
f = open(f'{file_name}', 'r')
other_color = ''
if my_color.lower() == 'red':
    my_color = 'Red'
    other_color = 'Black'
elif my_color.lower() == 'black':
    my_color = 'Black'
    other_color = 'Red'
else:
    print("Invalid color",flush=True)
    sys.exit(0)
wins = 0
total = 0
for line in f.readlines():
    if (line[:5] == "[Win]"):
        s = line.split(':')[1].strip()
        if (s.lower() == my_color):
            wins += 1
        total += 1
if(total==1):
    if wins>0:
        print(f'[Win ]: {my_color}', flush=True)
    else:
        print(f'[Win ]: {other_color}', flush=True)
elif total>0:
    print(f'[STATS] {my_color} won {wins} matches out of {total}', flush=True)
else:
    print(f'No winner')
f.close()
