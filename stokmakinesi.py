import tkinter as tk
import time

stok1_value = 1
stok2_value = 1

def stok1_ekle():
    global stok1_value
    stok1_value += 1
    text.delete('1.0', tk.END)
    text.insert(tk.END, stok1_value)

def stok1_cikar():
    global stok1_value
    stok1_value -= 1
    text.delete('1.0', tk.END)
    text.insert(tk.END, stok1_value)

def stok2_ekle():
    global stok2_value
    stok2_value += 1
    an.delete('1.0', tk.END)
    an.insert(tk.END, stok2_value)

def stok2_cikar():
    global stok2_value
    stok2_value -= 1
    an.delete('1.0', tk.END)
    an.insert(tk.END, stok2_value)

def save_data():
    global stok1_value, stok2_value
    stok1_value = int(text.get("1.0", tk.END))
    stok2_value = int(an.get("1.0", tk.END))
    with open("stok.txt", "w") as f:
        f.write(f"{stok1_value}\n{stok2_value}")

root = tk.Tk()
root.title("Stok Makinesi")
root.geometry('500x200')
root.config(background="black")

button3 = tk.Button(root, text="Stok 1 Ekle", command=stok1_ekle, bg="green", font="Sans", width="10")
button3.pack()
button3.place(x=-5 , y=-1)
button4 = tk.Button(root, text="Stok 1 Çıkar", command=stok1_cikar, bg="green", font="Sans", width="10")
button4.pack()
button4.place(x=100 , y=-1)
text = tk.Text(root, width=22, height=1, background="green",font="Sans")
text.insert(tk.END, stok1_value)
text.pack()
text.place(x=-1 , y=31)

button1= tk.Button(root, text="Stok 2 Ekle", command=stok2_ekle, bg="green", font="Sans", width="10")
button1.pack()
button1.place(x=-5 , y=50)
button2 = tk.Button(root, text="Stok 2 Çıkar", command=stok2_cikar, bg="green", font="Sans", width="10")
button2.pack()
button2.place(x=100 , y=50)
save_button = tk.Button(root, text="Kaydet", command=save_data, bg="green")
save_button.pack()
save_button.place(x=210, y=25)

an = tk.Text(root, width=22, height=1, background="green",font="Sans")
an.insert(tk.END, stok2_value)
an.pack()
an.place(x=-1, y=80)

try:
    with open("stok.txt", "r") as f:
        stok1_value, stok2_value = map(int, f.readlines()) # eski değerleri okur

except FileNotFoundError:
    # eğer dosya yoksa veya çalışmazsa değerleri otomatik normal belirler
    pass

root.mainloop()

## Koddaki Hiçbirşey ellenmemeli ellenirse bozulabilir 
## Devamı gelebilir fakat bunu ben burada yapamam şuan çünkü stoklar sizin stoğunuz 
