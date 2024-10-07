def caesar_cipher(text, key, choice):
    result = ""
    if choice == "1":  # Mã hóa
        for char in text:
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
    elif choice == "2":  # Giải mã
        for char in text:
            if char.isupper():
                result += chr((ord(char) - key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += char
    return result

# attach the key
def attack_all_keys(code):
    print("Kết quả tấn công tất cả các mã khóa có thể:")
    for key in range(1, 26):
        result = caesar_cipher(code, key, "2")
        print(f"Key = {key}: {result}")

# input information
key = int(input("Vui lòng nhập key: "))
code = input("Vui lòng nhập mã khóa: ")

# choice the 
print("1. Mã hóa \n2. Giải mã \n3. Tấn công tất cả mã khóa")
choice = input("Vui lòng chọn: ")

while choice not in ["1", "2", "3"]:
    choice = input("Vui lòng nhập lại lựa chọn: ")

# Thực hiện mã hóa, giải mã hoặc tấn công
if choice == "3":
    attack_all_keys(code)
else:
    result = caesar_cipher(code, key, choice)
    print("Kết quả:", result)
