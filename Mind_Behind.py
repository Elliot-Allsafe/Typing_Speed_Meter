import time
import sys


def run():
    try:
        test_sentence = "All She wanted was the answer, but she had no idea how much she would hate it. She could not " \
                        "decide " \
                        "of the glass was half empty or half full so she drank it. When he asked her favourite number, " \
                        "she answered without hesitation that it wad diamonds."
        Start = str(input("Press Enter to Start:> "))
        if Start == "":
            start = time.time()
            print(test_sentence)
            Input = str(input("> "))
        else:
            print("Read the Instructions Carefully.")
        while Input != test_sentence:
            if Input == test_sentence:
                end = time.time()
                final = end - start
                wpm = 47 / final
                print(str(int(wpm))+" "+str("WPM"))
            else:
                print("That was not completely correct but here are your Results: \n")
                end = time.time()
                final = end - start
                wpm = 47 / final
                print(str(int(wpm))+" "+str("WPM"))
                sys.exit()
    except KeyboardInterrupt:
        print("Exiting Program!")
        sys.exit()
    except UnboundLocalError:
        # print("Read the Instructions Carefully.")
        sys.exit()
