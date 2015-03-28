#This program is written by Uday Sagar Shiramshetty, studying 3rd year CSE, at MANIT-Bhopal
#It is written according to the python 3 syntax. Just run this program and follow the instructions 
#for encryption and decryption
#Any comments may be addressed to udaysagar.2177@gmail.com


s = [
		# S1
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S2
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S3
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S4
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S5
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S6
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S7
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

		# S8
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	]
p_box = [
		15, 6, 19, 20, 28, 11,
		27, 16, 0, 14, 22, 25,
		4, 17, 30, 9, 1, 7,
		23,13, 31, 26, 2, 8,
		18, 12, 29, 5, 21, 10,
		3, 24
	]
IP =    [       57, 49, 41, 33, 25, 17, 9,  1,
		59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5,
		63, 55, 47, 39, 31, 23, 15, 7,
		56, 48, 40, 32, 24, 16, 8,  0,
		58, 50, 42, 34, 26, 18, 10, 2,
		60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6
	]
FP =    [
		39,  7, 47, 15, 55, 23, 63, 31,
		38,  6, 46, 14, 54, 22, 62, 30,
		37,  5, 45, 13, 53, 21, 61, 29,
		36,  4, 44, 12, 52, 20, 60, 28,
		35,  3, 43, 11, 51, 19, 59, 27,
		34,  2, 42, 10, 50, 18, 58, 26,
		33,  1, 41,  9, 49, 17, 57, 25,
		32,  0, 40,  8, 48, 16, 56, 24
	]
C =     [
                 56, 48, 40, 32, 24, 16,  8,
		  0, 57, 49, 41, 33, 25, 17,
		  9,  1, 58, 50, 42, 34, 26,
		 18, 10,  2, 59, 51, 43, 35
        ]
D =     [
		 62, 54, 46, 38, 30, 22, 14,
		  6, 61, 53, 45, 37, 29, 21,
		 13,  5, 60, 52, 44, 36, 28,
		 20, 12,  4, 27, 19, 11,  3
        ]
exp_perm =  [
                31,  0,  1,  2,  3,  4,
		 3,  4,  5,  6,  7,  8,
		 7,  8,  9, 10, 11, 12,
		11, 12, 13, 14, 15, 16,
		15, 16, 17, 18, 19, 20,
		19, 20, 21, 22, 23, 24,
		23, 24, 25, 26, 27, 28,
		27, 28, 29, 30, 31,  0
            ]
comp_perm = [
                13, 16, 10, 23,  0,  4,
		 2, 27, 14,  5, 20,  9,
		22, 18, 11,  3, 25,  7,
		15,  6, 26, 19, 12,  1,
		40, 51, 30, 36, 46, 54,
		29, 39, 50, 44, 32, 47,
		43, 48, 38, 55, 33, 52,
		45, 41, 49, 35, 28, 31
            ]
to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
hex_to_bin = {v:k for k, v in to_hex.items()}
get_row = {'00': 0, '01': 1, '10': 2, '11': 3}
get_column = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, '0100': 4, '0101': 5, '0110': 6, '0111': 7, '1000': 8, '1001': 9, '1010': 10, '1011': 11, '1100': 12, '1101': 13, '1110': 14, '1111': 15}
to_binary = []
text_bits = []
key = []
keys = []
CD = []
block = []
left_block = []
right_block = []
bin_to_text = {}

def precompute():
    global to_binary, bin_to_text

    # for calculation of 8-bit list for every character
    for n in range(128):
        b = [0,0,0,0,0,0,0,0]
        for i in range(0, 8):
            if(n%2):
                b[7-i]=1
            n=n//2
        to_binary.append(b)

    # for calculation of char from string of 8-bits
    k = 0
    bin_to_text = {}
    for i in to_binary:
        string = ''
        for j in i:
            string += str(j)
        bin_to_text[string] = chr(k)
        k += 1

    return


#plain text to binary

def get_bits(plaintext):
    global to_binary
    global text_bits
    for i in plaintext:
        text_bits.extend(to_binary[ord(i)])
    return

#input permutaion

def apply_IP():
    global FP, block
    dummy = []
    dummy.extend(block)
    for i in range(0, 64):
        dummy[i] = block[(IP[i])]
    block = []
    block.extend(dummy)
    return

#final permutaion

def apply_FP():
    global FP, block
    dummy = []
    dummy.extend(block)
    for i in range(0, 64):
        dummy[i] = block[(FP[i])]
    block = []
    block.extend(dummy)
    return

#exapansion permutation to expand 32 bit block into 48 bit block

def expansion_permutation():
    global right_block, exp_perm
    dummy = []
    for i in range(48):
        dummy.append(right_block[exp_perm[i]])
    right_block = []
    for i in range(0, 48, 6):
        j = i+6
        right_block.append(dummy[i:j])
    return

#s-box function to reduce 48 bit block to 32 bit block

def s_boxfunc():
    global s, right_block, to_binary, get_row, get_column
    for i in range(0, 8):
        row = str(right_block[i][0])+str(right_block[i][-1])
        column = ''
        for j in range(1, 5):
            column = column+str(right_block[i][j])
        a = 16 * get_row[row]
        a += get_column[column]
        right_block.pop(i)
        right_block.insert(i, to_binary[ord(chr(s[i][a]))])
    dummy = []
    for i in right_block:
        dummy.extend(i[4:8])
    right_block = []
    right_block.extend(dummy)
    return

#p-box permutation

def p_boxfunc():
    global right_block, p_box
    dummy = []
    dummy.extend(right_block)
    for i in range(32):
    	dummy[i] = right_block[p_box[i]]
    right_block = []
    right_block.extend(dummy)
    return

#iterating code for the 16 rounds

def rounds():
    global right_block, left_block, keys
    for j in range(0, 16):
        d9 = []
        d9.extend(right_block)
        expansion_permutation()
        for i in range(0, 8):
            di = i*6
            for k in range(0, 6):
                right_block[i][k] ^= keys[j][di+k]
        s_boxfunc()
        p_boxfunc()
        for i in range(0, 32):
            right_block[i] ^= left_block[i]

        left_block = []
        left_block.extend(d9)
    return

#Heart of the program : DES algorithm

def DES(start, end):
    global block, left_block, right_block, text_bits
    block = []
    for i in range(start, end):
        block.append(text_bits[i])

    apply_IP()

    left_block = []
    right_block = []
    left_block.extend(block[0:32])
    right_block.extend(block[32:64])

    rounds()

    block = []
    block.extend(right_block)
    block.extend(left_block)

    apply_FP()

    cipher_block = ''
    for i in block:
        cipher_block += str(i)
    return cipher_block

#left shifting according to the present round number

def left_shift(times):
    global C, D
    for i in range(times):
        C.append(C.pop(0))
        D.append(D.pop(0))
    return

# selection of bits to form the key

def key_permutation():
    global CD, comp_perm, keys
    dummy = []
    for i in range(48):
        dummy.append(CD[comp_perm[i]])
    keys.append(dummy)
    return

# key generation

def generate_keys():
    global CD
    for i in range(28):
        C[i] = key[C[i]]
    for i in range(28):
        D[i] = key[D[i]]
    for i in range(0, 16):
        if(i==0 or i==1 or i==8 or i==15):
            left_shift(1)
        else:
            left_shift(2)
        CD = []
        CD.extend(C)
        CD.extend(D)
        key_permutation()
    return

#adding bits to make an integer number of 64-bit blocks
def apply_pads():
    global text_bits
    no_of_pads = len(text_bits) % 64
    if(no_of_pads):
        for i in range(64-no_of_pads):
            text_bits.append(0)
    return


#main function

def main():
    global text_bits, key, to_binary, bin_to_text, to_hex
    precompute()

    print('Enter the choice')
    print('1. ENCRYPT A MESSAGE')
    print('2. DECRYPT A MESSAGE')
    choice = int(input())

    print('Enter the key')
    keytext = str(input())
    for i in keytext:
        key.extend(to_binary[ord(i)])
    generate_keys()

    if(choice == 1):
        print('Enter the message(in Text-form)')
        plaintext = str(input())
        get_bits(plaintext)
        apply_pads()

        final_cipher = ''
        for i in range(0, len(text_bits), 64):
            final_cipher += DES(i, (i+64))

        # conversion of binary cipher into hex-decimal form
        hex_cipher = ''
        i = 0
        while i < len(final_cipher):
            hex_cipher += to_hex[final_cipher[i:i+4]]
            i = i+4

        print('the cipher is(in hex-decimal form)')
        print(hex_cipher)

    else:
        print('Enter the message(in hex-decimal form)')
        cipher = str(input())
        text_bits = []
        ciphertext = ''
        for i in cipher:
            ciphertext += hex_to_bin[i]         #conversion of hex-decimal form to binary form
        for i in ciphertext:
            text_bits.append(int(i))
        apply_pads()

        keys.reverse()
        bin_mess = ''
        for i in range(0, len(text_bits), 64):
            bin_mess += DES(i, (i+64))

        i = 0
        text_mess = ''
        while i < len(bin_mess):
            text_mess += bin_to_text[bin_mess[i:i+8]]
            i = i+8

        print('the original text is')
        print(text_mess)

    print('exiting...')
    return

main()

