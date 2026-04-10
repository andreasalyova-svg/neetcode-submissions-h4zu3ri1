class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            split = list(strs[i])
            print(split)
            count = len(split)
            strs[i] = (f"{str(count)}#{strs[i]}")
            s = "".join(strs)
        if strs == []:
            return ""
        return s

    def decode(self, s: str) -> List[str]:
        lns = []
        i= 0
        num = ""
        split_2 = list(s)


                
        while i < len(split_2):
            while split_2[i] != "#":
                num += split_2[i]
                i += 1
            if split_2[i] == "#":
                length = int(num)
                i += 1
                word = split_2[i: i+length]
                word_str = "".join(word)
                i += length
                lns.append(word_str)
                num = ""
        if s == "":
            return lns
        return lns
