from tkinter import *
from tkinter import messagebox
import Encryption

FONT = ("arial", 12, "normal")

#window
window = Tk()
window.title("Secret Notes")
window.minsize(width=300, height=600)
window.config(padx=10, pady=10)



'''***************Fonksiyonlar***************'''
def write_file_encode():
    if(entry_enter_title.get().strip() != "" and text_enter_secret.get("1.0", END).strip() != "" and entry_enter_key.get().strip() != ""):
        if(entry_enter_key.get().strip() == "deneme"):
            encrypted = Encryption.encode(text_enter_secret.get("1.0", END).strip().lower())
            with open("kayitlar.txt", mode="a", encoding="utf-8") as islemler:
                islemler.write(entry_enter_title.get() + "\n")
                islemler.write(encrypted + "\n")

            entry_enter_title.delete("0", END)
            text_enter_secret.delete("1.0", END)
            entry_enter_key.delete("0", END)
        else:
            messagebox.showwarning("Error", "Şifre hatalı.")
    else:
        messagebox.showwarning("Error", "Lütfen kutucukları boş bırakmayınız.")
def write_file_decode():
    if( text_enter_secret.get("1.0", END).strip() != ""):
        if(entry_enter_key.get().strip() == "deneme"):
            decrypted = Encryption.decode(text_enter_secret.get("1.0", END).strip())
            text_enter_secret.delete("1.0", END)
            entry_enter_key.delete("0", END)
            text_enter_secret.insert(1.0, decrypted)
        else:
            messagebox.showwarning("Error", "Şifre hatalı.")
    else:
        messagebox.showwarning("Error", "Lütfen şifrelenmiş mesajı giriniz.")
'''***************Fonksiyonlar***************'''



'''***************Arayüz Tasarimi***************'''
#image
image = PhotoImage(file="topsecret.png")
panel = Label(window, image=image)
panel.pack(pady=40)

#enter title label
label_enter_title = Label(text="Enter your title", font=FONT)
label_enter_title.pack(pady=3)

#enter title entry
entry_enter_title = Entry(width=40)
entry_enter_title.pack(pady=3)

#enter your secret label
label_enter_secret = Label(text="Enter your secret", font=FONT)
label_enter_secret.pack(pady=3)

#enter your secret textbox
text_enter_secret = Text(width=40, height=10)
text_enter_secret.pack(pady=3)

#enter master key label
label_enter_key = Label(text="Enter master key", font=FONT)
label_enter_key.pack(pady=3)

#enter master key entry
entry_enter_key = Entry(width=40, show="*")
entry_enter_key.pack(pady=3)

#save encrypt button
button_save = Button(text="Save & Encrypt", command=write_file_encode)
button_save.config(pady=5, padx=5)
button_save.pack(pady=3)

#decrypt button
button_decrypt = Button(text="Decrypt", command=write_file_decode)
button_decrypt.config(pady=5, padx=5)
button_decrypt.pack(pady=3)

'''***************Arayüz Tasarimi***************'''


window.mainloop()
