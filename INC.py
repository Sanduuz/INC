#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Programmed by Sanduuz
# Instagram: @sanduuz
# E-mail: 19jdmz5js@protonmail.ch

import os, optparse

try:
    import requests
except ImportError:
    import pip
    print "Missing library: requests"
    install_ = str(raw_input("Install? [Y/N]: ")).upper()
    if install_ == "Y":
        print "Installing module: requests"
        pip.main(['install', 'requests'])
    elif install_ == "N":
        print "requests module is crucial for the script!"
        verificateInstall_ = str(raw_input("Install? [Y/N]: ")).upper()
        if verificateInstall_ == "Y":
            print 'Installing module: requests'
            pip.main(['main', 'requests'])
        elif verificateInstall_ == "N":
            exit("Can't continue without requests module!\nExiting...")
        else:
            exit("Expected input Y/N, got "+verificateInstall_+" Instead\nExiting...")
    else:
        print "Please choose Y/N!"

def checkName(wordlist, verbose):
    with open(wordlist) as wordlist:
        print ''
        for user in wordlist.readlines():
            username = user.strip('\n')
            req = requests.get("https://www.instagram.com/"+username)
            if req.status_code == 404:
                print 'Username Found!: ' + str(username)
            elif req.status_code == 200:
                if verbose == True:
                    print "Username Taken: " + str(username)
            else:
                print "Unknown Error Code: " + req.status_code

def checkWordlist(wordlist):
    if os.path.isfile(wordlist) == True:
        return True
    elif os.path.isfile(wordlist) == False:
        return False
    else:
        print "What the actual fuck could cause this error?!"

def interactiveMode(verbose):
    mode = "Interactive"
    banner1(mode, verbose)
    print ''
    print 'Please input the names you would like checked.'
    print '[Separated by comma. For example: Sanduuz,created,this,script.]\n'
    usernames = str(raw_input("Usernames: "))
    usernames = usernames.split(',')
    print ''
    for user in usernames:
        req = requests.get("https://www.instagram.com/"+user)
        if req.status_code == 404:
                print 'Username Found!: ' + str(user)
        elif req.status_code == 200:
            if verbose == True:
                print "Username Taken: " + str(user)
        else:
            print "Unknown Error Code: " + req.status_code

def main():
    parser = optparse.OptionParser("Usage: python INC.py -w <Wordlist> | See -h/--help for more help.")
    parser.add_option('-w', dest='wordlist', type='string', help='Specify Wordlist [Passive Mode]')
    parser.add_option('-i', dest='interact', default=False, action="store_true", help='Interactive Mode')
    parser.add_option('--dv', dest='verbose', default=True, action="store_false", help='Disable Verbosity')

    (options, args) = parser.parse_args()

    if (options.wordlist == None) and (options.interact == False):
        exit("Usage: "+parser.usage)
    elif (options.wordlist != None) and (options.interact == True):
        exit("Interactive mode can't be used with passive mode.")
    elif (options.interact == True) and (options.wordlist == None):
        verbose = options.verbose
        interactiveMode(verbose)
    else:
        mode = "Passive"
        wordlist = options.wordlist
        verbose = options.verbose
        banner(mode, verbose, wordlist)
        checkWordlistValue = checkWordlist(wordlist)
        if checkWordlistValue == True:
            checkName(wordlist, verbose)
        elif checkWordlistValue == False:
            exit("\nWordlist not found! Make sure the file exists.")
        else:
            print "What the fuck causes this error."

def banner(mode, verbose, wordlist):
    banner = """
    _____   ________
   /  _/ | / / ____/      ____  __  __
   / //  |/ / /          / __ \/ / / /
 _/ // /|  / /____  __  / /_/ / /_/ /
/___/_/ |_/\_____/ /_/ / .___/\__, /
                      /_/    /____/

Instagram Name Checker

Author: Sanduuz
Instagram: @Sanduuz
E-mail: 19jdmz5js@protonmail.ch

[Mode] """+mode+" | [Verbosity] "+str(verbose)+"\n[Wordlist] "+os.path.abspath(wordlist)
    print banner

def banner1(mode, verbose):
    banner = """
    _____   ________
   /  _/ | / / ____/      ____  __  __
   / //  |/ / /          / __ \/ / / /
 _/ // /|  / /____  __  / /_/ / /_/ /
/___/_/ |_/\_____/ /_/ / .___/\__, /
                      /_/    /____/

Instagram Name Checker

Author: Sanduuz
Instagram: @Sanduuz
E-mail: 19jdmz5js@protonmail.ch

[Mode] """+mode+" | [Verbosity] "+str(verbose)
    print banner

if __name__ == "__main__":
    main()
