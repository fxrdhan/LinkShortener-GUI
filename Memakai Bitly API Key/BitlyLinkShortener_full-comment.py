# Import library tkinter untuk membuat GUI
import tkinter as tk
import tkinter.messagebox as messagebox 
# Import library requests untuk melakukan HTTP request ke API Bitly
import requests
#Import library pyperclip untuk meng-copy hasil link yang sudah disingkat ke clipboard
import pyperclip

# Buat variabel TOKEN dan masukkan token API bitly
TOKEN = "Masukkan token API Bitly akun anda disini"

#Buat fungsi untuk memendekkan link
def shorten_link(link):
    # Buat header dengan isi Authorization berisi token API
    headers = {"Authorization": f"Bearer {TOKEN}"}
    # Buat payload berisi link yang ingin dipendekkan
    payload = {"long_url": link}
    # Kirim POST request ke API bitly.com
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=payload, headers=headers)
    # Periksa apakah terdapat error dalam response
    response.raise_for_status()
    # Ubah data response menjadi format JSON dan ambil data link pendek
    data = response.json()
    return data["link"]

# Buat fungsi untuk memendekkan link dari semua entry yang diisi
def shorten_links():
    # Looping untuk setiap entry pada list entry_list
    for i in range(3):
        # Ambil link dari entry
        LINK = entry_list[i].get()
        # Jika link tidak kosong
        if LINK:
            try:
                # Coba untuk memendekkan link dengan fungsi shorten_link
                shortened_link = shorten_link(LINK)
                # Ubah text pada label result_list menjadi shortened_link dan ubah warna menjadi hijau
                result_list[i].config(text=shortened_link, fg="green", bg="black")
            except Exception:    # Jika terdapat error ketika memendekkan link
                # Ubah text pada label result_list menjadi "Link can't be shortened!" dan ubah warna menjadi merah
                result_list[i].config(text="Link can't be shortened!", fg="red", bg="black")

# Buat fungsi untuk menyalin hasil memendekkan link ke clipboard
def copy_to_clipboard(event):
    widget = event.widget
    # Ambil text dari widget
    result = widget.cget("text")
    if result:                  # Jika text tidak kosong
        # Salin text ke clipboard menggunakan library pyperclip
        pyperclip.copy(result)
        # Tampilkan messagebox yang memberitahu bahwa hasil berhasil disalin ke clipboard
        messagebox.showinfo("", "Shortened link has been copied to clipboard.")
   
# Buat fungsi untuk mereset hasil memendekkan link ke clipboard     
def reset_links():
    for i in range(3):
        entry_list[i].delete(0, 'end')
        result_list[i].config(text="", fg="white", bg="grey")

# Buat window interface 
window = tk.Tk()
window.title("Bitly Link Shortener")
window.configure(bg="black")
window.resizable(False,False)
label = tk.Label(window, text="@fxrdhan_", font=('arial', '8'),                                 
                 fg="magenta", bg="black")                                                    
label.place(relx=0, rely=1, anchor="sw")                                                      

# Buat list untuk menyimpan entry dan label hasil memendekkan link
entry_list = []
result_list = []

# Looping untuk membuat 5 entry dan label hasil memendekkan link
for i in range(3):
    # Buat label yang menunjukkan nomor link
    label = tk.Label(window, text=f"Link {i+1}:", fg="white", bg="black")
    label.grid(row=i, column=0, padx=5, pady=5)
    # Buat entry untuk memasukkan link
    entry = tk.Entry(window, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entry_list.append(entry)
    # Buat label untuk menampilkan hasil memendekkan link
    result = tk.Label(window, text="", fg="white", bg="grey", width=20, anchor="w")
    result.grid(row=i, column=2, padx=5, pady=5)
    result.bind("<Button-1>", copy_to_clipboard)
    result_list.append(result)

# Buat tombol untuk memendekkan semua link yang telah dimasukkan
button_shorten = tk.Button(window, text="Shorten Links", command=shorten_links,                 
                        bg="green", fg="white",                                          
                        font=("arial bold", "10"))                                       
button_shorten.grid(row=5, column=1, padx=5, pady=5, columnspan=1)    
                                               
# Buat tombol untuk mereset semua link yang telah dimasukkan
button_reset = tk.Button(window, text="Reset Links", command=reset_links,                      
                        bg="red", fg="white",                                             
                        font=("arial bold italic", "10"))                                       
button_reset.grid(row=5, column=2, padx=5, pady=5, columnspan=1)                               

# Loop untuk menjalankan GUI
window.mainloop()
