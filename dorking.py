import webbrowser
import urllib.parse
import os
import time
from datetime import datetime

def generate_queries(target):
    return [
        f'site:facebook.com "{target}"',
        f'site:instagram.com "{target}"',
        f'site:threads.net "{target}"',
        f'site:tiktok.com "@{target}"',
        f'site:linkedin.com/in "{target}"',
        f'inurl:{target} site:pastebin.com',
        f'filetype:pdf "{target}"',
        f'"{target}" ext:doc OR ext:docx OR ext:odt',
        f'"{target}" ext:xls OR ext:xlsx',
        f'"{target}" ext:ppt OR ext:pptx',
        f'"{target}" intitle:index.of? "{target}"',
        f'"{target}" site:archive.org',
    ]

def open_in_browser(queries):
    base_url = "https://www.google.com/search?q="
    for query in queries:
        url = base_url + urllib.parse.quote_plus(query)
        webbrowser.open(url)
        time.sleep(3)  

def save_to_file(queries, target):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"dork_{target.replace(' ', '_')}_{timestamp}.txt"
    filepath = os.path.join("reports", filename)
    os.makedirs("reports", exist_ok=True)
    
    with open(filepath, "w") as f:
        for query in queries:
            f.write(f"{query}\n")
    
    print(f"[✔] Hasil berhasil disimpan ke: {filepath}")

if __name__ == "__main__":
    print("===== GOOGLE DORKING TOOL =====")
    target = input("Masukkan target (nama/user/email/domain): ").strip()

    queries = generate_queries(target)
    
    print("\n[+] Membuka hasil pencarian di browser...")
    open_in_browser(queries)

    while True:
        print("\n[2] Simpan hasil ke file report")
        print("[3] Keluar")
        choice = input("Pilih opsi selanjutnya (2/3): ")

        if choice == "2":
            save_to_file(queries, target)
            print("[✔] Hasil berhasil disimpan.")
        elif choice == "3":
            print("[-] Keluar dari program.")
            break
        else:
            print("[!] Pilihan tidak valid. Coba lagi.")
