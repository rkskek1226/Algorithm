from collections import deque


# 이진 트리의 최대 깊이
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1

        for _ in range(len(q)):
            cur_root = q.popleft()
            if cur_root.left:
                q.append(cur_root.left)
            if cur_root.right:
                q.append(cur_root.right)

    return depth

