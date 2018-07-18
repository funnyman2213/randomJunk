#fucntion deffinition, 
def parsecommand(command): #main parse funcion
    command = command.lower().split() #sanitizes and makes commands predicable
    if command[0] not in commandlist: #makes sure the command is in the list
        #print("IN IF {}".format(command))#debug
        print(help(None)) #if the command isn't in the list it prints out help
    else:
        #print("IN ELSE {}".format(command))#debug
        if command[0] == "help": #if it sees "help" as the first part of the command
            try:
                print(help(command[1])) #tries to print out help for a funcion
            except Exception as e: #catches exceptions
                print(help(None))
                print("ERROR {}".format(e)) #prints default help

def loadFile(path):
    pass #skips over call

def showCharacterInfo(stat, character):
    pass #skips over call

def magicMissle(level):
    pass #skips over call

def help(command=None): #defines the help funcion
    helpoutput={
        "load":"loads a file, proper use \"load [file path]\"",
        "show":"Shows a stat for a character, proper use \"show [name] [stat]\"",
        "help":"shows the help for a command, proper use \"help [commmand]\" or \"help\" for a list of commands",
        "exit":"exit's the program if it's the first parramiter"
    } #represents the different options to output
    if command == None: #watches for help(None)
        catcommandlist = "" 
        for i in commandlist: 
            catcommandlist = catcommandlist + i + ", " #strings commandlist into one variable
        return "list of commands \"{}\"".format(catcommandlist.strip().strip(",")) #prints out all the commands

    else:
        for i in helpoutput: #searches through helpoutput variable for the command
            if command == i: #checks to see if the comman currently indexed is the command inputed
                return helpoutput[i] #returns help output sliced by the input name
        return help(None) #returns the default output

#draw prompt and create loop
commandlist = ("load","show","help","exit")
while True:
    command = input(">") #prints the prompt and sets input
    try:
        parsecommand(command) #sends command input to parsecommand funcion for processing
    except Exception as e: #catches exceptions
        print("ERROR {}".format(e)) #prints out exceptions as "ERROR exception"
    
    if command.lower() == "exit": #waits for "exit" command
        print("goodbye") #says goodbye
        break #exits the loop and finishes the program