import json
frameDataDef = "Damage \t Startup \t  Active \t Recovery \t Block Adv \t  Guard"

with open('FrameDataUNI.json', 'r') as fd: #using FrameDataUNI.json and opening it for read-only purposes.
    FrameData = json.load(fd)

def frameDataPrint(name, move):
    # function prints frameData that is defined by Character Name and Character's move.
    # name = character name, usually defined in json file
    # move = character move, defined after character name in json file
    if FrameData.get(name):
        if FrameData[name].get(move): #Double check if both name and move exist in the json file, if it does then print data, else give error msg
            moveData = (FrameData[name][move]) # Load defined FrameData into moveData
            print (name + " " + move)
            print (frameDataDef)
            for i in range (0,6): # start at 0 of array, 6 total slots in array(0-5)
                print (moveData[i], end ='\t\t')
            print ("\n")
        else:
            print ("This character/move does not exist! Check if " + name + " " + move + " " + "is defined in the frame data json file!")
            print ("\n")
    else:
        print ("This character/move does not exist! Check if " + name + " " + move + " " + "is defined in the frame data json file!")
        print ("\n")

def frameDataGather(name, move):
    # Function is same as frameDataPrint(name, move), but it's made more for storing into a variable of some sort for future reference.
    moveData = "                        " #This... is a solution for defining moveData(that is always a string!)
    if FrameData.get(name):
        if FrameData[name].get(move): #Double check if both name and move exist in the json file, if it does then print data, else give error msg
            moveData = (FrameData[name][move]) # Load defined FrameData into moveData
        else:
            return moveData
    else:
        return moveData

    return moveData #Either returned as X amount of slots that are referenced from json file or a blank space.

def frameDataRead(n):
    print ("Reading frame data for: ", n)

    if n == "Linne":
        data5A = frameDataGather("Linne","5A")
        datajA = frameDataGather("Goku","jA")

        print ("What is the startup on Linne 5A?")
        print ("Startup: " + str(data5A[1]) + "\n")
        print ("What is the block advantage on Goku jA?")
        print ("Block Adv: " + str(datajA[5]) + "\n")

        frameDataPrint("Linne","6A")
        frameDataPrint("Goku","jA")
        frameDataPrint("Linne","2A")
        frameDataPrint("Linne","5A")
        frameDataPrint("Linne","5B")
        frameDataPrint("Linne","jA")
        frameDataPrint("Linne","jB")
        frameDataPrint("Linne","jC")

        # print ("Linne 2A")
        # linne2A = (FrameData["Linne"]["2A"])
        # print (frameDataDef)
        # for i in range (0,6):
        #     print (linne2A[i], end ='\t\t')
        # print ("\n")
        #
        # print ("Linne jA")
        # linnejA = (FrameData["Linne"]["jA"])
        # print (frameDataDef)
        # for i in range (0,6):
        #     print (linnejA[i], end ='\t\t')
        # print ("\n")
        #
        # print ("Linne jB")
        # linnejB = (FrameData["Linne"]["jB"])
        # print (frameDataDef)
        # for i in range (0,6):
        #     print (linnejB[i], end ='\t\t')
        # print ("\n")
        #
        # print ("Linne jC")
        # linnejC = (FrameData["Linne"]["jC"])
        # print (frameDataDef)
        # for i in range (0,6):
        #     print (linnejC[i], end ='\t\t')
        # print ("\n")
        #
        # print ("What is the block advantage on Linne 5A? \t\t")
        # print (FrameData["Linne"]["5A"][4])
        # print ("\n")

    # elif n == "Yuzuhira":
    #     print ("Yuzuhira 5A \t\t")
    #     yuzu5A = json.loads(str(FrameData["Yuzuhira"]["5A"]))
    #     print (frameDataDef)
    #     for i in range (0,5):
    #         print (yuzu5A[i], end ='\t\t')
    #     print ("\t\t")
    #
    #     print ("Yuzuhira 2A \t\t")
    #     yuzu2A = json.loads(str(FrameData["Yuzuhira"]["2A"]))
    #     print (frameDataDef)
    #     for i in range (0,5):
    #         print (yuzu2A[i], end ='\t\t')
    #     print ("\t\t")
    #
    # else:
    #     print ("nigga who \t\t")

frameDataRead("Linne")
#frameDataRead("Yuzuhira")
#frameDataRead("Goku")
