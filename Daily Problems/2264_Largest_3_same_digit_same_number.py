class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = '\0'
        for index in range(len(num)-2):
            if num[index]==num[index+1]==num[index+2]:
                max_num = max(max_num,num[index])
        return '' if max_num=='\0' else max_num*3
