# Binary Tree

A data structure that consist of nodes in a **parent/child** relationship.

## Examples

* Think of a **tree** with multiple *branches* and *leaves*.

## Terminology

* **Root** - The *top* node in a tree
* **Child** - A Node directly connected to a (Parent) Node when moving away from Root.
* **Parent** - The converse notion of a Child
* **Siblings** - A group of Nodes with the same Parent
* **Leaf** - A Node with no Children
* **Edge** - The connection between one Node and another

## Use Cases

* HTML DOM - Javascript Object Model
* Network Routing
* **A**bstract **S**yntax **T**rees (AST) - to model code and logic
* Artificial Intelligence - Imagine you're trying to model all the possible moves in a Tic-tac-toe game.
* Folders in _Operating Systems_

## Kinds of Trees

* **Trees** - each node can have *any number* of children.
* **Binary Trees** - each node can have at most **two** children.
* **Binary Search Trees (BST)**
  * each node can have at most **two** children.
  * BSTs are meant to model data that's _sorted_ and _comparable_
    * To the _left_ are numbers **smaller**, to the _right_ are numbers **bigger**

## Big O (BST only)

* Insertion - **O(log N)**
* Searching - **O(log N)**
  * *Not guaranteed*
    * What if you have a small number like 1 as the root, and all other numbers are larger than 1 (the root)
