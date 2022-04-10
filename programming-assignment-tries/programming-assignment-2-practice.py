import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode = False, isWordEnd = False, key = ''):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isWordEnd = isWordEnd # is this node a word ending node
        self.isRoot = isRootNode # is this a root node
        self.count = 0 # frequency count
        self.key = key # keeps track of the string that mapped to this node
        self.next = {} # Dictionary mapping each character from a-z to 
                       # the child node if any corresponding to that character.

    # Returns list of valid words in subtrees of self node
    def dfsFindAllWords(self):
        assert(self is not None)
        subtree_words = []
        node_stack = [self]
        nodes_seen = {}

        while(len(node_stack)) :
            curr_node = node_stack.pop()
            
            if curr_node.key not in nodes_seen :
                nodes_seen[curr_node.key] = curr_node # make sure it's marked as seen
            
                if curr_node.isWordEnd : # get the current word if it is one
                    subtree_words.append((curr_node.key, curr_node.count))

                # add all the neighbors of curr_node
                for key in curr_node.next :
                    if key not in nodes_seen : # add it to the stack
                        node_stack.append(curr_node.next[key])

        return subtree_words


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
                new_node = MyTrieNode(key = word_so_far)
                curr_node.next[word_so_far] = new_node
            
            curr_node = curr_node.next[word_so_far] #advance to the next node

            if i >= len(word) - 1 : # we're at the end of the word
                curr_node.isWordEnd = True
                curr_node.count += 1

        return

    # Helper function to return the node which contains the string word
    def findNode(self, word):
        assert(self is not None, "findNode called a null trie.  Node is None.")
        assert(isinstance(word, str))
        curr_node = self # keeping track of current node
        word_so_far = ""

        # start at root and check if any of the children, 
        # items in the self.next dictionary, have a letter shared
        # walk down the trie checking each new letter added produces a word in trie
        for i in range(len(word)) :
            word_so_far += word[i] # add one letter at a time to find next node
            if word_so_far not in curr_node.next :
                return None

            curr_node = curr_node.next[word_so_far] #advance to the node with that key

        # we reached the node with the word in it by reaching the end of the word
        return curr_node

    def lookupWord(self, word):
        # Return frequency of occurrence of the string word in the trie
        # returns a number for the frequency and 0 if the word does not occur. 
        assert(len(word) > 0)
        freq_count = 0

        word_node = self.findNode(word) # get pointer to node for word fragment
        
        if (word_node is not None) and (word_node.isWordEnd) : # we're at the end of the word
            freq_count = word_node.count

        return freq_count


    def autoComplete(self,word):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        autocompletes = []

        word_node = self.findNode(word) # find node pointed to by word

        if (word_node is not None) and (word_node.isWordEnd) :
            autocompletes.append((word, word_node.count)) # add word if valid word to options
        
        # DFS traversal stopping on each valid word
        autocompletes = word_node.dfsFindAllWords() + autocompletes
        
        return autocompletes

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