# Abjad plaintext
pattern = "KRYPTOSABCDEFGHIJLMNQUVWXZ"

# Kata kunci "ABSCISSA"
keyword = "ABSCISSA"

# Membuat tabel Vigenère custom
kryptos_table = []
for k in range(len(keyword)):
    row = []
    start_index = pattern.index(keyword[k])
    for i in range(len(pattern)):
        row.append(pattern[(start_index + i) % len(pattern)])
    kryptos_table.append(row)

# Mencetak array plaintext
print("Array Plaintext:")
formatted_pattern = ' '.join(pattern)
print(formatted_pattern)

# Mencetak tabel Vigenère
print("\nTabel Vigenère:")
for row in kryptos_table:
    print(" ".join(row))

def decrypt(encrypted_message, keyword):
    dec_text = ""
    keyword_len = len(keyword)
    encrypted_message = encrypted_message.replace(" ", "")
    keyword_index = 0
    count = 0

    for i, char in enumerate(encrypted_message):
        char = char.upper()
        if char in pattern:
            row = keyword.index(keyword[keyword_index % keyword_len])
            col = kryptos_table[row].index(char)
            dec_char = pattern[col]
            dec_text += dec_char
            keyword_index += 1
            count += 1
        else:
            # Karakter khusus tetap dalam alur dekripsi
            dec_text += char

        if count == 5:
            count = 0

    return dec_text

# Pesan yang akan dienkripsi
pesan = "VFPJU DEEHZ WETZY VGWHK KQETG FQJNC EGGWH KK?"

# Mendekripsi pesan
pesan_terdekripsi = decrypt(pesan, keyword)
print("Pesan Terdekripsi:", pesan_terdekripsi)