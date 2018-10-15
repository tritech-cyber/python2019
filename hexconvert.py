#binarystring.py cwc
def bincon(decimal):
    print(decimal)
    print("********")
    binstr = "" # binstr is a string
    for i in range(8):
        bin = decimal % 2
        decimal = decimal // 2
        #print(bin)
        binstr = binstr + str(bin)
        print(binstr)
    print("-----")
    print(binstr)
def main():
    print("INPUT -1 TO EXIT THE PROGRAM")
    print("INPUT A POSITIVE INTEGER LESS THAN 256")
    done = 0
    while (done >= 0):
        dec = input("INPUT AN INTEGER : ")
        bincon(dec)
        print("done",done)
        done = dec


main()
