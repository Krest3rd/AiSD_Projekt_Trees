from math import log2,floor

for i in range(2000):
    if floor(log2(i+1)) != (i+1).bit_length()-1:
        print(floor(log2(i+1))," = ",(i+1).bit_length()-1, i)