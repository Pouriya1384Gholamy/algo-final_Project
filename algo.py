class BSTNode:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insertRequest(self, id, name):
        self.root = self._insert(self.root, id, name)

    def _insert(self, node, id, name):
        if not node:
            return BSTNode(id, name)
        if id < node.id:
            node.left = self._insert(node.left, id, name)
        elif id > node.id:
            node.right = self._insert(node.right, id, name)
        return node

    def searchRequest(self, id):
        return self._search(self.root, id)

    def _search(self, node, id):
        if not node or node.id == id:
            return node
        if id < node.id:
            return self._search(node.left, id)
        else:
            return self._search(node.right, id)

    def deleteRequest(self, id):
        self.root = self._delete(self.root, id)

    def _delete(self, node, id):
        if not node:
            return None
        if id < node.id:
            node.left = self._delete(node.left, id)
        elif id > node.id:
            node.right = self._delete(node.right, id)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._minValueNode(node.right)
            node.id, node.name = min_larger_node.id, min_larger_node.name
            node.right = self._delete(node.right, min_larger_node.id)
        return node

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def printBST(self):
        print("BST Pre-order Traversal:")
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(f"(ID: {node.id}, Name: {node.name})", end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def isEmpty(self):
        return self.root is None

    def sizeBST(self):
        return self._size(self.root)

    def _size(self, node):
        if not node:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertHeap(self, id, priority):
        self.heap.append((priority, id))
        self._heapify_up(len(self.heap) - 1)

    def deleteMaxHeap(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        max_item = self.heap.pop()
        self._heapify_down(0)
        return max_item

    def processHighestPriorityRequest(self, bst):
        if not self.heap:
            print("No requests to process.")
            return
        priority, id = self.deleteMaxHeap()
        bst.deleteRequest(id)
        print(f"Processed request ID {id} with priority {priority}.")

    def increasePriority(self, id, newPriority):
        for i, (priority, _id) in enumerate(self.heap):
            if _id == id:
                if newPriority > priority:
                    self.heap[i] = (newPriority, id)
                    self._heapify_up(i)
                    return True
        return False

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[parent][0]:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def printMaxHeap(self):
        print("MaxHeap Level Order:")
        for priority, id in self.heap:
            print(f"(ID: {id}, Priority: {priority})", end=" ")
        print()

    def isEmpty(self):
        return len(self.heap) == 0

    def sizeMaxHeap(self):
        return len(self.heap)


def main():
    bst = BST()
    heap = MaxHeap()

    print("\n--- Request Management System ---")
    print("1. Add new request")
    print("2. Search request by ID")
    print("3. Delete request by ID")
    print("4. Process highest priority request")
    print("5. Increase priority of a request")
    print("6. Print BST")
    print("7. Print MaxHeap")
    print("8. Exit")
    while True:
        choice = input("Choose an option: ")

        if choice == "1":
            id = int(input("Enter request ID: "))
            name = input("Enter user name: ")
            priority = int(input("Enter priority: "))
            bst.insertRequest(id, name)
            heap.insertHeap(id, priority)

        elif choice == "2":
            id = int(input("Enter ID to search: "))
            node = bst.searchRequest(id)
            if node:
                print(f"Found: (ID: {node.id}, Name: {node.name})")
            else:
                print("Request not found.")

        elif choice == "3":
            id = int(input("Enter ID to delete: "))
            bst.deleteRequest(id)
            print("Deleted from BST (not removed from MaxHeap automatically).")

        elif choice == "4":
            heap.processHighestPriorityRequest(bst)

        elif choice == "5":
            id = int(input("Enter ID: "))
            new_priority = int(input("Enter new priority: "))
            if heap.increasePriority(id, new_priority):
                print("Priority updated successfully.")
            else:
                print("Request not found or priority not increased.")

        elif choice == "6":
            bst.printBST()

        elif choice == "7":
            heap.printMaxHeap()

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
