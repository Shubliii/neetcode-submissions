class Solution:
    def simplifyPath(self, path: str) -> str:

        # Split path by '/' and process each part
        # ""  -> ignore (extra slashes //)
        # "." -> ignore (current directory)
        # ".."-> pop (go to parent directory)
        # else-> push (valid folder name, even "..." or "....")


        stack=[]


        for folder in path.split("/"):

            if folder=="" or folder==".":
                continue

            if folder=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)


        return "/" + "/".join(stack)        
        