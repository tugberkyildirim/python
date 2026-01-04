# SecureBox v1.0 🔐

SecureBox is a modern, lightweight, and professional cryptography toolkit built with Python and PyQt5. It provides essential security tools for daily use, designed with a focus on both functionality and aesthetics.



## 🚀 Key Features

* **Advanced Password Generator:** Create secure passwords with customizable length (8-64 chars).
    * Toggle Uppercase, Lowercase, Numbers, and Special Symbols.
    * Integrated "Copy to Clipboard" action inside the input field.
* **Base64 Encoder/Decoder:** Fast conversion between Plain Text and Base64.
    * Optimized vertical layout for clean text processing.
* **RSA Crypto Toolkit:**
    * Generate **1024, 2048, or 4096-bit** RSA key pairs.
    * **Disk Persistence:** Save keys to `Data/RSA/` and load them back later.
    * Secure Encryption and Decryption using the **PKCS1_OAEP** protocol.
* **Professional UI:** Clean interface and modern font-weight balance.

---

## 🛠️ Requirements

The project requires the following libraries:

* **Python 3.10+**
* **PyQt5** (For the GUI)
* **PyCryptodome** (For RSA Algorithms)

Install dependencies with a single command:
```
pip install PyQt5 pycryptodome
```
**📂 Project Structure**

```
SecureBox/
├── main.py             # Main GUI application
├── PasswordManager.py  # Backend logic and crypto functions
├── README.md           # Project documentation
└── Data/
    └── RSA/            # Directory for stored .pem keys
```
Run Application:
```
python main.py
```
Key Management: Go to the RSA tab, select your bit size, click Generate Keys, and then Save to Disk. Your keys will be securely stored as `private.pem` and `public.pem` in the `Data/RSA/` folder.

**🛡️ Security Note**
This project is intended for educational and personal use only.

Important: Never commit sensitive data such as private RSA keys to version control.
Ensure that the `Data/` directory (or any directory containing cryptographic keys) is included in your `.gitignore` file to prevent accidental leakage of private keys.

For better security, always generate RSA keys with a minimum length of 2048 bits and protect private keys with a passphrase.
