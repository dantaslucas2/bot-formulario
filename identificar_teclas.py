import pyHook, pythoncom, sys, logging

file_log='C:\\log.txt'

def OnKeyboardEvent(event):
    print("Dd")
    return True

hooks_manager = pyHook.HookManager ( )
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard ( )
pythoncom.PumpMessages () #pythoncom module is used to capture the key messages.
