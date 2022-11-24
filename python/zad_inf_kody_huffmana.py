text = "tata ma tatarak i rak ma mak"
dict = {'i': '0000', 'r': '0001', 'k': '001', 'm': '110', 't': '111', ' ': '01', 'a': '10'}
bin_encoded = ''
ch_encoded = ''

# 1
for i in text:
    bin_encoded += dict[i]

# 2
for i in range(0,len(bin_encoded), 8):
    bin_number = '0b' + bin_encoded[i: i + 7] # Dzielenie na oktety i dodane prefiksu liczby binarnej
    dec_number = int(bin_number, 2)
    ch_encoded += chr(dec_number)

print(bin_encoded)
print(ch_encoded)