text = open('input2.txt', 'r')
signal = ''

for i in text:
    signal += i

for i in range(len(signal)):
    bits = set(signal[i:i+14])
    if len(bits) == 14:
        print(i+14)
        break