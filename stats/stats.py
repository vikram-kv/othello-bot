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
loss = 0
for line in f.readlines():
    if (line.find(f'[Win]: {my_color}') != -1):
        wins = 1
    if (line.find(f'[Win]: {other_color}') != -1):
        loss = 1
if wins > 0:
    print(f'{my_color} WINS')
elif loss > 0:
    print(f'{other_color} WINS')
else:
    print('DRAW')

f.close()
