class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth=0
        def helper(i,depth):
            node_depth=0
            temp=i
            while temp<len(traversal) and traversal[temp]=="-":
                node_depth+=1
                temp+=1
            if node_depth>depth:
                node_val=""
                while temp<len(traversal) and traversal[temp]!="-":
                    node_val+=traversal[temp]
                    temp+=1
                node_val=int(node_val)
                node_val=TreeNode(node_val)
                out=helper(temp,depth+1)
                node_val.left=out[0]
                out2=helper(out[1],depth+1)
                node_val.right=out2[0]
                return [node_val,out2[1]]
            else:
                return [None,i]
        depth=0
        root=""
        temp=0
        while temp<len(traversal) and traversal[temp]!="-":
            root+=traversal[temp]
            temp+=1
        root=int(root)
        root=TreeNode(root)
        out=helper(temp,depth)
        root.left=out[0]
        out2=helper(out[1],depth)
        root.right=out2[0]
        return root