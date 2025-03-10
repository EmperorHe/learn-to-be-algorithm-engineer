# 232.用栈实现队列
"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
"""

class MyQueue:

    def __init__(self):
      # 通过两个栈，一个in，一个out来模拟队列的先进先出效果
      self.stack_in = []
      self.stack_out = []

    def push(self, x: int) -> None:
      self.stack_in.append(x)

    def pop(self) -> int:
      # 判断是否为空
      if self.empty():
        return None

      if len(self.stack_out) > 0:
        return self.stack_out.pop()
      else:
        while self.stack_in:
          out = self.stack_in.pop()
          self.stack_out.append(out)
        return self.stack_out.pop()

    def peek(self) -> int:
      res = self.pop()
      self.stack_out.append(res)
      return res        

    def empty(self) -> bool:
      return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()