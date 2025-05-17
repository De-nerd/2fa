import pyotp
import time

def generate_google_2fa_code(key):
    totp = pyotp.TOTP(key)
    return totp.now()

def seconds_remaining():
    return 30 - (int(time.time()) % 30)

def simple_2FA(key):
    key = key.replace(" ", "")
    return(generate_google_2fa_code(key))

def loop(key):
    while True:
        print(generate_google_2fa_code(key))
        time.sleep(seconds_remaining())

def output(key):
    return("Current 2FA Code:", generate_google_2fa_code(key))

def output_loop(key):
    while True:
        print("Current 2FA Code:", generate_google_2fa_code(key))
        time.sleep(seconds_remaining())

def insert():
    key = input("Key: ")
    key = key.replace(" ", "")
    return key

def insert_output():
    key = input("Key: ")
    key = key.replace(" ", "")
    return("Current 2FA Code:", generate_google_2fa_code(key))

def insert_output_loop():
    key = input("Key: ")
    key = key.replace(" ", "")
    while True:
        print("Current 2FA Code:", generate_google_2fa_code(key))
        time.sleep(seconds_remaining())