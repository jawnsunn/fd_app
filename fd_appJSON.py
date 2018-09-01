import json
frameDataDef = "Damage \t Startup \t  Active \t Recovery \t Block Adv \t  Guard"

def frameDataRead(n):
    print ("Reading frame data for: ", n)

    with open('FrameDataUNI.json', 'r') as fd: #using FrameDataUNI.json and opening it for read-only purposes.
        FrameData = json.load(fd)

    if n == "Linne":
        linne5A = (FrameData["Linne"]["5A"]) # Load FrameData into Linne 5A
        print ("Linne 5A")
        print (frameDataDef)
        for i in range (0,6):
            print (linne5A[i], end ='\t\t')
        print ("\n")

        print ("Linne 2A")
        linne2A = (FrameData["Linne"]["2A"])
        print (frameDataDef)
        for i in range (0,6):
            print (linne2A[i], end ='\t\t')
        print ("\n")

        print ("Linne jA")
        linnejA = (FrameData["Linne"]["jA"])
        print (frameDataDef)
        for i in range (0,6):
            print (linnejA[i], end ='\t\t')
        print ("\n")

        print ("Linne jB")
        linnejB = (FrameData["Linne"]["jB"])
        print (frameDataDef)
        for i in range (0,6):
            print (linnejB[i], end ='\t\t')
        print ("\n")

        print ("Linne jC")
        linnejC = (FrameData["Linne"]["jC"])
        print (frameDataDef)
        for i in range (0,6):
            print (linnejC[i], end ='\t\t')
        print ("\n")

        print ("What is the block advantage on Linne 5A? \t\t")
        print (FrameData["Linne"]["5A"][4])
        print ("\n")

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
