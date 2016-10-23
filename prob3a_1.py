

def StringMatch(target, key):

    count = 0

    temp = target

    index = -1

    while (temp.find(key)) != -1:
 		index = temp.find(key)
 		count = count + 1

 		temp = temp[(index + len(key)):]
 		location = len(target) - len(temp)-1

 		print "location of", count, "match in target:", location
 		

StringMatch("abcdabcdabcdabcd", "bc")


