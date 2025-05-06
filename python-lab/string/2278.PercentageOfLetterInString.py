# 2278. Percentage of Letter in String

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if s.count(letter) == 0:
            return 0
        num = s.count(letter) 
        return  int(num / len(s) * 100)
    
    
if __name__ == "__main__":
    s = "foobar"
    letter = "o"
    print(Solution().percentageLetter(s, letter))