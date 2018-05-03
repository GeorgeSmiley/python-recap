
import player
import field

f = field.FootballField()

threads = []

for x in range(10):
    newthread = player.Player(0, f)
    threads.append(newthread)
    newthread.start()

for x in range(10):
    newthread = player.Player(1, f)
    threads.append(newthread)
    newthread.start()
