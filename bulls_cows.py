class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        s_d={}
        g_d={}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                if secret[i] in s_d:
                    s_d[secret[i]]+=1
                else:
                    s_d[secret[i]]=1
                if guess[i] in g_d:
                    g_d[guess[i]]+=1
                else:
                    g_d[guess[i]]=1
        for digit in s_d:
            if digit in g_d:
                cows+=min(s_d[digit],g_d[digit])
        return (str(bulls)+'A'+str(cows)+'B')
