import os.path
import pyotp
import time
import argparse
import sys
import keyboard
import threading

print("\nPress c twice to clear.\n")

try:
    def charPressActions():
        global action
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                action = event.name
                if action == "c":
                    action = ""
                    while True:
                        event = keyboard.read_event()
                        if event.event_type == keyboard.KEY_DOWN:
                            action = event.name
                            if action == "c":
                                os.system("cls")
                                action = ""
                                break
                            else:
                                action = ""
                                break

    charPressProcess = threading.Thread(target=charPressActions)
    charPressProcess.daemon = True
    charPressProcess.start()


    def generate_google_2fa_code(key):
        totp = pyotp.TOTP(key)
        return totp.now()

    def seconds_remaining():
        return 30 - (int(time.time()) % 30)

    def doc(file):
        global key
        file = file.replace('"', '')
        with open(file, "r") as contents:
            key = contents.readline()
        key = key.replace("\n", "")

    def code():
        global key
        key = key.replace(" ", "")

    parser = argparse.ArgumentParser(description="-p/--path OR -s/--string", epilog="The key is not space sensitive")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--path", help="Path to the file with the key on the first line")
    group.add_argument("-s", "--string", help="The key itself")
    args, unknown = parser.parse_known_args()

    if args.path:
        file = args.path
        try:
            doc(file)
            code()
        except:
            print("Invalid argument")
            time.sleep(1)
            sys.exit()
    elif args.string:
        key = args.string
        code()
    elif unknown:
        if os.path.exists(unknown[0]):
            file = unknown[0]
            try:
                doc(file)
                code()
            except:
                print("Invalid argument")
                time.sleep(1)
                sys.exit()
        else:
            print(f"Unknown argument: {' '.join(unknown)}")
            time.sleep(1)
            sys.exit()
    else:
        while True:
            item = input("s - string\np - path\n ")
            item.lower()
            if item == "s" or item == "string" or item == "s - string":
                key = input("Key: ")
                code()
                break
            elif item == "p" or item == "path" or item =="p - path":
                file = input("path to the file with the key on the first line: ")
                try:
                    doc(file)
                    code()
                    break
                except:
                    print("Invalid path")
                    time.sleep(1)
            else:
                print("invalid choice")

    while True:
        try:
            print("Current 2FA Code:", generate_google_2fa_code(key))
            time.sleep(seconds_remaining())
        except(KeyboardInterrupt):
            sys.exit()
        except:
            print("Invalid key")
            time.sleep(1)
            sys.exit()
except:
    sys.exit()