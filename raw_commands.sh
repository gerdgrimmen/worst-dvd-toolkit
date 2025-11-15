# Just the Raw Commands used in the script
# lsdvd
lsdvd /dev/sr0
# dvdbackup
dvdbackup -i /dev/dvd -M -p
# ffmpeg
ffmpeg -y -i VTS_02_2.VOB -map 0:v -c:v copy -map 0:a -c:a copy -map 0:s -c:s copy output2.mp4