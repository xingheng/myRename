
__version__ = '1.0'
__author__ = " Will Han"


import os, sys


def myRename1(dirpath, filePrefix):
    files = os.listdir(dirpath)

    if len(files) <= 0 or filePrefix == '' :
        return

    baseFolder = dirpath[:]
    if dirpath[-1] != '\\' :
        baseFolder += '\\'

    index = 0
    count = 0
    
    for file in files:
        oname = file
        suffixIndex = file.rfind('.')
        if suffixIndex != -1 :
            suffix = file[suffixIndex:]
            oname = file[:suffixIndex]
        else :
            suffix = ''
        
        index += 1
        newname = filePrefix + str(index) + suffix

        if os.path.exists(baseFolder + newname) :
            print "existing file ", newname
            continue
        
        os.rename(baseFolder + file, baseFolder + newname)
        count += 1

    return count


def myRename2(dirpath, subStr):
    files = os.listdir(dirpath)

    if len(files) <= 0 or subStr == '' :
        return

    baseFolder = dirpath[:]
    if dirpath[-1] != '\\' :
        baseFolder += '\\'

    index = 0
    count = 0
    
    for file in files:
        oname = file
        suffixIndex = file.rfind('.')
        if suffixIndex != -1 :
            suffix = file[suffixIndex:]
            oname = file[:suffixIndex]
        else :
            suffix = ''
        
        index += 1

        if oname.find(subStr) == -1 :
            continue
        
        newname = oname.replace(subStr, '') + suffix

        if os.path.exists(baseFolder + newname) :
            print "existing file ", newname
            continue
        
        os.rename(baseFolder + file, baseFolder + newname)
        count += 1

    return count


def printHelp():
    print """
        Usage:
        This program is only for renaming the filename part currently, file extension not included.

        If you want to rename all the files in specified folder with new suffix, go to mode1.
        If you want to remove a specified substring of filename, go to mode2.
        
        For mode 1, three parameters are needed:
            the first one is which mode you choose, "mode1", "mode2" or "modex".
            the second one is the folder path which contains the files to be renamed.
            the third one is the new prefix name of new files.
        For mode 2, the three parameters are:
            the first one is the mode.
            the second one is the folder path.
            the third one is the substring to be removed.

            """

def main():
    
    dirPath = ''
    filePrefix = 'item'
    if len(sys.argv) == 4 :

        sysMode = sys.argv[1]
        dirPath = sys.argv[2]
        filePrefix = sys.argv[3]

        count = 0
        if sysMode == 'mode1' :
            count = myRename1(dirPath, filePrefix)
        elif sysMode == 'mode2' :
            count = myRename2(dirPath, filePrefix)
        else :
            print "Invalid mode."

        print "We finished renaming ", count, " file(s)."
    else :
        printHelp()


if __name__ == '__main__':
    main()
