'''
Created on Nov 18, 2013

@author: Yaron
'''
import string

def hello_foo(name):
    return 'hello %s' % name

def beers_on_the_wall(num):
    beers = range(1,num+1)
    beers.reverse()
    return ("%i bottles of beer on the wall, %i bottles of beer.\
    Take one down, pass it around, %i bottles of beer on the wall...\n" % (x,x,x-1) for x in beers) 

def gematria(letter):
    """
    Returns the gimatric value of hebrew letters
    """
    pass

def palindrome(inp):
    #word = str(inp)
    s = inp.translate(string.maketrans("",""), string.punctuation)
    length = len(s)/2 + 1 if (len(s) % 2 == 1) else len(s) / 2
    return s[:length] == s[:-length-1:-1]
    
    

if __name__ == '__main__':
    assert hello_foo('yaron') == 'hello yaron'
    beers_on_the_wall(5)
    
    print 'OK'