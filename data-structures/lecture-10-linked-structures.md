
# Linked Data Structures 

## A Basic Node

<pre>
+-------------+
|cargo|       +---->
|     |  next |
+-----+-------+
</pre>

# Linked Stack Implementation 

## The `_StackNode ` Class
* value
* next_node

## The `Stack` Class
* want:

```Python
   s = Stack() 
```
* all previous code using array implementations should work without modification when the linked implementation is used
* `push ()` uses the __old___ top of the stack

```Python
self._top = _StackNode(value, _self.top)
self._size += 1 #remove from implementation 
```

> The stack itself needs to keep track of the total size.  Nodes are stupid. 

**felt board, wooden nodes, whiteboard magnets, string and velcro**

### Pop()

### is_empty()

```Python
return self._top is None
# Returns true or false
```

- the linked stack `combine` method uses a **helper** method
  - no new nodes are created
  - **never make copies of the data!**
  - temp just points to the old top
  - and a `rhs`
  - never refers to value
  - use to so we never loose track 

`combine` is **O(n)** when implemented this way.

# Linked Queue Implementation 

## The `_QueueNode` Class
  - deciding which way it should face has 1 good answer
  - looks the same as `_StackNode`
  - put the front on the left

## The `Queue` Class
  - front
  - rear
  - size

### Insert
* special  case: front and rear both point to same thing
* rear next of a queue ALWAYS points to none

### Remove
  - from the front
  - similar to stack pop
  - warning when removing the last node
      -  rear must point to None 
  
