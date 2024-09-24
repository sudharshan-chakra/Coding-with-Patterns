class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        out = ""

        for string in strs:
            out += str(len(string)) + "#" + string
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        out = []
        length = len(s)
        i = 0

        while i < length:
            strlen = ""
            while s[i] != "#":
                strlen += s[i]
                i += 1
            i += 1
            strlen = int(strlen)
            out.append(s[i:i+strlen])
            i += strlen
        
        return out

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))