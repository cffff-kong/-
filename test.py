#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param s string字符串 
# @return string字符串
#
class Solution:
    def removeDuplicateLetters(s):
        """
        去除字符串中的重复字符，保留每个字符第一次出现的位置
        """
        # 记录每个字符最后出现的位置
        last_occurrence = {char: i for i, char in enumerate(s)}
        print(last_occurrence)
        # 结果栈
        stack = []
        # 记录已经在栈中的字符
        in_stack = set()
        
        for i, char in enumerate(s):
            print(i, char)
            # 如果字符已经在结果中，跳过
            if char in in_stack:
                continue
                
            # 如果栈不为空，且栈顶元素大于当前字符，且栈顶元素在后面还会出现，则弹出栈顶
            while (stack and 
                stack[-1] > char and 
                last_occurrence[stack[-1]] > i):
                removed_char = stack.pop()
                in_stack.remove(removed_char)
                
            # 将当前字符加入栈和集合
            stack.append(char)
            in_stack.add(char)
            
        return ''.join(stack)

if __name__ == "__main__":
    s = "bcabc"
    print(Solution.removeDuplicateLetters(s))  # 输出 "acdb"