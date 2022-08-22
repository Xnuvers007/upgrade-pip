# Upgrade pip python packages from outdated

import sys, os, time
from sys import platform

def startupgradepip():
    if platform=="win32":
        print("checking for update / outdated pip packages")
        print("it will take 5-10 minutes for checking")
        time.sleep(2)
        os.system("pip list --outdated")
        print("what do u want to uptade ?")
        print("1. all")
        print("2. specific")
        print("3. exit")
        choice = input("enter your choice: ")
        if choice == "1":
            os.system("pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}")

        elif choice == "2":
            print("enter the package name")
            package = input("enter the package name: ")
            os.system("pip install --upgrade "+package)
        elif choice == "3":
            print("exiting")
            sys.exit(1)

    elif platform=="linux" or platform=="linux2":
        # if distro kali, then using apt get install grep, if distro centos7, then using yum install grep
        import distro
        if distro.id()=="debian" or distro.id()=="ubuntu" or distro.id()=="linuxmint":
            os.system("sudo apt-get install grep")
        elif distro.id()=="centos" or distro.id()=="rhel":
            os.system("sudo yum install grep")
        elif distro.id()=="arch":
            os.system("sudo pacman -S grep")
        elif distro.id()=="fedora":
            os.system("sudo dns install grep")
        elif distro.id()=="opensuse":
            os.system("sudo zypper install grep")
        else:
            pass

        print("checking for update / outdated pip packages")
        print("it will take 5-10 minutes for checking")
        time.sleep(2)
        os.system("sudo pip3 list --outdated")
        print("what do u want to uptade ?")
        print("1. all")
        print("2. specific")
        print("3. exit")
        choice = input("enter your choice: ")
        if choice == "1":
            os.system("sudo pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 sudo pip3 install -U")

        elif choice == "2":
            print("enter the package name")
            package = input("enter the package name: ")
            os.system("sudo pip3 install --upgrade "+package)
        elif choice == "3":
            print("exiting")
            sys.exit()

    else:
        print("platform not supported")
        sys.exit(1)
