
#!/usr/bin/python3
def word_chain(global_set):
    """Wrapping function, which launches recursive chain_builder function on the particular word in given list,
    consequently gathers all chains into final_chain_list. Finally it extracts the longest chain from the list
    and returns it. If there are more than one longest chain, word_chain will return all of them.
    
    The function is a bit bulky but robust enough to digest words where word[0] == word[-1].
    Such words usualy result in RecursionError in alterantive solutions (from StackOverflow or elsewhere). 

    Args:
        global_set (set): set with str to create word chains

    Returns:
        list: one or more longest word chains
    """
    # try to implement dynamic programming here in form {(curr_chain.split(';')[-1], words_left)}
    # only if having some time at the end
    
    def chain_builder(curr_chain, words_left):
        """Recursive function which is generating word strings for each word in the given list

        Args:
            curr_chain (str): current word or word chain
            words_left (list): List of words, remained to check for particular word chain 

        Returns:
            list: returns list with all possible word chains, 
        """
        words_left = words_left[:]
        # deleting current word from the words_left
        words_left.remove(curr_chain.split(';')[-1])
        # provisional storage of chains
        curr_chain_list = []
        
        # base case
        # if no suitable candidate left in the words_left - append resulting chain into the curr_chain_list
        if curr_chain[-1] not in list(map(lambda x: x[0], words_left)):
            curr_chain_list.append(curr_chain.split(';'))
        else:
            # iterate through the words_left (guarantees that all candidate-words will be checked)
            for cand_word in words_left:
                if curr_chain[-1] == cand_word[0]:
                  # Here we will get list of lists, to get normal list (without crazy nested structures) I  use extend
                    curr_chain_list.extend(chain_builder(curr_chain +';'+ cand_word, words_left))
        return curr_chain_list
    
    # We have to convert global_set to a list (to avoid RecursionError with words starting and ending with the same letter)
    global_set = list(global_set)
    # Using chain_builder for every element of global_set
    final_chain_list = []
    for i in global_set:
        final_chain_list.extend(chain_builder(i, global_set))
    # According to the task - we should return a string. 
    # Let it be a list of strings - as we can get several longest chains sometimes.
    longest_chains = [" - ".join(x) for x in final_chain_list if len(x) == len(max(final_chain_list, key=len))]
    return longest_chains

  
if __name__ == "__main__":     
    long_chains = word_chain({'goose', 'dog', 'ethanol'})
    print(*long_chains)

