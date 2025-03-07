#!/usr/bin/env python3
'''
Validation checks for string to int and float to prevent any errors
'''
def isInt(number):
    try:
        int(number)
        return True
    except:
        return False

def isFloat(number):
    try:
        float(number)
        return True
    except:
        return False

'''
This function is used to determine which version of a flag was used
'''
def isFound(first,second,cmdln):
    data = ''
    try:
        data = cmdln[cmdln.index(first) + 1]
    except:
        data = cmdln[cmdln.index(second) + 1]
    return data
'''
Function that will parse the command line arguments. This might be better served
as a seperate file so this file does not get to large.
'''
def commandLine(cmdln,script_dir):

    if len(cmdln) < 5:
        print("Requiered flags to run: -rd and -gs")
        exit()

    # Variables that will get passed to the scripts
    # Set defaults are shown
    # sisrs_dir = ""      --> 0
    # data_path = ""      --> 1
    # trimed = False      --> 2
    # threads = 1         --> 3
    # genomeSize = 0      --> 4
    # threshold = 1       --> 5
    # minRead = 3         --> 6
    # missing = 0         --> 7
    # addTaxon = False    --> 8
    #addData = False      --> 9
    rtn = [ "" for i in range(10)]

    # Variablese used throughout if's
    bool = True

    # Let the user specify where to place the sisrs output
    if '-dir' in cmdln or '--directory' in cmdln:
        rtn[0] = isFound('-dir','--directory',cmdln)
    else:
        rtn[0] = script_dir

    # Flag to tell us were the raw data is stored
    if '-rd' in cmdln or '--rawData' in cmdln:
        rtn[1] = isFound('-rd','--rawData',cmdln)
    else:
        print("MISSING PATH TO RAW DATA (-rd,--rawData)")
        exit()

    # Determine if the data has been pretrimmed or not
    if '-trm' in cmdln or '--trimmed' in cmdln:
        rtn[2] = True
    else:
        rtn[2] = False

    # Determine the number of the threads to use
    if '-p' in cmdln or '--processors' in cmdln:
        bool = isInt(isFound('-p','--processors',cmdln))
        rtn[3] = int(isFound('-p','--processors',cmdln)) if bool else 1
    else:
        print("DEFAULT NUMBER OF PROCESSORS (-p,--processors) BEING USED: 1")
        rtn[3] = 1

    # Obtain the genomeSize estimation for script 3
    if '-gs' in cmdln or '--genomeSize' in cmdln:
        bool = isInt(isFound('-gs','--genomeSize',cmdln))
        rtn[4] = int(isFound('-gs','--genomeSize',cmdln)) if bool else 0
    else:
        if bool == False:
            print("GENOME SIZE ESTIMATION (-gs,--genomeSize) IS NOT A VALID NUMBER")
        else:
            print("GENOME SIZE ESTIMATION (-gs,--genomeSize) IS REQUEIRED FOR SISRS")
        exit()

    # Get threshold for script 5
    if '-thresh' in cmdln or '--threshold' in cmdln:
        bool = isFloat(isFound('-thresh','--threshold',cmdln))
        rtn[5] = float(isFound('-thresh','--threshold',cmdln)) if bool else 1
        if bool == False:
            print("MINIMUM SITE HOMOZYGOSITY FOR SISRS SITES WAS NOT A VALID NUMBER --> SWITCHED TO 1")
        elif rtn[5] <= 0 or rtn[5] > 1:
            print("MINIMUM SITE HOMOZYGOSITY FOR SISRS SITES MUST BE BETWEEN 0 AND 1  --> SWITCHED TO 1")
            rtn[5] = 1
    else:
        print("DEFAULT THRESHOLD IS BEING USED: 1")
        rtn[5] = 1

    # Gets the minread need to run the 5 script
    if '-mr' in cmdln or '--minread' in cmdln:
        bool = isInt(isFound('-mr','--minread',cmdln))
        rtn[6] = int(isFound('-mr','--minread',cmdln)) if bool else 3

        if bool == False:
            print("MINREAD COVERAGE (-mr,--minread) MUST BE A VALID INTEGER --> SWITCHED TO 3")
        elif rtn[6] < 1:
            print("MINREAD COVERAGE (-mr,--minread) MUST BE GREATER THAN 1 --> SWITCHED TO 3")
            rtn[6]=3
    else:
        print("DEFAULT MINREAD IS BEING USED: 3")
        rtn[6] = 3

    # Gets the allowed amount of missing data from the files
    if '-ms' in cmdln or '--missing' in cmdln:
        bool = isInt(isFound('-ms','--missing',cmdln))
        rtn[7] = int(isFound('-ms','--missing',cmdln)) if bool else 0
        if bool == False:
            print("THE ALLOWED AMOUNT OF MISSING DATA (-ms/--missing) MUST BE A VALID NUMBER --> SWITCHED TO 0")
            rtn[7] = 0
    else:
        print("THE DEFAULT AMOUNT OF MISSING DATA(-ms/--missing) IS BEING USED TO RUN SISRS: 0")
        rtn[7] = 0

    # Deal with adding a taxon
    rtn[8] = True if '-aT' in cmdln else False

    # Deal with adding new data to an existing taxon
    rtn[9] = True if '-aD' in cmdln else False

    return rtn
