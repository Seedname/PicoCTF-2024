import dis

input_list = [0] * 40
input_list[0] = 4
input_list[1] = 54
input_list[2] = 41
input_list[3] = 0
input_list[4] = 112
input_list[5] = 32
input_list[6] = 25
input_list[7] = 49
input_list[8] = 33
input_list[9] = 3
input_list[10] = 0
input_list[11] = 0
input_list[12] = 57
input_list[13] = 32
input_list[14] = 108
input_list[15] = 23
input_list[16] = 48
input_list[17] = 4
input_list[18] = 9
input_list[19] = 70
input_list[20] = 7
input_list[21] = 110
input_list[22] = 36
input_list[23] = 8
input_list[24] = 108
input_list[25] = 7
input_list[26] = 49
input_list[27] = 10
input_list[28] = 4
input_list[29] = 86
input_list[30] = 43
input_list[31] = 108
input_list[32] = 122
input_list[33] = 14
input_list[34] = 2
input_list[35] = 71
input_list[36] = 62
input_list[37] = 115
input_list[38] = 88
input_list[39] = 78

key_str = 'J'
key_str = key_str + '_'
key_str = key_str + 'o'
key_str = key_str + '3'
key_str = key_str + 't'

key_list = [ord(char) for char in key_str]

while len(key_list) < len(input_list):
    key_list.extend(key_list)

result = [a ^ b for a, b in zip(input_list, key_list) if 31 <= a ^ b < 128]
print(list(map(chr, result)))
result_text = ''.join(map(chr, result))
print(result_text)
