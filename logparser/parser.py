# %%
import re

my_string = "whoa, this is so kewl"

def parselog (linemarker, separator, logfile, vector):
    with open(logfile) as f:
        listNew = list(generateDicts(linemarker, separator, f, vector))
    return listNew

# %%

def generateDicts(beginline, separator, log_fh, vector):
    currentDict = {}
    for line in log_fh:
        if line.startswith(matchBegin(beginline, line)):
            if currentDict:
                yield currentDict
            currentDict = {"date":line.split(separator)[vector[0]], #0
                           "type":line.split(separator)[vector[1]], #2
                           "text":line.split(separator)[-1]} #always return last column
        else:
            currentDict["text"] += line
    yield currentDict

#%%

def matchBegin(beginline, line):
    matchThis = ""
    matched = re.match(beginline,line)
    if matched:
        #matches a date and adds it to matchThis            
        matchThis = matched.group() 
    else:
        matchThis = "NONE"
    return matchThis

#%%
