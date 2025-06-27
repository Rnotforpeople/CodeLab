import webbrowser
import urllib.parse
import os
import time
from datetime import datetime

def generate_queries(target):
    """
    Generates a list of Google Dorking queries specifically for Instagram,
    including 'site', 'intext', 'intitle', and 'inurl' modifiers.
    """
    instagram_queries = [
        f'site:instagram.com "{target}"',            
        f'site:instagram.com intext:"{target}"',     
        f'site:instagram.com intitle:"{target}"',    
        f'site:instagram.com inurl:"{target}"',      
        f'site:instagram.com @{target}',             
        f'site:instagram.com hashtag:{target}'       
    ]
    return instagram_queries

def open_in_browser(queries):
    """
    Opens each generated Google Dork query in a new browser tab.
    Includes a delay between opening tabs to prevent overwhelming the browser.
    """
    base_url = "https://www.google.com/search?q="
    for query in queries:
        url = base_url + urllib.parse.quote_plus(query)
        print(f"[+] Opening: {url}") 
        webbrowser.open(url)
        time.sleep(3) # Wait for 3 seconds before opening the next tab

def save_to_file(queries, target):
    """
    Saves the generated Google Dork queries to a text file in a 'reports' directory.
    The filename includes the target and a timestamp for easy identification.
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"instagram_dork_{target.replace(' ', '_')}_{timestamp}.txt"
    filepath = os.path.join("reports", filename)
    os.makedirs("reports", exist_ok=True) 
    
    with open(filepath, "w") as f:
        for query in queries:
            f.write(f"{query}\n")
    
    print(f"[✔] Results saved to: {filepath}")

if __name__ == "__main__":
    print("===== INSTAGRAM GOOGLE DORKING TOOL =====")
    target = input("Input Instagram Target (username/name/keyword): ").strip()
    queries = generate_queries(target)
    print("\n[+] Opening results in browser...")
    open_in_browser(queries)

    
    while True:
        print("\n[2] Save Results to File Report")
        print("[3] Quit")
        choice = input("Select Next Option (2/3): ")

        if choice == "2":
            save_to_file(queries, target)
            print("[✔] Results Saved.")
        elif choice == "3":
            print("[-] Exiting from program.")
            break
        else:
            print("[!] Not a valid choice. Please try again.")
