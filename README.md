# 🔓 Multi-threaded Password Cracker

## 📖 Overview
A **multi-threaded password cracking tool** built in **Python** and **C++** that supports:
- **Dictionary attacks** (using wordlists)
- **Brute-force attacks** (iterating through possible passwords)
- **Multi-threading** for faster cracking

## 🚀 Features
✅ Fast multi-threaded brute-force attacks  
✅ Dictionary attack with wordlists  
✅ Hashing & verification with **SHA-256**  
✅ Implemented in both **Python** & **C++**  

---

## ⚙️ Usage

### 📥 Installation
Clone the repository and navigate to the project:
```bash
git clone https://github.com/InfosecSamurai/password_cracker.git
cd password_cracker
```

### ▶️ Running the Python Cracker
```bash
cd python
python cracker.py
```

### ▶️ Running the C++ Cracker
Compile and run:
```bash
cd cpp
g++ -o cracker cracker.cpp -lssl -lcrypto
./cracker
```

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use, modify, and contribute.  

🔹 _Developed by [InfosecSamurai](https://github.com/InfosecSamurai)_  
