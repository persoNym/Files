#Victoria
#Project 1
#ITP 295- Python for Cybersecurity
#application will start by asking user for a file to process.  If the file exists, the app will open the existing file.
# Otherwise it will open a new file for reading and writing.Based on selection, the app should then ask user if this is
# for a read or a write operation. if writing, the user should be prompted for n lines of text
# and they should be written to the file.
# if reading, the user should see the contents of the file displayed.  The file should then be graciously closed.
# Key points:  All Input/Output operations should be enclosed in Try Catch blocks.

#!/usr/bin/python
import sys


def main():
    selection = input("Select 1 for Read, Select 2 for Write, Select 0 to Quit. Please input your selection: ")
    if selection == 0:
        print("You have decided to Quit.")
        sys.exit(0)
    elif selection == 1:
        print("You have selected the Read option.")
        try:
            # opens user inputed file for reading
            PFile = raw_input("Please enter name of file for processing: ")
            print("You have entered: " + PFile)
            FRead = open(PFile)
            content = FRead.read()
            print("The content of file is: "+ content)
            # outputs file name and closes file
            FRead.close()
        except IOError as e:
            #creates blank file
            print("File not found. Creating new file")
            FRead = open(PFile,'a')
            FRead.close()
            print("File is empty so will not output contents")
    elif selection == 2:
        print("You have selected the Write option.")
        PFile = raw_input("Please enter name of file for processing: ")
        data = raw_input("Enter data you wish to add to the file: ")
        try:
            print("You have selected: "+ PFile," and have entered " + data)
            with open(PFile, "a") as FWrite:
                FWrite.write(data)
                print("Process Completed")
                FWrite.close()
        except IOError as e:
            print("File not found. Creating new file")
            print("You have entered " + data)
            with open(PFile, "a") as FWrite:
                FWrite.write(data)
                print("Process Completed")
                FWrite.close()
    else:
        print("INVALID OPTION.")
        sys.exit(1)

if __name__ == "__main__":
        main()