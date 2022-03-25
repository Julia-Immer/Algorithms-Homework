import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode = False, isWordEnd = False):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isWordEnd = isWordEnd # is this node a word ending node
        self.isRoot = isRootNode # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mapping each character from a-z to 
                       # the child node if any corresponding to that character.


    def addWord(self, word):
        assert(len(word) > 0)
        assert(self is not None)
        assert(isinstance(word, str))
        curr_node = self # keeping track of current node
        word_so_far = ""
        # start at root and check if any of the children, 
        # items in the self.next dictionary, have a letter shared

        for i in range(len(word)) :
            word_so_far += word[i]
            if word_so_far not in curr_node.next :
                # create a new Trie node with this letter added to its dictionary
                new_node = MyTrieNode()
                curr_node.next[word_so_far] = new_node
            
            curr_node = curr_node.next[word_so_far] #advance to the next node

            if i >= len(word) - 1 : # we're at the end of the word
                curr_node.isWordEnd = True
                curr_node.count += 1

        return
          


    def lookupWord(self, word):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur. 
        freq_count = 0
        assert(len(word) > 0)
        assert(self is not None)
        assert(isinstance(word, str))
        curr_node = self # keeping track of current node
        word_so_far = ""
        # start at root and check if any of the children, 
        # items in the self.next dictionary, have a letter shared

        for i in range(len(word)) :
            word_so_far += word[i]
            if word_so_far not in curr_node.next :
                return 0

            curr_node = curr_node.next[word_so_far] #advance to the node with that key

            if (i >= len(word) - 1) and (curr_node.isWordEnd) : # we're at the end of the word
                freq_count = curr_node.count

        return freq_count
    

    def autoComplete(self, word):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #BFS type traversal
        
        return [('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)] # ToDo: change this line, please

# TESTS #

t= MyTrieNode(True) # Create a root Trie node
lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']
# Insert the words in lst1
for w in lst1:
    t.addWord(w)
    
# Perform lookups
j = t.lookupWord('testy') # should return 0
j2 = t.lookupWord('telltale') # should return 0
j3 = t.lookupWord ('testing') # should return 2

# Run autocompletes
lst3 = t.autoComplete('pi')
print('Completions for \"pi\" are : ')
print(lst3)

lst4 = t.autoComplete('tes')
print('Completions for \"tes\" are : ')
print(lst4)