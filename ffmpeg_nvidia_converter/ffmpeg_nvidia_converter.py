import os  # Importing the os module which provides a way of using operating system dependent functionality.
import subprocess  # Importing the subprocess module which allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
from send2trash import send2trash  # Importing the send2trash module which sends files to the Trash (or Recycle Bin) natively and on all platforms.

# Defining a function to convert videos to mp4 format.
def convert_videos_to_mp4(folder_path, logfile):
    with open(logfile, "w", encoding="utf-8") as log:  # Opening the log file in write mode.
        for root, dirs, files in os.walk(folder_path):  # Looping through each file in the specified folder and its subfolders.
            for file in files:  # Looping through each file.
                # Checking if the file ends with any of the specified video formats.
                if file.endswith((".avi", ".mov", ".ogg", ".webm", ".wmv")):
                    input_file = os.path.join(root, file)  # Joining the root and file name to get the full path of the input file.
                    output_file = os.path.join(root, f"{os.path.splitext(file)[0]}.mp4")  # Creating the output file path by replacing the extension of the input file with .mp4.
                    counter = 1  # Initializing a counter for duplicate files.
                    while os.path.exists(output_file):  # Checking if a file with the same name already exists.
                        output_file = os.path.join(root, f"{os.path.splitext(file)[0]} ({counter}).mp4")  # If a file with the same name exists, append a counter to the name.
                        counter += 1  # Incrementing the counter.
                    command = f'ffmpeg -hwaccel cuvid -hwaccel_output_format cuda -i "{input_file}" -c:v h264_nvenc -c:a aac -map_metadata:g 0 -preset medium -crf 23 "{output_file}"'  # Defining the command to convert the video using ffmpeg.
                    try:
                        result = subprocess.run(command, check=False)  # Running the command and capturing the result.
                        if result.returncode == 0:  # Checking if ffmpeg successfully converted the video.
                            log.write(f"Successfully converted {input_file} to {output_file}\n")  # Writing a success message to the log file.
                            send2trash(input_file)  # Moving the original file to the recycle bin.
                        else:
                            log.write(f"Failed to convert {input_file}: ffmpeg returned non-zero exit code\n")  # Writing an error message to the log file if ffmpeg failed to convert the video.
                    except subprocess.CalledProcessError as e:
                        log.write(f"Failed to convert {input_file}: {e}\n")  # Writing an error message to the log file if there was an error running ffmpeg.
                    except UnicodeEncodeError as e:
                        log.write(f"Failed to convert {input_file}: {e}\n")  # Writing an error message to the log file if there was a UnicodeEncodeError.

# Defining the path of the folder containing videos to be converted
# This is is the scripts default path
default_path = os.path.join(os.environ.get('USERPROFILE'), 'Downloads', 'ffmpeg_nvidia_converter', 'test')

# This is your input path. REPLACE THIS WITH THE ACTUAL INPUT.
input_path = "%userprofile%\\Downloads\\ffmpeg_nvidia_converter\\test"

# Check if the input path contains %userprofile%
if "%userprofile%" in input_path.lower():
    # Script to replace %userprofile% with the actual USERPROFILE path
    folder_path = input_path.replace("%userprofile%", os.environ.get('USERPROFILE'))
else:
    # Use the input path as is
    folder_path = input_path

# If the folder path is empty, use the default path
if not folder_path:
    folder_path = default_path

# Defining the path of the folder where logfile needs to be saved
# This is the script default log file path
default_logfile = os.path.join(os.environ.get('USERPROFILE'), 'Downloads', 'ffmpeg_nvidia_converter', 'conversion_log.txt')

# This is your input log file path. REPLACE THIS WITH THE ACTUAL INPUT.
input_logfile = "%userprofile%\\Downloads\\ffmpeg_nvidia_converter\\conversion_log.txt"

# Check if the input log file path contains %userprofile%
if "%userprofile%" in input_logfile.lower():
    # Script to replace %userprofile% with the actual USERPROFILE path
    logfile = input_logfile.replace("%userprofile%", os.environ.get('USERPROFILE'))
else:
    # Use the input log file path as is
    logfile = input_logfile

# If the log file path is empty, use the default log file path
if not logfile:
    logfile = default_logfile

convert_videos_to_mp4(folder_path, logfile)  # Calling the function with folder_path and logfile as arguments.
