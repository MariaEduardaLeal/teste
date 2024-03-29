import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube

def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()

    # Abrir diálogo para selecionar a pasta de destino
    save_path = filedialog.askdirectory()
    if save_path:
        stream.download(save_path)

root = tk.Tk()
root.title('YOUTUBE DOWNLOAD')

# Adicione um ícone
root.iconbitmap('youtube.png')

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(main_frame, text="URL:")
url_label.grid(row=0, column=0, padx=(0, 10))

url_entry = ttk.Entry(main_frame, width=50)
url_entry.grid(row=0, column=1)

download_button = ttk.Button(main_frame, text="Download", command=download_video)
download_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

root.mainloop()
