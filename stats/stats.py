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

figures = ''
flag = False
for line in f.readlines():
    if (line.find(f'Win') != -1 or line.find('Draw') != -1 or line.find('Timeout') != -1):
        flag = True
    if flag:
        figures += line

print('\n'+figures)
f.close()
