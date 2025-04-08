# **PassStretcher** 

Transform simple passwords into long, complex strings using multiple **hashing** and **encoding** algorithms!  

![Python](https://img.shields.io/badge/Python-3-blue?style=flat-square&logo=python)  

---  

## ** Overview**  

**PassStretcher** is a Python tool that takes a basic password (e.g., `"daniel8252"`) and converts it into a long, seemingly random—yet **deterministic** (same output for the same input)—string.  

 **Why use it?**  
- Generate **unique and complex** passwords from a memorable base.  
- Create secure, reproducible keys for encryption.  
- Increase entropy for weak passwords without sacrificing usability.  

---  

## ** How to Use**  

### **Installation**  
Ensure you have **Python 3.7+** installed.  

```bash
git clone https://github.com/Vasilysmert/PassStretcher.git
cd PassStretcher
```

### **Execution**  
```bash
python3 passtretcher.py -s "your_password" -l 512
```

#### **Arguments:**  
| Argument | Description | Default |  
|-----------|-----------|--------|  
| `-s` / `--string` | Input password (required) | - |  
| `-l` / `--length` | Output length (minimum: 10) | `1024` |  
| `-v` / `--verbose` | Show processing details | `False` |  

### **Example**  
**Input:**  
```bash
python3 passtretcher.py -s "daniel8252" -l 256 -v
```  

**Output:**  
```
Processing input string: 'daniel8252'  
Generating output with 256 characters...  

Result:  
a1b2c3d4e5f6... (256 hexadecimal characters)  
```  

---  

## ** How It Works**  

1. **Cascade Hashing**  
   - Applies **SHA3-512, BLAKE2b, and SHA-512** in multiple iterations.  
2. **Multi-Stage Encoding**  
   - Uses **Base64, Base85, and Hexadecimal** to enhance complexity.  
3. **Length Adjustment**  
   - Leverages **SHAKE-256** to produce the exact desired output length.  

---  
