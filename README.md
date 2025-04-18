# ViolaAI  
**Voice-Activated AI Assistant**  
*Powered by OpenAI Whisper (STT) & Edge-TTS (TTS)*  

A lightweight Python tool that processes voice input via OpenAI Whisper and responds with synthesized speech. Requires a **DeepSeek API key** (minimal cost per query). If we're acquainted, I can share a key with you.  

---

## Compatibility Notice  
**OpenAI Whisper does not support Python 3.13**. Use **Python 3.10** for guaranteed stability.  

---

## Setup Guide  

### 1️⃣ **Download the Project**  
- Click the green **"Code" button** (top right of this page) → **"Download ZIP"**.  
- Extract the ZIP to your preferred directory.  

### 2️⃣ **Install Dependencies**  
#### **FFmpeg (Required for Audio Processing)**  
- **Linux**: Run `sudo apt install ffmpeg mpg321`  
- **Windows**:  
  1. Download FFmpeg from [BtbN's latest build](https://github.com/BtbN/FFmpeg-Builds/releases/latest).  
  2. Extract and [add to PATH](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10). *(Need help? Ask ChatGPT!)*  

#### **Python 3.10 (Recommended)**  
- Download Python 3.10 from [python.org](https://www.python.org/downloads/).  

### 3️⃣ **Set Up Virtual Environment**  
```bash
# Navigate to the project directory, then:
py -3.10 -m venv venv      # Create virtual env
.\venv\Scripts\activate    # Activate (Windows)
source venv/bin/activate   # Activate (Linux/Mac)
```

### **4️⃣ Install Python Dependencies**

All required packages will be installed automatically, but ensure you're working in a Python 3.10 virtual environment (not 3.13, as Whisper isn't compatible).

**Required packages:**
```bash
pip install openai edge_tts whisper sounddevice scipy
```
### 5️⃣ **Run the Application**
1. Open a terminal in the project directory
2. ```bash
python main.py
```
