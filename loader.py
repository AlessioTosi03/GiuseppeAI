import sys
import subprocess
import importlib

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

imports = {
    "openai==0.28": "openai",
    "edge_tts": "edge_tts",
    "whisper": "whisper",
    "sounddevice": "sd",  # custom alias
    "scipy.io.wavfile": "wav"
}

print("Checking for required packages... (this may take a while)")

print(f"Do you want to install openai-whisper? (y/n)")
choice = input().strip().lower()
if choice == 'y':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openai-whisper"])
else:
    print(f"Exiting... Openai-whisper is required.")
    sys.exit()

# Load them into a dict
loaded = {}

for module, alias in imports.items():
    try:
        imported_module = importlib.import_module(module.split("==")[0])
        globals()[alias] = imported_module
    except ImportError:
        print(f"Do you want to install {module}? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            if '==' in module: install(module)  # Install specific version
            else: install(module.split('.')[0])
            imported_module = importlib.import_module(module.split("==")[0])
            globals()[alias] = imported_module
        else:
            print(f"Exiting... {module} is required.")
            sys.exit()

    loaded[alias] = imported_module