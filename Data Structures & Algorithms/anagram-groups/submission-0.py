class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
    
        for word in strs:
            # Sort the letters of the word to create a key (e.g., 'tea' -> 'aet')
            sorted_word = "".join(sorted(word.lower()))
            # Append the original word to the list of its anagram key
            anagram_groups[sorted_word].append(word)
            
        return list(anagram_groups.values())
            
            


