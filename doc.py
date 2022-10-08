import subprocess


outfile = "black.txt"
f = open(outfile,'w')
g = open('red.txt', 'w')

runs = 100
# for i in range(50):

#     # Play as Black
#     print(f'Playing as Black with {i}.so ...',end="\t")
#     proc = subprocess.Popen(['./bin/Desdemona', './so_bots/50.so', f'./so_bots/{i}.so'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
#     stdout, stderr = proc.communicate()
#     print('Game Over')
#     with open(outfile, 'a') as f:
#         f.write(stdout.decode())    

for i in range(50):
    # Play as Red
    print(f'Playing as Red with {i}.so ...',end="\t")
    proc = subprocess.Popen(['./bin/Desdemona', f'./so_bots/{i}.so', './so_bots/50.so'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    stdout, stderr = proc.communicate()
    print('Game Over')
    
    with open('red.txt', 'a') as g:
        g.write(stdout.decode())

f.close()
g.close()
