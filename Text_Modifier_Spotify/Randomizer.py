import random

o = open('Output.txt', 'w')
f = open('Songs.txt')
songs_list = []
with f as file_handle:
    for line in file_handle:
        songs_list.append(line)

for i in songs_list:
    if '\n' not in i:
        songs_list[songs_list.index(i)] = i + '\n'

print("Shuffle = 's' , Done: 'd'")
inp = input()
while inp != 'd':
    random.shuffle(songs_list)
    inp = input()

for i in songs_list:
    o.write(i)
