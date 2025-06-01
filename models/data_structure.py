"""
Linked list but better than those i wrote
- Methods
1. insert : begining
2. append : at the end
3. len : returns length of linkedlist
"""

class Node:
    """ Class Responsible for handling and managing Nodes """
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def __repr__(self):
        return f"Node(value={self.value}, next_node={self.next_node})"
    


class LinkedList:
    """ Class Respinsible for managing Nodes to build a linkedlist """
    def __init__(self):
        self.head_node : Node = None
        self.tail_node : Node = None
        self.__length = 0

    def __len__(self):
        """
        returns length of linked list
        T/C : O(1)
        """
        return self.__length

    def __iter__(self):
        """
        Allows Iteration over linkedlist
        T/C : O(n)
        """
        current_node = self.head_node
        while current_node:
            yield current_node
            current_node = current_node.next_node

    def __reversed__(self):
        """
        Returns a reversed Linkedlist based on values
        T/C : O(n)
        """
        new_linked_list = LinkedList()
        current_node = self.head_node
        while current_node:
            value = current_node.value
            new_linked_list.add(value=value)
            current_node = current_node.next_node
        return new_linked_list
        
    def __repr__(self):
        """
        Linkedlist respresentataion
        time complexity : O(n)
        """
        messages = []
        current_node = self.head_node
        while current_node:
            if current_node == self.head_node:
                message = f"[head: {current_node.value}] ->"
            elif current_node.next_node == None:
                message = f"[tail: {current_node.value}]"
            else:
                message = f"{current_node.value} ->"
            messages.append(message)
            current_node = current_node.next_node
        return " ".join(str(msg) for msg  in messages)
            

    # INSERT OPERATIONS (add, append, insert)
    def add(self, value):
        """
        Adds new values to the head of linkedlist
        T/C : O(1) -> Head insert
        """
        new_node = Node(value=value)
        if self.head_node == None:
            self.head_node = self.tail_node = new_node
        else:
            new_node.next_node = self.head_node
            self.head_node = new_node
        self.__length += 1

    
    def append(self, value):
        """
        Adds new values to the tail of linkedlist
        T/C : O(1) -> Tail insert
        """
        if self.head_node is None:
            self.add(value=value)
        else:
            if self.tail_node != None:
                new_node = Node(value=value)
                self.tail_node.next_node = new_node
                self.tail_node = new_node
                self.__length += 1

    def insert(self, value, index:int):
        """
        Inserts new element at any given arbitary position
        T/C : O(n)
        """
        ## Handling 3 cases : 1. head : 0, tail: -1 or len(ll) -1
        if  index not in [x for x in range(self.__length)]:
            raise ValueError("Index out of bounds")
            
        if index == 0:
            self.add(value=value)
        elif index == self.__length -1:
            self.append(value=value)
        else:
            position = 1
            current_node = self.head_node
            while current_node and position < index:
                current_node = current_node.next_node
                position += 1

            ## inserting new node
            new_node = Node(value=value)
            next_node = current_node.next_node
            new_node.next_node = next_node
            current_node.next_node = new_node
            self.__length += 1
        
    
    ## DELETE OPERATIONS (pop_head, pop, clear)
    def clear(self):
        """
        Clears all references made to head and tail node
        T/C : O(1)
        """
        self.head_node = None
        self.tail_node = None
        self.__length = 0

    def pop(self):
        """
        Removes last element/ node from Linkedlist and returns its value
        T/C: O(n)
        """
        if self.__length == 1:
            pop_node = self.head_node
            self.clear()
            return pop_node

        current_node = self.head_node
        while current_node:
            if current_node.next_node and current_node.next_node.next_node == None:
                pop_node = self.tail_node
                current_node.next_node = None
                self.tail_node = current_node
                self.__length -= 1
                return pop_node
            current_node = current_node.next_node
        return None

    def pop_head(self):
        """
        Removes First element/node from LinkedList and returns its value
        T/C : O(1)
        """
        if self.head_node == None:
            return None
        pop_node = self.head_node
        self.head_node = self.head_node.next_node
        self.__length -= 1
        return pop_node

    def remove(self, value):
        """
        Removes first value occurernce from the list
        T/C :  O(n)
        """
        if self.head_node.value == value:
            self.pop_head()
            self.__length -= 1
            return
            
        current_node = self.head_node
        while current_node:
            if current_node.next_node and current_node.next_node.value == value:
                main_node = current_node.next_node
                current_node.next_node = main_node.next_node
                self.__length -=1
                break
            current_node = current_node.next_node