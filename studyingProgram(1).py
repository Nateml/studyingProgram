import random
import pickle
import time
import sys

def load_set(path):
    name = input("Name of the set you would like to load: \n")
    with open("%s.pickle" % (name), "rb") as read:
        definitions = pickle.load(read)

    if path == "3":
        print("Current dictionary:\n")
        for key in definitions:
            print(key + " --> " + definitions[key])
        loop = 0
        while True:
            if loop == 0:
                print("\nEnter data as --> <Word> : <Definition>")
            arguments = input("")

            if arguments.lower() == "complete":
                print("Dictionary updated")
                save_out = open("%s.pickle" % (name), "wb")
                pickle.dump(definitions, save_out)
                save_out.close()
                break
                
            key, value = arguments.split(" : ")
            definitions[key] = value
            loop += 1

    return definitions

def create_set():
    definitions = dict()
    loop = 0
    while True:
        if loop == 0:
            print("Enter the word with its definition seperate by a colon (term : comma):\n(When all the words have been inputted, type 'complete').")
        arguments = input("\r")
        if arguments.lower() == "complete":
            print("Your dictionary:\n")
            for key in definitions:
                print(key + " --> " + definitions[key])
            
            while True:
                savePrompt = input("Would you like to save this dictionary?\nY. Yes\n N. No")
                if savePrompt.upper() == "Y":
                    name = input("Name the dictionary: ")
                    save_out = open("%s.pickle" % (name), "wb")
                    pickle.dump(definitions, save_out)
                    save_out.close()
                    break
                elif savePrompt.upper() == "N":
                    break
                else:
                    print("Error - invalid option\nPlease enter either: Y or N")
            break

        key, value = arguments.split(" : ")
        definitions[key] = value
        loop += 1
    return definitions
    


run = input("Would you like to: \n1. Create a new set of terms \n2. Load a saved set of terms\n3. Add to an existing set\n")
if run == "1":
    definitions = create_set()
elif run == "2" or run == "3":
    definitions = load_set(run)

listofkeys = []
for key in definitions:
    listofkeys.append(key)

def getkeyword(listofkeys):
    keyword = random.choice(listofkeys)
    return keyword

def genword(dict, keyword):
    definition = definitions[keyword]
    return definition

def getcorrect(userinput, definition):
    if userinput.lower() == definition.lower():
        return True
    else:
        return False

def get_score(correct, incorrect, time):
    score = ((correct - incorrect)* 10 / time) * 100
    return score

def test_for_term(definitions, listofkeys):
    correct = 0
    incorrect = 0
    total = 0

    x = 1
    print('This is a test program thing')
    print('')

    while x > 0:
        print('Type "help" for a list of commands and an explanation of things...')
        start = input('Or type "start" to start: ')
        if start == 'help':
            print('Once the program starts, to end at anytime: type "end", or "stop')
            print ('')
            print ('The program will present you with one of the defintions for a word/term, just enter the correct term')
            print ('')
            print("answer has to be a 100% match")
            print ("")
            print('The program keeps track of how many answers you get correct and/or incorrect. ')
            print('It also keeps track of how much time it takes for you to answer all the questions, or until you choose to stop the program by typing "stop", or "end"')
            print('')
            n = 1
            while n > 0:
                start = input('Type "start" to start: ')
                if start == 'start':
                    break
        if start != 'start' and start != 'help':
            print ('Invalid command')
        else:
            x -= 1
            start_time = time.time()
    while start == 'start':
        term = getkeyword(listofkeys)
        definition = genword(listofkeys, term)
        print ('def: ', definition)
        userguess = input('term: ')
        if userguess =='end' or userguess == 'stop':
            print('%d correct' % (correct))
            print('%d incorrect' % (incorrect))
            percent_correct = (correct / total) * 100
            print('%d percent correct' % (percent_correct))
            elapsed_time = time.time() - start_time
            print ('That took you %d seconds' % elapsed_time)
            print ('Score: %d' % get_score(correct, incorrect, elapsed_time))
            break
        if getcorrect(userguess, term) is True:
            print('')
            print('Correct')
            print('')
            correct += 1
            listofkeys.remove(term)
        else:
            print('')
            print('Incorrect')
            print('Answer was: %s' % (term))
            print('')
            incorrect += 1
        total += 1

        if len(listofkeys) == 0:
            print('All done!')
            print('%d correct' % (correct))
            print('%d incorrect' % (incorrect))
            percent_correct = (correct / total) * 100
            print('%d percent correct' % (percent_correct))
            elapsed_time = time.time() - start_time
            print ('That took you %d seconds' % elapsed_time)
            print ('Score: %d' % get_score(correct, incorrect, elapsed_time))
            break


test_for_term(definitions, listofkeys)




    

