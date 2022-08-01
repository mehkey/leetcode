class TextEditor:

    def __init__(self):
        self.c = 0
        self.s = ''

    def addText(self, text: str) -> None:
        self.s = self.s[0:self.c] + text + self.s[self.c:]
        self.c = self.c + len(text)

    def deleteText(self, k: int) -> int:
        new_c = max(0,self.c - k)
        
        self.s = self.s[0:new_c] + self.s[self.c:]
        
        r = abs(self.c - new_c)
        self.c = new_c
        
        return r

    def cursorLeft(self, k: int) -> str:
        self.c = max(0,self.c - k)
        
        return self.s[max(self.c-10,0):self.c]

    def cursorRight(self, k: int) -> str:
        self.c = min(len(self.s),self.c + k)
        
        return self.s[max(self.c-10,0):self.c]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)