import tkinter as tk                                                                            # impor modul tkinter sebagai "tk"
import tkinter.messagebox as messagebox                                                         # impor modul messagebox dari tkinter sebagai "messagebox"
import requests                                                                                 # impor modul requests untuk mengirim permintaan HTTP
import pyperclip                                                                                # impor modul pyperclip untuk mengakses clipboard sistem

TOKEN = "Masukkan token API Cuttly akun anda disini"                                            # token API Cuttly yang akan digunakan untuk memendekkan link

def shorten_link(link):                                                                         # buat fungsi untuk memendekkan link
    payload = {'key': TOKEN, 'short': link}                                                     # payload dengan token API Cuttly dan link yang akan dipendekkan
    response = requests.get('https://cutt.ly/api/api.php', params=payload)                      # kirim permintaan GET ke API Cuttly dengan payload
    data = response.json()                                                                      # baca respon JSON dari permintaan
    if data['url']['status'] == 7:                                                              # jika status respon adalah 7, artinya link berhasil dipendekkan
        return data['url']['shortLink']                                                         # kembalikan link yang telah dipendekkan
    else:
        raise Exception('Link cannot be shortened!')                                            # jika terjadi kesalahan pada saat memendekkan link, raise exception

def shorten_links():                                                                            # buat fungsi untuk memendekkan beberapa link sekaligus
    for i in range(3):                                                                          # lakukan iterasi sebanyak 5 kali
        link = entry_list[i].get()                                                              # baca link yang diinputkan pada kotak teks ke-i
        if link:                                                                                # Jika link tidak kosong
            try:                                                                                # coba memendekkan link
                shortened_link = shorten_link(link)                                             # pendekkan link dengan fungsi "shorten_link"
                result_list[i].config(text=shortened_link, fg="green", bg="black")              # tampilkan link yang telah dipendekkan pada kotak teks hasil
            except Exception:                                                                   # jika terjadi kesalahan pada saat memendekkan link
                result_list[i].config(text="Link can't be shortened!", fg="red", bg="black")    # tampilkan pesan error pada kotak teks hasil

def reset_links():                                                                              # buat fungsi untuk mereset beberapa link sekaligus
    for i in range(3):                                                                          # lakukan iterasi sebanyak 5 kali
        entry_list[i].delete(0, tk.END)                                                         # baca link yang dihapus pada kotak teks ke-i
        result_list[i].config(text="", bg="grey")                                               # kosongkan link seperti awal
        
def copy_to_clipboard(event):                                                                   # buat fungsi untuk menyalin link yang telah dipendekkan ke clipboard
    widget = event.widget                                                                       # ambil widget yang men-trigger event
    result = widget.cget("text")                                                                # ambil teks pada widget tersebut
    if result:                                                                                  # jika teks tidak kosong
        pyperclip.copy(result)                                                                  # salin teks ke clipboard sistem
        messagebox.showinfo("", "Shortened link has been copied to clipboard.")                 # tampilkan pesan konfirmasi bahwa link telah berhasil disalin ke clipboard

window = tk.Tk()                                                                                # buat objek window sebagai root window dari aplikasi
window.title("Cuttly Link Shortener")                                                           # berikan judul pada jendela aplikasi
window.configure(bg="black")                                                                    # atur warna background jendela menjadi hitam
window.resizable(False,False)                                                                   # cegah pengguna untuk mengubah ukuran jendela aplikasi
label = tk.Label(window, text="@fxrdhan_", font=('arial', '8'),                                
                 fg="magenta", bg="black")                                                     
label.place(relx=0, rely=1, anchor="sw")                                                        

entry_list = []                                                                                 # buat list kosong untuk kotak teks
result_list = []                                                                                # buat list kosong untuk label

for i in range(3):                                                                              # ulangi 5 kali
    label = tk.Label(window, text=f"Link {i+1}:", fg="white", bg="black")                       # buat label sebagai keterangan input link
    label.grid(row=i, column=0, padx=5, pady=5)                                                 # tempatkan label pada kolom pertama dan baris ke-i
    entry = tk.Entry(window, width=30)                                                          # buat entry widget untuk menginputkan link
    entry.grid(row=i, column=1, padx=5, pady=5)                                                 # tempatkan entry pada kolom kedua dan baris ke-i
    entry_list.append(entry)                                                                    # tambahkan entry ke dalam list entry_list
    result = tk.Label(window, text="", fg="white", bg="grey", width=20, anchor="w")             # buat label kosong untuk menampilkan hasil
    result.grid(row=i, column=2, padx=5, pady=5)                                                # tempatkan label pada kolom ketiga dan baris ke-i
    result.bind("<Button-1>", copy_to_clipboard)                                                # ikat event mouse click pada label hasil agar hasil dapat dicopy ke clipboard
    result_list.append(result)                                                                  # tambahkan label hasil ke dalam list result_list

button_shorten = tk.Button(window, text="Shorten Links", command=shorten_links,                 # buat tombol untuk memperpendek link
                        bg="green", fg="white",                                                 # atur warna tombol dan warna teks
                        font=("arial bold", "10"))                                              # atur jenis font dan ukuran font
button_shorten.grid(row=5, column=1, padx=5, pady=5, columnspan=1)                              # atur posisi penempatan tombol                           

button_reset = tk.Button(window, text="Reset Links", command=reset_links,                       # buat tombol untuk reset untuk menghapus semua link sebelumnya
                        bg="red", fg="white",                                                   # atur warna tombol dan warna teks
                        font=("arial bold italic", "10"))                                       # atur jenis font dan ukuran font
button_reset.grid(row=5, column=2, padx=5, pady=5, columnspan=1)                                # atur posisi penempatan tombol

window.mainloop()                                                                               # jalankan main loop