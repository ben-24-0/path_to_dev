class Solution(object):
    def groupAnagrams(self, strs):
        table = {}          # Hash Table

        for word in strs:   # Array of Strings
            key = "".join(sorted(word))  # Sorting + String

            if key not in table:
                table[key] = []
            table[key].append(word)

        return list(table.values())  # Array of Arrays
