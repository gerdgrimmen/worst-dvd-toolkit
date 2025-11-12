import subprocess
lsdvd = subprocess.run(["lsdvd", "/dev/sr0"], capture_output=True, text=True)

print(lsdvd.stdout)

# simple info?
#$ dvdbackup -i /dev/sr0 -I
# full dvd
#$ dvdbackup -i /dev/dvd -M -p
dvdbackup = subprocess.run(["dvdbackup","-i", "/dev/sr0", "-M", "-p"], capture_output=True, text=True)

print(dvdbackup.stdout)