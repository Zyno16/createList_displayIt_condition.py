import os
files = [f for f in os.listdir("zino.3.txt") if os.path.isfile("zino.3.txt/" + f)]
for file in files:
    print(file)
