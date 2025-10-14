class Solution:
    def myAtoi(self, s: str) -> int:
        contains = [i for i in s]
        i=0
        num = 0
        start = 0
        negative = 1
        pn = 0
        ans = ""
        while i < len(contains):
            if contains[i].isdigit():
                num = 1
                if contains[i] != "0":
                    start = 1
                    ans += contains[i]
                    i +=1
                else:
                    if start == 1:
                        ans += contains[i]
                        i +=1
                    else:
                        i +=1

            else:
                if num ==0:
                    if contains[i] not in (" ", "-", "+"):
                        return 0
                    elif pn == 1:
                        return 0
                    else:
                        if contains[i] == " ":
                            i +=1
                        elif contains[i] == "-":
                            negative = -1
                            i +=1
                            pn = 1
                        elif contains[i] == "+":
                            i +=1
                            pn = 1
                else:
                    break
        if ans == '':
            return 0
        else:
            output = int(ans) * negative
            if output < (-2)**31:
                return (-2)**31
            elif output>2**31-1:
                return 2**31-1
            else:
                return output

