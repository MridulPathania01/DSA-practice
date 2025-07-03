class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        res = []
        w=set(word)
        def collectSubsequences(a, output):
            if len(a) == 0:
                res.append(output)
                return
            collectSubsequences(a[1:], output + a[0])
            collectSubsequences(a[1:], output)

        collectSubsequences(word, "")
        v = [seq for seq in res if len(seq) >= k and w.issubset(set(seq))]
        return len(set(v))