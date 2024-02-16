import os 

def read_dotenv(dir):
    with open(f"{dir}.env", "r") as f:
        for line in f.readlines():
            try:
                key, value = line.split('=')
                os.putenv(key, value)
            except ValueError:
                # syntax error
                pass

def write_dotenv_encryption_key(dir,key,value):
    with open(f"{dir}\.env", "w") as f:
        f.write(f"{key}={value}")
        