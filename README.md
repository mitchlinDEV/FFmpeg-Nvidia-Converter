# FFmpeg-NVIDIA-accelerated Video Converter

This script batch converts video files in Windows to MP4 format using FFmpeg with NVIDIA GPU hardware acceleration.

## Requirements / Installation

- Windows >7 x64
- NVIDIA GPU and drivers (https://www.nvidia.com/Download/index.aspx?lang=en-us)
- NVIDIA CUDA SDK Headers (https://developer.nvidia.com/nvidia-video-codec-sdk/download) *install if the script wont run with only NVIDIA driver
- Python 3 (https://www.python.org/downloads/windows/) *make sure to enable "Add to PATH"
- send2trash Python module (pip install Send2Trash)
- Chocolatey (pip install choco) *optional for use next step
- FFmpeg compiled with NVIDIA hardware acceleration support ("pip install ffmpeg" / "choco install ffmpeg-full") *According to https://www.gyan.dev/ffmpeg/builds/ all versions include HW acceleration.
  
## Usage

1. Download (and unzip) the package (The repo contains some test files. If the script was downloaded to Windows default Downloads folder, it can run the test without modifications below.
2. Replace (in line-36) `"%userprofile%\\Downloads\\ffmpeg_nvidia_converter\\test"` with the path of the folder containing videos to be converted. It will include subfolders by default. (note: use "\\" between paths)
Replace (in line-55) `"%userprofile%\\Downloads\\ffmpeg_nvidia_converter\\conversion_log.txt"` with the path where you want to store the conversion log.
4. Run the script, open a (Powershell) terminal from the Download folder and enter "ffmpeg_nvidia_converter.py" to execute the script. 

## How It Works

The script walks through each file in the specified folder and its subfolders. If a file ends with a specified video format, it converts the file to MP4 format using FFmpeg with NVIDIA hardware acceleration in place. The original file is then moved to the recycle bin. If an output file name already exists, a number will be added at the end of the filename, similar to how Windows Explorer handles duplicate filenames. The script should work with filenames containing Cyrillic, Arabic, Chinese characters, and other non-ASCII characters. The script will catch any UnicodeEncodeError exceptions and continue with the next file. Only files that are successfully converted will be saved, and any files with errors will be logged as failed conversions. The script should utilize both the GPU and CPU optimally.

## Settings

- Filetypes included by default: avi, mov, ogg, webm, wmv (add/modify as you desire, are case sensitive)
- ffmpeg flags enabled:
  - -hwaccel cuvid: This flag enables CUDA Video Decoder (CUVID), which is a hardware-accelerated video decoder.
  - -hwaccel_output_format cuda: This flag sets the output format for hardware-accelerated decoding to CUDA.
  - -c:v h264_nvenc: This flag sets the codec for video encoding to h264_nvenc, which is a hardware-accelerated H.264 encoder provided by NVIDIA.
  - -c:a aac: This flag sets the codec for audio encoding to aac.
  - -map_metadata:g 0: This flag maps global metadata from input file to output file
  - -preset medium (can be modified as you desire): This flag is used to set the encoding speed to compression ratio. Presets are configurations of x264 options that trade off encoding speed to compression ratio. A slower preset will provide better compression (compression is quality per filesize). The available presets in descending order of speed are: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow, placebo. The medium preset is the default and provides a good balance between encoding speed and compression ratio.
   - -crf 23 (can be modified as you desire): This flag is used to set the Constant Rate Factor (CRF) in x264 and x265 encoders in FFmpeg, which is a quality-controlled variable bitrate. It adjusts the file size to achieve a certain level of quality. The CRF scale is from 0–51, where 0 is lossless, 23 is the default, and 51 is the worst quality. Lower values mean better quality. A CRF of 23 means you’re aiming for a fairly high level of quality.

## License

This project is licensed under The Unlicense - see the LICENSE file for details.

## Contributors

Initiated by mitchlinDEV with help of Bing Chat

## Version
1.00 (Sept 2023)
