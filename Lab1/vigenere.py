def vigenere_encrypt(plaintext, key):
    # Hàm này mã hóa văn bản đầu vào (plaintext) bằng khóa (key) sử dụng thuật toán Vigenère

    # Lọc bỏ các ký tự không phải chữ cái và chuyển mọi ký tự thành chữ hoa
    plaintext = ''.join(filter(str.isalpha, plaintext)).upper() #Hàm isalpha() dùng để kiểm tra chuỗi có phải là chữ cái không
    key = key.upper()  # Cho phép nhập khóa bằng chữ thường và hàm này dùng để chuyển khóa thành chữ hoa

    encrypted = []  # Danh sách để lưu trữ các ký tự đã mã hóa
    key_length = len(key)  # Đo chiều dài của khóa

    for i, char in enumerate(plaintext):  # Duyệt từng ký tự trong plaintext
        if char.isalpha():  # Chỉ xử lý ký tự chữ cái
            p = ord(char) - ord('A')  # Tính giá trị số cho ký tự văn bản (A=0, B=1, ..., Z=25)
            k = ord(key[i % key_length]) - ord('A')  # Tính giá trị số cho ký tự khóa (lặp lại nếu cần)
            c = (p + k) % 26  # Áp dụng công thức mã hóa Vigenère
            encrypted.append(chr(c + ord('A')))  # Chuyển giá trị số trở lại ký tự và thêm vào danh sách
        else:
            encrypted.append(char)  # Nếu không phải ký tự chữ cái, thêm vào danh sách như cũ

    return ''.join(encrypted)  # Kết hợp các ký tự đã mã hóa thành một chuỗi và trả về


def vigenere_decrypt(ciphertext, key):
    # Hàm này giải mã văn bản đầu vào (ciphertext) bằng khóa (key) sử dụng thuật toán Vigenère

    # Lọc bỏ các ký tự không phải chữ cái và chuyển mọi ký tự thành chữ hoa
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    key = key.upper()  # Chuyển khóa thành chữ hoa

    decrypted = []  # Danh sách để lưu trữ các ký tự đã giải mã
    key_length = len(key)  # Đo chiều dài của khóa

    for i, char in enumerate(ciphertext):  # Duyệt từng ký tự trong ciphertext
        if char.isalpha():  # Chỉ xử lý ký tự chữ cái
            c = ord(char) - ord('A')  # Tính giá trị số cho ký tự cipher (A=0, B=1, ..., Z=25)
            k = ord(key[i % key_length]) - ord('A')  # Tính giá trị số cho ký tự khóa (lặp lại nếu cần)
            p = (c - k + 26) % 26  # Áp dụng công thức giải mã Vigenère (cộng 26 để tránh giá trị âm)
            decrypted.append(chr(p + ord('A')))  # Chuyển giá trị số trở lại ký tự và thêm vào danh sách
        else:
            decrypted.append(char)  # Nếu không phải ký tự chữ cái, thêm vào danh sách như cũ

    return ''.join(decrypted)  # Kết hợp các ký tự đã giải mã thành một chuỗi và trả về


if __name__ == "__main__":
    action = input("Bạn muốn (E)ncrypt hay (D)ecrypt? ").strip().upper()  # Cho phép nhập chữ thường sau đó hàm upper() sẽ tự chuyển thành chữ in hoa
    key = input("Nhập khóa: ")  

    if action == 'E':  
        plaintext = input("Nhập văn bản cần mã hóa: ") 
        encrypted_message = vigenere_encrypt(plaintext, key)  # Gọi hàm mã hóa
        print(f"Văn bản đã mã hóa: {encrypted_message}")  # In ra văn bản đã mã hóa

    elif action == 'D': 
        ciphertext = input("Nhập văn bản cần giải mã: ")  
        decrypted_message = vigenere_decrypt(ciphertext, key)  # Gọi hàm giải mã
        print(f"Văn bản đã giải mã: {decrypted_message}")  # In ra văn bản đã giải mã

    else:
        print("Hành động không hợp lệ. Vui lòng chọn 'E' hoặc 'D'.")  