import os
import subprocess
tmpdir = 'heic'

files = os.listdir(tmpdir)

for f in files:
    command = 'sips --setProperty format jpeg ' + tmpdir + f +  ' --out ' + tmpdir + f.replace('.HEIC','.jpeg')
    subprocess.call(command, shell=True)

