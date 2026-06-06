class Solution:
    def compress(self, chars: List[str]) -> int:
        nw = ""
        count = 1

        for i in range(1, len(chars) + 1):

            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                nw += chars[i - 1]

                if count > 1:
                    nw += str(count)

                count = 1

        chars[:] = list(nw)
        return len(chars)