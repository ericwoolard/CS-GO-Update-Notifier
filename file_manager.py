# System imports
import io
import json
import os
import sys


##############################
#	   BASIC OPERATIONS
##############################

# Saves string of text to a file
def save(path, data_str, mode='w'):
    path = ensureAbsPath(path)
    try:
        with io.open(path, mode, encoding='utf-8') as f:
            f.write(str(data_str))
    except IOError:
        # This block of code will run if the path points to a file in a
        # non-existant directory.  To fix this, create the necessary
        # director(y/ies) and call this function again to create the file.
        directory = os.path.dirname(path)
        if not os.path.isdir(directory):
            try:
                os.makedirs(directory)
            except OSError as oserr:
                pass
        if os.path.isdir(directory):
            return save(path, data_str, mode)
        else:
            print('Could not write to ' + path)
            return False
    else:
        return True


# Reads text from a file as a string and returns it
def read(path):
    path = ensureAbsPath(path)
    try:
        fileContents = ''
        with open(path) as f:
            fileContents = f.read()
        return fileContents
    except IOError:
        print('Could not find or open file: ' + path)
        return False


# If any relative paths are given, make them relative to the bot's working dir
def ensureAbsPath(path):
    botRootDir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'
    return path if os.path.isabs(path) else botRootDir + path


##############################
#		  JSON FILES
##############################

# Converts object to JSON, then saves it to a file
def saveJson(path, data):
    return save(
        path,
        json.dumps(
            data,
            ensure_ascii=False,
            indent=4,
            separators=(',', ': ')
        )
    )


# Reads text from a file, converts it to JSON, and returns it
def readJson(path):
    f = read(path)
    if f:
        try:
            return json.loads(f)
        except ValueError:
            print('Could not parse JSON file: ' + path)
            return False
    else:
        return False


def updateJson(path, new_id):
    jsonFile = open(path, 'r')
    data = json.load(jsonFile)  # Load json data into the buffer
    jsonFile.close()

    tmp = data['build_ID']
    data['build_ID'] = new_id

    jsonFile = open(path, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()


