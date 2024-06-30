import os
import time

# Petya.exe
folder_path = "C:/Users/Username/Downloads"

# Whitelisted file types
whitelist = [".doc", ".docx", ".pdf" ]

# Infinite loop for continuous monitoring
while True:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ending) for ending in whitelist):
                # File is whitelisted, continue monitoring
                continue
            else:
                # Unauthorized file detected, take action (e.g., delete file, alert user)
                print(f"Unauthorized file detected you may have petya ransomware or another for of a virus, please run this virus through here: https://www.virustotal.com/gui/home/upload: {os.path.join(root, file)}")
                # Add your actions here (e.g., delete the file, alert the user)

    # Interval for monitoring (every 5 seconds)
    time.sleep(5)
