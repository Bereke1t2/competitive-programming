class Websit:
    def __init__(self ,url):
        self.url = url
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Websit(homepage) 
        

    def visit(self, url: str) -> None:
        new_web = Websit(url)
        self.curr.next = new_web
        new_web.prev = self.curr
        self.curr = self.curr.next

        

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -=1
        return self.curr.url

        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -=1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)