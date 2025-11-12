import subprocess
import sys
from shutil import which

version = "0.1.0"

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

def command_check_dependencies():
    print("You do not need every dependency to run the toolkit: ")
    if which("lsdvd"):
        print("lsdvd is found. Available commands are:")
        print("info")
    if which("dvdbackup"):
        print("dvdbackup is found. Available commands are:")
        print("backup (not yet implemented)")
    if which("ffmpeg"):
        print("ffmpeg is found. Available commands are:")
        print("convert (not yet implemented)")

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

if __name__ == "__main__":
    arguments_guard()
    determine_command(sys.argv[1])