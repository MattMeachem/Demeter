import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_extension = os.path.splitext(event.src_path)[1].lower()
        if file_extension == ".evtx":
            # Execute command for event log file
            print(f"Event log file created: {event.src_path}")
            # Replace the command with your desired command for event log files
            os.system("your_event_log_command_here")
        elif file_extension == ".pcap":
            # Execute command for pcap file
            print(f"PCAP file created: {event.src_path}")
            # Replace the command with your desired command for pcap files
            os.system("your_pcap_command_here")

def watch_folder(folder_path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)  # Sleep for 10 seconds
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_path = "/path/to/your/folder"  # Change this to the folder you want to monitor
    watch_folder(folder_path)
