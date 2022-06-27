class Solution:
    def simplifyPath(self, path: str) -> str:
        
        places = [p for p in path.split("/") ]
        stack = []
        for p in places:
            if p == "." or p == "":
                continue
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

        