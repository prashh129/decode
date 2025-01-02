# Simple Encryption and Decryption Program

This Python script provides a basic encryption and decryption mechanism for words. It's designed for demonstration purposes and includes customizable prefixes and suffixes.

---

## Features
- **Encryption**: Transforms a word by moving the first character to the end, converting it to lowercase, and appending a predefined prefix and suffix.
- **Decryption**: Reverses the encryption process to retrieve the original word.
- Handles words shorter than 3 characters by simply reversing them.

---

## How It Works
1. **Encrypt**:
   - Adds a prefix (`"axt"`) and suffix (`"lqz"`) to the modified word.
   - Example: `"Hello"` → `"axtellohqlz"`

2. **Decrypt**:
   - Removes the prefix and suffix to restore the original word.
   - Example: `"axtellohqlz"` → `"Hello"`

---

## Usage
### Prerequisites
- Python 3.x installed on your system.

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/prashh129/decode.git
   ```
2. Navigate to the directory:
   ```bash
   cd decode
   ```
3. Run the script:
   ```bash
   python3 script_name.py
   ```
4. Follow the prompts:
   - Enter `"code"` to encrypt a word.
   - Enter `"decode"` to decrypt a word.
   - Enter the word when prompted.

---

## Example
### Encryption:
Input:
```
Enter if you want to Code or Decode: code
Enter the word you want to encrypt: Hello
```
Output:
```
Your encrypted word is: axtellohqlz
```

### Decryption:
Input:
```
Enter if you want to Code or Decode: decode
Enter the word you want to decrypt: axtellohqlz
```
Output:
```
Your decrypted word is: Hello
```

---

## Notes
- Words shorter than 3 characters are reversed during both encryption and decryption.
- Input validation ensures that empty words are not accepted.

---

## License
This project does not have a license. All rights are reserved. If you would like to use this code, please contact the repository owner for permission.

## Acknowledgments

Thanks for checking out this project! If you have any feedback or questions, please feel free to open an issue or contact me directly.

