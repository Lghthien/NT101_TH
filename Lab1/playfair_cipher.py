import re

# Xử lý văn bản khóa và tạo ma trận 5x5
def create_playfair_matrix(key):
    key = re.sub(r'[^A-Za-z]', '', key).upper().replace('J', 'I')  # Loại bỏ ký tự không phải chữ cái, đổi J thành I
    matrix = []
    used_chars = set()

    for char in key:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Không có J trong ma trận Playfair
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

# In ma trận Playfair
def print_playfair_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

# Xử lý văn bản thuần thành các cặp cho mã hóa
def preprocess_text(text):
    text = re.sub(r'[^A-Za-z]', '', text).upper().replace('J', 'I')  # Loại bỏ ký tự không phải chữ cái
    processed_text = ''
    
    i = 0
    while i < len(text):
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += 'X'  # Thêm 'X' giữa các chữ cái trùng nhau
        elif i + 1 < len(text):
            processed_text += text[i + 1]
            i += 1
        else:
            processed_text += 'X'  # Thêm 'X' nếu chữ cái cuối cùng không có cặp

        i += 1

    return processed_text

# Tìm vị trí của một ký tự trong ma trận
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

# Mã hóa hoặc giải mã cặp ký tự
def process_pair(matrix, char1, char2, mode='encrypt'):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:  # Cùng hàng
        if mode == 'encrypt':
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        else:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Cùng cột
        if mode == 'encrypt':
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # Hình chữ nhật
        return matrix[row1][col2] + matrix[row2][col1]

# Mã hóa hoặc giải mã văn bản
def playfair_cipher(matrix, text, mode='encrypt'):
    text = preprocess_text(text)
    processed_text = ''

    for i in range(0, len(text), 2):
        processed_text += process_pair(matrix, text[i], text[i + 1], mode) + ' '

    return processed_text

def main():
    print("Playfair Cipher")
    choice = input("Enter 1 to Encrypt, 2 to Decrypt: ")

    key = input("Enter the key: ")
    matrix = create_playfair_matrix(key)
    
    print("\nPlayfair Matrix:")
    print_playfair_matrix(matrix)

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        ciphertext = playfair_cipher(matrix, plaintext, mode='encrypt')
        print("\nEncrypted Text:", ciphertext)
    elif choice == '2':
        ciphertext = input("Enter the ciphertext: ")
        plaintext = playfair_cipher(matrix, ciphertext, mode='decrypt')
        print("\nDecrypted Text:", plaintext)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
