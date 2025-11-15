import subprocess
import sys
from shutil import which

version = "0.3.0"

def arguments_guard():
    if len(sys.argv) < 2:
        print("There is no command given. Nothing To Do here:")
        command_help()
        exit()

def command_guard(command, length):
    print("checking structure for: " + command)
    if len(sys.argv) == length:
        return True
    else:
        print("not the right amount of arguments.")
        exit()

def check_arguments_structure(command):
    match command:
        case "info":
            if command_guard("info", 3):
                lsdvd = subprocess.run(["lsdvd", sys.argv[2]], capture_output=True, text=True)
                print(lsdvd.stdout)
        case "backup":
            if command_guard("backup", 3):
                dvdbackup = subprocess.run(["dvdbackup","-i", sys.argv[2], "-M", "-p"], capture_output=True, text=True)
                print(dvdbackup.stdout)
        case "convert":
            if command_guard("convert", 3):
                ffmpeg = subprocess.run(["ffmpeg", "-y", "-i", sys.argv[2], "-map", "0:v", "-c:v", "copy", "-map", "0:a", "-c:a", "copy", "-map", "0:s", "-c:s", "copy", sys.argv[2][:-3]+"mp4"], capture_output=True, text=True)
                print(ffmpeg.stdout)

def command_version():
    print(version)

def command_help():
    print("Version:")
    command_version()
    print("Help Page")
    print("Type '<script_name> help' to get a list of commands")
    print("")
    print("Commands:")
    print("info <path_to_dvd>")
    print("uses the programm lsdvd")
    print("")
    print("backup <path_to_dvd>")
    print("uses the programm dvdbackup")
    print("")
    print("convert <path_to_single_video>")
    print("uses the programm ffmpeg")
    print("gets all audio tracks and subtitle tracks - both without descriptions")


def command_check_dependencies():
    print("You do not need every dependency to run the toolkit: ")
    if which("lsdvd"):
        print("lsdvd is found. Available commands are:")
        print("info")
    if which("dvdbackup"):
        print("dvdbackup is found. Available commands are:")
        print("backup")
    if which("ffmpeg"):
        print("ffmpeg is found. Available commands are:")
        print("convert")

def determine_command(command):
    match command:
        case "help":
            command_help()
        case "version":
            command_version()
        case "check":
            command_check_dependencies()
        case "info":
            check_arguments_structure("info")
        case "backup":
            check_arguments_structure("backup")

if __name__ == "__main__":
    arguments_guard()
    determine_command(sys.argv[1])