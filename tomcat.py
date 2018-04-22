import os,os.path
import sys

dir='C:\\Tomcat\\apache-tomcat-8.5.30\\bin\\'

def start():
        os.chdir(dir)
        os.startfile("startup.bat")

def stop():
        os.chdir(dir)
        os.startfile("shutdown.bat")

def main():
                
        choice=sys.argv[1]
        if choice.lower() == "start":
                start()
                print("\nSTARTING TOMCAT........\n")
        if choice.lower() == "stop":
                stop()
                print("\nSTOPING TOMCAT........\n")

if __name__ == "__main__":
        main()

