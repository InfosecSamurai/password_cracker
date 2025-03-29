import hashlib
import itertools
import string
import threading

def hash_password(password):
    """Hashes the password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(hash_to_crack, wordlist_file):
    """Attempts to crack the hash using a dictionary attack."""
    with open(wordlist_file, "r", encoding="utf-8") as file:
        for word in file:
            word = word.strip()
            if hash_password(word) == hash_to_crack:
                print(f"[+] Password found: {word}")
                return word
    print("[-] Password not found in dictionary.")
    return None

def brute_force_attack(hash_to_crack, length=4):
    """Attempts a brute-force attack with given character length."""
    chars = string.ascii_lowercase + string.digits  # Modify if needed

    def attempt(password):
        if hash_password(password) == hash_to_crack:
            print(f"[+] Password found: {password}")
            return password

    for combination in itertools.product(chars, repeat=length):
        password = ''.join(combination)
        attempt(password)

def multi_threaded_brute_force(hash_to_crack, length=4, threads=4):
    """Splits brute-force workload across multiple threads."""
    chars = string.ascii_lowercase + string.digits
    chunk_size = len(chars) // threads

    def worker(start, end):
        for combination in itertools.product(chars[start:end], repeat=length):
            password = ''.join(combination)
            if hash_password(password) == hash_to_crack:
                print(f"[+] Password found: {password}")
                return

    thread_list = []
    for i in range(threads):
        start, end = i * chunk_size, (i + 1) * chunk_size
        thread = threading.Thread(target=worker, args=(start, end))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

# Example usage
if __name__ == "__main__":
    target_hash = hash_password("pass123")  # Hash to crack (example)
    
    print("[*] Running dictionary attack...")
    dictionary_attack(target_hash, "wordlist.txt")

    print("[*] Running brute-force attack...")
    multi_threaded_brute_force(target_hash, length=4, threads=4)
