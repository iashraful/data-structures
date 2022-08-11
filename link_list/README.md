## Link List

### Intro
Link list is a linear dataset where data are not stored sequencially on the memory. Unlike array link list consist of value and next pointer. This is how we can determine where to go in next. Simply the iteration each after each.

### Pros
* **Dynamic Data Structure**. Linked list is a dynamic data structure so it can grow and shrink at runtime by allocating and deallocating memeory. So there is no need to give initial size of linked list. Some of the high level language has this feature in the array like Python's list.
* **Insertion and Deletion**. Unlike array link list is very easy to remove and add new value. Array needed to shift all the remaining items. But in link list we just need to update the pointer.
* **No Memory Wastage**. As link list is dynamic. So, we don't have to daclare a size for it.

### Cons
* **Memory Usage**. More memory is required to store elements in linked list as compared to array. Because in linked list each node contains a pointer and it requires extra memory for itself.
* **Traversal**. Elements or nodes traversal is difficult in linked list. We can not randomly access any element as we do in array by index. For example if we want to access a node at position n then we have to traverse all the nodes before it. So, time required to access a node is large.
* **Reverse Traversing**. In linked list reverse traversing is really difficult. In case of doubly linked list its easier but extra memory is required for back pointer hence wastage of memory.

