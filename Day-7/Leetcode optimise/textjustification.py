from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        a=[]
        current_length = 0

        for word in words:
            if current_length + len(word) + len(a) > maxWidth:
                for i in range(maxWidth - current_length):
                    a[i % (len(a) - 1 or 1)] += ' '
                res.append(''.join(a))
                a=[]
                current_length = 0
            
            a.append(word)
            current_length += len(word)

        res.append(' '.join(a).ljust(maxWidth))
        return res