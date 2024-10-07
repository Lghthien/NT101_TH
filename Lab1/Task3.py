from collections import Counter
import re
import matplotlib.pyplot as plt
import pandas as pd

def count_letter_frequency(text):
    # Lọc ra tất cả các chữ cái từ văn bản và chuyển về chữ thường
    letters = re.findall(r'[a-zA-Z]', text.lower())
    letter_frequency = Counter(letters)
    return letter_frequency

def encode_text(text, mapping):
    # Mã hóa văn bản theo ánh xạ cho trước
    encoded_text = ''.join(mapping.get(char, char) for char in text)
    return encoded_text

# Đọc dữ liệu từ file
file_path = r"D:\Sukem\Nam3\AT_MMT\ThucHanh\Lab01\3_1_cipher_text.txt"

with open(file_path, "r") as file:
    text = file.read()

# Thống kê tần số chữ cái trong văn bản từ file
frequency = count_letter_frequency(text)

# Tính tổng số ký tự
total_letters = sum(frequency.values())

# Tạo danh sách các chữ cái và tần suất tương ứng
letters = list(frequency.keys())
frequencies = [frequency[letter] for letter in letters]

# Sắp xếp theo tần suất tăng dần
sorted_freqs = sorted(zip(frequencies, letters), key=lambda x: x[0])
sorted_letters = [letter for freq, letter in sorted_freqs]
sorted_frequencies = [freq for freq, letter in sorted_freqs]
percentages = [(count / total_letters) * 100 for count in sorted_frequencies]


english_frequency = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.70, 'f': 2.2,
    'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 'k': 0.8, 'l': 4.0,
    'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 'q': 0.10, 'r': 6.0,
    's': 6.3, 't': 9.1, 'u': 2.8, 'v': 0.10, 'w': 2.3, 'x': 0.10,
    'y': 2.0, 'z': 0.1
}

# Sắp xếp tần suất chuẩn của tiếng Anh
english_letters = list(english_frequency.keys())
english_frequencies = list(english_frequency.values())

sorted_english_letters = [letter for _, letter in sorted(zip(english_frequencies, english_letters))]
sorted_english_frequencies = sorted(english_frequencies)

# Tính tỷ lệ phần trăm tần suất chuẩn
english_percentages = sorted_english_frequencies

# Tạo ánh xạ từ cipher sang tiếng Anh
mapping = dict(zip(sorted_letters, sorted_english_letters))

# Mã hóa văn bản
encoded_text = encode_text(text.lower(), mapping)

# Xuất ra văn bản đã mã hóa
print("\nVăn bản đã mã hóa:")
print(encoded_text)


# Tạo bảng ánh xạ
mapping_df = pd.DataFrame(list(mapping.items()), columns=['Cipher Letter', 'English Letter'])
mapping_df['Cipher Frequency (%)'] = [(frequency[char] / total_letters) * 100 for char in mapping_df['Cipher Letter']]
mapping_df['English Frequency (%)'] = [english_frequency[char] for char in mapping_df['English Letter']]

# Xuất bảng ánh xạ
print("\nBảng ánh xạ giữa các chữ cái trong văn bản cipher và tiếng Anh:")
print(mapping_df)

# Vẽ biểu đồ tần suất chữ cái của văn bản (tùy chọn)
plt.figure(figsize=(14, 6))

# Biểu đồ cho văn bản cipher
plt.subplot(1, 2, 1)
plt.bar(sorted_letters, percentages, color='gray')
plt.xlabel('Letter')
plt.ylabel('Frequency (%)')
plt.title('Tần suất (%) của các chữ cái trong văn bản cipher (tăng dần)')
for i, v in enumerate(percentages):
    plt.text(i, v + 0.5, f'{v:.2f}', ha='center')

# Biểu đồ cho tần suất tiếng Anh
plt.subplot(1, 2, 2)
plt.bar(sorted_english_letters, english_percentages, color='blue')
plt.xlabel('Letter')
plt.ylabel('Frequency (%)')
plt.title('Tần suất (%) của các chữ cái trong tiếng Anh (tăng dần)')
for i, v in enumerate(english_percentages):
    plt.text(i, v + 0.5, f'{v:.2f}', ha='center', fontsize=8)

plt.tight_layout()
plt.show()