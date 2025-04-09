
// Node class
class Node {
    int data;
    Node next; // Change int to Node

    public Node(int data) {
        this.data = data;
        this.next = null; // Initialize next as null
    }
}

// Singly Linked List class
class SinglyLinkedList {
    Node head; // Head of the linked list

    // Insert at the end
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    // Print the linked list
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();

        // Add nodes
        list.append(3);
        list.append(2);
        list.append(4);

        // Print linked list
        list.printList();
    }
}
