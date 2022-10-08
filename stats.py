import sys

if (len(sys.argv) < 3):
    print("[Usage]: python3 stats.py <input_file> <your_bot_color>")
    sys.exit(0)
file_name = sys.argv[1]
my_color = sys.argv[2]

f = open(f'{file_name}', 'r')
wins = 0
total = 0
for line in f.readlines():
    if (line[:5] == "[Win]"):
        s = line.split(':')[1].strip()
        if (s == my_color):
            wins += 1
        total += 1
print(f'{my_color} won {wins} matches out of {total}')
f.close()
