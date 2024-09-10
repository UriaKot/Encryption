import secrets
import tkinter as tk
from tkinter import messagebox

def encrypt_text():
    """
    Шифрует текст, используя случайный ключ.
    """
    global key
    text = input_text.get("1.0", tk.END).strip()
    encrypted_text = "".join(chr(ord(c) ^ key) for c in text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt_text():
    """
    Расшифровывает текст, используя сохраненный ключ.
    """
    global key
    encrypted_text = output_text.get("1.0", tk.END).strip()
    decrypted_text = "".join(chr(ord(c) ^ key) for c in encrypted_text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

def generate_key():
    """
    Генерирует случайный ключ.
    """
    global key
    key = secrets.randbelow(256)
    messagebox.showinfo("Ключ", f"Сгенерирован новый ключ: {key}")

# Создание окна приложения
root = tk.Tk()
root.title("Шифрование")

# Настройка элементов интерфейса
label_input = tk.Label(root, text="Введите текст:")
label_input.pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

label_output = tk.Label(root, text="Зашифрованный текст:")
label_output.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Кнопки
button_encrypt = tk.Button(root, text="Зашифровать", command=encrypt_text)
button_encrypt.pack()

button_decrypt = tk.Button(root, text="Расшифровать", command=decrypt_text)
button_decrypt.pack()

button_generate_key = tk.Button(root, text="Сгенерировать ключ", command=generate_key)
button_generate_key.pack()

# Запускаем цикл обработки событий
root.mainloop()