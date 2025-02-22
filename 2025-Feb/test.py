# Ordering of words could be wrong
rw1 = "ADMIRERS"
rw2 = "ASTIR"
rw3 = "BLACK"
rw4 = "DITHER"
rw5 = "DRINK"
rw6 = "HOAGIES"
rw7 = "JOLTS"
rw8 = "OKRA"
rw9 = "PREMISE"
rw10 = "STICKERS"
rw11 ="SURFACED"
rw12 ="SWARM"
rw13 ="WILTS"
rw14 ="WRAP"
bw1 = "ARK"
bw2 ="CHILDRENS"
bw3 ="CUIRASS"
bw4 ="FOR"
bw5 ="HOE"
bw6 ="ISOMER"
bw7 ="LANE"
bw8 ="LORDS"
bw9 ="NOCTURNES"
bw10 ="RIDDLE"
bw11 ="SAT"
bw12 ="SOLE"
bw13 ="TRIONYM"
bw14 ="TROPE"

'''
1r on the 6r
2b 4b
5r 11r on the 11b 12b 
The 10b 5b 3b 
7b of the 13b 6b 
... and the 3r 1b 
4r 9r 
13r 8r 
10r 14b 
2r 12r 
8b of the 14r 
7r of a 9b 
'''

sum = 0
for i in range(len(rw1)):
    print(ord(rw1[i]) - 64, rw1[i])
    sum += ord(rw1[i]) - 64

bsum = 0
for i in range(len(bw1)):
    print(ord(bw1[i]) - 64, bw1[i])
    bsum += ord(bw1[i]) - 64

print(sum, bsum)




