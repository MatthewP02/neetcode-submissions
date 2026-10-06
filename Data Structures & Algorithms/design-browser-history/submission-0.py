class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url)
        temp = self.current
        self.current = self.current.next
        self.current.prev = temp

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.prev:
                break
            self.current = self.current.prev
        
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.next:
                break
            self.current = self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)