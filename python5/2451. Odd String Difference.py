
class Solution:
    def oddString(self, words: List[str]) -> str:

        dict_of_changes_count : defaultdict = defaultdict(int)
        dict_of_changes : defaultdict = defaultdict(str)
        
        for word in words:
            
            changes:list[int] = []
            
            for char_id in range(len(word)-1):
                
                change = ord(word[char_id+1]) - ord(word[char_id])  

                changes.append(str(change))
            
            val = '-'.join(changes)

            dict_of_changes_count[val] +=1
            dict_of_changes[val] = word
        
        for k in dict_of_changes_count:
            if dict_of_changes_count[k] == 1:
                return dict_of_changes[k]

