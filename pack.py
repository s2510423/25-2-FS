import subprocess
import sys

def pip():
    subprocess.run([sys.executable, '-m','pip','install','-r','requirements.txt'])

pip()