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

# Fungsi untuk mengenkripsi pesan
def encrypt(message, keyword):
    enc_text = ""
    keyword_len = len(keyword)
    message = message.replace(" ", "")
    keyword_index = 0
    count = 0

    for i, char in enumerate(message):
        char = char.upper()
        if char in pattern:
            row = keyword.index(keyword[keyword_index % keyword_len])
            col = pattern.index(char)
            enc_char = kryptos_table[row][col]
            enc_text += enc_char
            keyword_index += 1
            count += 1
        else:
            # Karakter khusus tetap dalam alur enkripsi
            enc_text += char

        if count == 5:
            enc_text += ' '
            count = 0

    return enc_text

# Pesan yang akan dienkripsi
pesan = "It was totally invisible Hows that possible? They used the Earths magnetic field X The information was gathered and transmitted undergruund to an unknown location X Does Langley know about this? They should Its buried out there somewhere X Who knows the exact location? Only WW This was his last message X Thirty eight degrees fifty seven minutes six point five seconds northSeventy seven degrees eight minutes forty four seconds west ID by rows"

# Mengenkripsi pesan
pesan_terenkripsi = encrypt(pesan, keyword)
print("Pesan Terenkripsi:", pesan_terenkripsi)