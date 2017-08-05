"""
TODO: Make a class that will identify a word that is a palindrome. For example:
HANNAH is a palindrome since it is spelled the same way backwards as forwards.
DAMIEN is not. That's cause I'm cooler :P (jk)
"""

class Word():
    """
    This is a Word class. You can make mulitple instances/objects of it (aka multiple words).
    For example:
    >>> hannah = Word('hannah')
    >>> damien = Word('damien')
    >>> hannah.reverse()
    >>> damien.reverse()
    >>> print hannah.getWord()
    hannah
    >>> print damien.getWord()
    neimad

    Classes have public methods and private methods. Private methods are denoted by the underscore on the front (aka _).
       Private methods should not be called outside of the class. So notice in the above example we didn't call
       hannah._reverse('hannah') because that's a private method. Notice that reverse() is allowed to call _reverse() because
       it's inside the class.
    """
    def __init__(self, word):
        """
        This takes in a string and stores it in the private attribute _word.
        """
        self._word = word

    def getWord(self):
        return self._word

    def _reverse(self, word):
        """
        This reverses the order of the letters in a word and returns the reversed word.
        """
        reversed_word = ""
        for position in range(len(word)-1, -1, -1):
            reversed_word = reversed_word + word[position]
        return reversed_word

    def reverse(self):
        """
        This reverses the order of the letters in the word.
        """
        self._word = self._reverse(self._word)

    def is_palindrom(self):
        """
        This returns True if the word is a palindrome and False otherwise.
        """
        # WRITE YOUR CODE HERE
        # if palindrome
        return True
        # else
        return False


if __name__ == '__main__':
    first_name = input("Please enter first name:")
    name = Word(first_name)
    name.reverse()
    print("Did you know your name spelled backwards is {}?".format(name.getWord()))
    name.reverse() # reverse it back
    if name.is_palindrom():
        print("Did you know your name is a palindrome?")
