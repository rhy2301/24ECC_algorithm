def delete_subtree(tree, node):
    to_delete = [node]
    while to_delete:
        current = to_delete.pop()
        for child in tree[current]:
            to_delete.append(child)
        tree[current] = []  

def count_leaf_nodes(tree, root):
    if not tree[root]:  
        return 1

    leaf_count = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        children = tree[node]
        
        if not children: 
            leaf_count += 1
        else:
            for child in children:
                stack.append(child)
    
    return leaf_count


n = int(input("노드 개수를 입력하세요: "))
parent = list(map(int, input("부모 배열을 입력하세요: ").split()))
delete_node = int(input("삭제할 노드를 입력하세요: "))


tree = [[] for _ in range(n)]
root = -1

for node in range(n):
    if parent[node] == -1:
        root = node
    else:
        tree[parent[node]].append(node)


if delete_node == root:
    print(0)  
else:
    delete_subtree(tree, delete_node)
    print(count_leaf_nodes(tree, root))
