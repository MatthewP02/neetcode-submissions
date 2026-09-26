class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {letter: s.count(letter) for letter in set(s)}
        t_count = {letter: t.count(letter) for letter in set(t)}

        return s_count == t_count