text = open('input.txt', 'r')
signal = ''

for i in text:
    signal += i

for i in range(len(signal)):
    bits = set(signal[i:i+4])
    if len(bits) == 4:
        print(i+4)
        break