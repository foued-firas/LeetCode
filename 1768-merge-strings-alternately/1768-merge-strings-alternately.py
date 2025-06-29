class Solution(object):
    def mergeAlternately(self, word1, word2):
        if len(word1) >= 1 and len(word2) >= 1:
            word1 = word1.lower()
            word2 = word2.lower()
            merged = []
            
            if len(word1) == len(word2):
                k = len(word2)
                for i in range(k):
                    merged.append(word1[i])
                    merged.append(word2[i])
            
            elif len(word1) > len(word2):
                k = len(word2)
                for i in range(k):
                    merged.append(word1[i])
                    merged.append(word2[i])
                merged.extend(word1[k:])  
            
            else:
                k = len(word1)
                for i in range(k):
                    merged.append(word1[i])
                    merged.append(word2[i])
                merged.extend(word2[k:])  
            
            resultat = ''.join(merged)
            return resultat
        else:
            return ""
