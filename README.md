# Bencode-Torrent-Editor

Added set_completed.py for Transmission .resume files.
This script will mark any Transmission torrents as completed.
So you can skip / avoid hash check.  
Tested on Transmission daemon 2.92  
Usage:  
1. Add your torrent to transmission, WITHOUT STARTING IT. If you start it, it will begin the lengthy hash check process which can't be stopped without killing transmission.  
2. Make sure the relevant .resume file is created. In my ubuntu machine .resume files are located at `/var/lib/transmission-daemon/.config/transmission-daemon/resume/`. Your case may vary. To create the .resume file if it doesn't already exist try scraping the tracker for peers, or restarting transmission.  
3. Now that the .resume files exist, stop transmission to avoid having it touch the files while we edit them. I use `service transmission-daemon stop` but depending on your system you may use something else.  
4. Now with transmission stopped, run `python set_completed.py my-file.resume` for any torrent(s) that you want to mark as completed, and start transmission again.

Please note, when stopping/restarting transmission all your torrents may be stopped on restart, and you'll have to start them again manually.
