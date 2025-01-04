class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        # sort spaces
        spaces.sort()

        #prealocate new characters as an array with spaces
        new = [' '] * (len(s) + len(spaces))

        # move left to right, copying characters
        cnt = 0
        for i in range(len(s)):
            # if this index is a space
            if cnt < len(spaces) and i == spaces[cnt]:
                cnt += 1
            
            # update character
            new[i + cnt] = s[i]
        return ''.join(new)
            
