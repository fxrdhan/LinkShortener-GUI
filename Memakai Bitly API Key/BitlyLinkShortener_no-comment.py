import tkinter as tk
import tkinter.messagebox as messagebox 
import requests
import pyperclip

TOKEN = "Masukkan token API Bitly akun anda disini"

def shorten_link(link):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    payload = {"long_url": link}
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["link"]

def shorten_links():
    for i in range(3):
        LINK = entry_list[i].get()
        if LINK:
            try:
                shortened_link = shorten_link(LINK)
                result_list[i].config(text=shortened_link, fg="green", bg="black")
            except Exception:
                result_list[i].config(text="Link can't be shortened!", fg="red", bg="black")

def copy_to_clipboard(event):
    widget = event.widget
    result = widget.cget("text")
    if result:              
        pyperclip.copy(result)
        messagebox.showinfo("", "Shortened link has been copied to clipboard.")
        
def reset_links():
    for i in range(3):
        entry_list[i].delete(0, 'end')
        result_list[i].config(text="", bg="grey")

window = tk.Tk()
window.title("Bitly Link Shortener")
window.configure(bg="black")
window.resizable(False,False)
label = tk.Label(window, text="@fxrdhan_", fg="magenta", bg="black")
label.place(relx=0, rely=1, anchor="sw")

entry_list = []
result_list = []

for i in range(3):
    label = tk.Label(window, text=f"Link {i+1}:", fg="white", bg="black")
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(window, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entry_list.append(entry)
    result = tk.Label(window, text="", fg="white", bg="grey", width=20, anchor="w")
    result.grid(row=i, column=2, padx=5, pady=5)
    result.bind("<Button-1>", copy_to_clipboard)
    result_list.append(result)

button_shorten = tk.Button(window, text="Shorten Links", command=shorten_links,                 
                        bg="green", fg="white",                                          
                        font=("arial bold", "10"))                                       
button_shorten.grid(row=5, column=1, padx=5, pady=5, columnspan=1)                                                    

button_reset = tk.Button(window, text="Reset Links", command=reset_links,                      
                        bg="red", fg="white",                                             
                        font=("arial bold italic", "10"))                                       
button_reset.grid(row=5, column=2, padx=5, pady=5, columnspan=1)                          

window.mainloop()                