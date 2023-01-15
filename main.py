import tkinter
import tkinter.messagebox
import tkinter.dialog
import sys
import subprocess

import tkmacosx
import Quartz
import AppKit
from rich import print, inspect

if sys.platform != 'darwin':
    tkinter.messagebox.showerror("Error", "This program is only for macOS")
    
def execute_applescript(script):
    result = subprocess.run(['osascript', '-e', script], capture_output=True)
    return result.stdout.decode('utf-8').strip()

def geAllApps():
    apps = AppKit.NSWorkspace.sharedWorkspace().runningApplications()
    all_app = []
    for app in apps:
        all_app.append(app)
            

def getAllWindows():
    """
    Get all windows on macOS
    Returns an list with this format: https://developer.apple.com/documentation/coregraphics/quartz_window_services/required_window_list_keys
    """
    all_windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionAll | Quartz.kCGWindowListExcludeDesktopElements, Quartz.kCGNullWindowID)
    return all_windows


print(getAllWindows())