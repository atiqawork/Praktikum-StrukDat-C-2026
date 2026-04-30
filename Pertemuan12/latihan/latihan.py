class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")
        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
        self.root.right.right = Node("F")

    def traverse_preorder(self, node):
        hasil = []
        if node:
            hasil.append(node.data)
            hasil += self.traverse_preorder(node.left)
            hasil += self.traverse_preorder(node.right)

        return hasil

    def traverse_inorder(self, node):
        hasil = []
        if node:
            hasil += self.traverse_inorder(node.left)
            hasil.append(node.data)
            hasil += self.traverse_inorder(node.right)
        return hasil

    def traverse_postorder(self, node):
        hasil = []
        if node:
            hasil += self.traverse_postorder(node.left)
            hasil += self.traverse_postorder(node.right)
            hasil.append(node.data)
        return hasil
    
    def get_leaf_nodes(self, node, leaves=None):
        if leaves is None:
            leaves = []
        if node:
            if node.left is None and node.right is None:
                leaves.append(node.data)

            self.get_leaf_nodes(node.left, leaves)
            self.get_leaf_nodes(node.right, leaves)
        return leaves


p1 = BinaryTree()

print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
print("======================================")
print("[INFO] Membangun Struktur Gudang...")

p1.insert_manual()

print("[INFO] Struktur berhasil dibuat.\n")
print("HASIL AUDIT:")

preorder = p1.traverse_preorder(p1.root)
inorder = p1.traverse_inorder(p1.root)
postorder = p1.traverse_postorder(p1.root)
leaf_nodes = p1.get_leaf_nodes(p1.root)

print("1. Pre-Order  :", " - ".join(preorder))
print("2. In-Order   :", " - ".join(inorder))
print("3. Post-Order :", " - ".join(postorder))

print("\n[DATA] Gudang Ujung (Leaf Nodes):", ", ".join(leaf_nodes))

print("======================================")
print("Audit Selesai!")