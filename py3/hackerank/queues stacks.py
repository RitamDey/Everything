""""
    The solution contains all the code I wrote and the stub code provided by the problem setter
"""
import sys

class Solution:
  
  def __init__(self):
    self._stack = []
    self._queue = []
  
  def pushCharacter(self, ch):
    self._stack.append(ch)
  
  def enqueueCharacter(self,ch):
    self._queue.append(ch)
  
  def popCharacter(self):
    return self._stack.pop()

  def dequeueCharacter(self):
    return self._queue.pop(0)


s=input()
obj=Solution()   

l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
