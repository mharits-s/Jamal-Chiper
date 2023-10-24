# Abjad plaintext
plaintext_alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ"

# Kata kunci "ABSCISSA"
keyword = "ABSCISSA"

# Membuat tabel Vigenère custom
vigenere_table = []
for k in range(len(keyword)):
    row = []
    start_index = plaintext_alphabet.index(keyword[k])
    for i in range(len(plaintext_alphabet)):
        row.append(plaintext_alphabet[(start_index + i) % len(plaintext_alphabet)])
    vigenere_table.append(row)

# Mencetak array plaintext
print("Array Plaintext:")
formatted_plaintext = ' '.join(plaintext_alphabet)
print(formatted_plaintext)

# Mencetak tabel Vigenère
print("\nTabel Vigenère:")
for row in vigenere_table:
    print(" ".join(row))
