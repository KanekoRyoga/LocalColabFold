import glob
import os
import subprocess


file_path = "/home/kaneko/221018/*"

files = sorted(glob.glob(file_path))


for file in files:
  
    cmd = ["colabfold_batch" , "--amber" , "--use-gpu-relax" , "--num-recycle 3" , "--templates" ,  file , "outputdir"]
   
    subprocess.run(cmd)