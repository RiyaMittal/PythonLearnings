# A Python program to find first non-repeating character from
# a stream of characters
MAX_CHAR = 256


def findFirstNonRepeating():
    # inDLL[x] contains pointer to a DLL node if x is present
    # in DLL. If x is not present, then inDLL[x] is NULL
    inDLL = [] * MAX_CHAR
    print inDLL

    # repeated[x] is true if x is repeated two or more times.
    #  If x is not seen so far or x is seen only once. then
    # repeated[x] is false
    repeated = [False] * MAX_CHAR
    print repeated


    # Let us consider following stream and see the process
    stream = "geeksforgeeksandgeeksquizfor"
    for i in xrange(len(stream)):
        x = stream[i]
        print "Reading " + x + " from stream"

        # We process this character only if it has not occurred
        # or occurred only once.  repeated[x] is true if x is
        # repeated twice or more.s
        print "x , ord(x), repeated[ord(x)]", x,ord(x),repeated[ord(x)]
        if not repeated[ord(x)]:

            # If the character is not in DLL, then add this
            # at the end of DLL
            if not x in inDLL:
                inDLL.append(x)
                print "appended :",inDLL
            else:
                inDLL.remove(x)
                print "removed "+x+" from inDLL:",inDLL

        if len(inDLL) != 0:
            print "First non-repeating character so far is ",
            print str(inDLL[0])




findFirstNonRepeating()