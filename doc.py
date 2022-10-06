import subprocess


outfile = "RESULTSRED.txt"
f = open(outfile,'w')
f.close()

runs = 100
for _ in range(100):
    proc = subprocess.Popen(['./bin/Desdemona', './bots/RandomBot/RandomBot.so', './bots/MyBot/bot.so'], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    stdout, stderr = proc.communicate()
    
    with open(outfile, 'a') as f:
        f.write(stdout.decode())
