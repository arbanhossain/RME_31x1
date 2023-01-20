#ifndef DS_H
#define DS_H

#define LIMIT 100 // Stack/Queue Limit

// Node prototype
template <typename T> class Node {
  public:
    T data;
    Node<T>* next;
    Node(T value);
};

// Stack Prototype

template <typename T> class Stack {
  private:
    T arr[LIMIT];
    int top;

  public:
    Stack();
    ~Stack();
    bool is_empty();
    void push(T value);
    T pop();
    void display();
};

// Queue Prototype

template <typename T> class Queue {
  private:
    Node<T>* head;
    Node<T>* tail;
  
  public:
    Queue();
    bool is_empty();
    void enqueue(T value);
    T dequeue();
    void display();
};

// Max Heap Prototype

template <typename T> class MaxHeap {
  private:
    T arr[LIMIT];
    int end;
    void reheap_up(int index);
    void reheap_down(int index);
  
  public:
    MaxHeap();
    ~MaxHeap();
    void insert(T value);
    T remove();
};

// Min Heap Prototype

template <typename T> class MinHeap {
  private:
    T arr[LIMIT];
    int end;
    void reheap_up(int index);
    void reheap_down(int index);
  
  public:
    MinHeap();
    ~MinHeap();
    void insert(T value);
    T remove();
};

#endif