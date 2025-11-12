# Worst DVD Toolkit

Simple Control Programm for various DVD tools.

## Description

Side Project - Documentation of the process for Orchestrating several different dvd tools.
Possible Structure of tasks:
* ISO File of DVD
* (Optional) Open Disc Drive/Eject Disc

Operations on ISO File or DVD-Drive directly
* Get Chapter / Episode Info with lsdvd
  * Figure Out How exactly the IFO File is structured and maybe read it without dependency.
  * Save Info in File in project folder
* (Maybe) Change Container from VOB to mp4?
* Extract Video and Audio together or seperate based on IFO File data?
  * if Video and Audio are extracted separately merge
    * if possible save all or just more than one audio track
  * name the files according to the data found in ifo file

### Dependencies

* lsdvd
* dvdbackup
* ffmpeg
* import subprocess
* import sys
* from shutil import which

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

just run the command "worst-dvd-toolkit"

```
worst-dvd-toolkit
```


## Authors

Contributors names and contact info

ex. Gerd Grimmen (F.KU)

## Version History

* 0.1
    * Initialize project structure
    * added commands help, version, info, check

## License

The Unlicense. Feel free to use or change it how you need.