class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        lns = []
        i = 0

        while i < len(s):
            num = ""

            while s[i] != "#":
                num += s[i]
                i += 1

            length = int(num)
            i += 1

            word = s[i:i + length]
            lns.append(word)

            i += length

        return lns