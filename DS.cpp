#include <iostream>
#include <exception>

#include "DS.h"

// Exceptions

struct UnderflowException : public std::exception { };

// Node Implementation

template <typename T> Node<T>::Node(T value) {
  next = NULL;
  data = value;
}

// Stack Implementation

template <typename T> Stack<T>::Stack() {
  top = -1;
}

template <typename T> Stack<T>::~Stack() {
  delete[] arr;
}

template <typename T> bool Stack<T>::is_empty() {
  return top == -1;
}

template <typename T> void Stack<T>::push(T value) {
  if (top == LIMIT - 1) {
    std::cout << "Stack Overflow. Cannot push." << std::endl;
  } else {
    arr[++top] = value;
  }
}

template <typename T> T Stack<T>::pop() {
  if (is_empty()) {
    throw UnderflowException();
  }
  return arr[top--];
}

template <typename T> void Stack<T>::display() {
  if (top == -1) {
    std::cout << "Stack is empty." << std::endl;
    return;
  }
  for (int i = 0; i <= top; i++) {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;
}

// Queue Implementation

template <typename T> Queue<T>::Queue() {
  head = NULL;
  tail = NULL;
}

template <typename T> bool Queue<T>::is_empty() {
  return head == NULL;
}

template <typename T> void Queue<T>::enqueue(T value) {
  Node<T> *node  = new Node<T>(value);
  if (head == NULL) {
    head = node;
    tail = node;
  } else {
    tail->next = node;
    tail = node;
  }
}

template <typename T> T Queue<T>::dequeue() {
  if (is_empty()) {
    throw UnderflowException();
  }
  Node<T> *node = head;
  T value = node->data;
  head = head->next;
  delete node;
  return value;
}

template <typename T> void Queue<T>::display() {
  if (is_empty()) {
    std::cout << "Queue is empty." << std::endl;
    return;
  }
  Node<T> *node = head;
  while (node != NULL) {
    std::cout << node->data << " ";
    node = node->next;
  }
  std::cout << std::endl;
}

// Max Heap Implementation

template <typename T> MaxHeap<T>::MaxHeap() {
  end = -1;
}

template <typename T> MaxHeap<T>::~MaxHeap() {
  delete[] arr;
}

template <typename T> void MaxHeap<T>::reheap_up(int index) {
  if (index == 0) {
    return;
  }
  int parentIdx = (index - 1) / 2;
  if (arr[parentIdx] < arr[index]) {
    T temp = arr[parentIdx];
    arr[parentIdx] = arr[index];
    arr[index] = temp;
    reheap_up(parentIdx);
  }
}

template <typename T> void MaxHeap<T>::reheap_down(int index) {
  int leftIdx = 2 * index + 1;
  int rightIdx = 2 * index + 2;
  if (leftIdx > end) {
    return;
  } else if (rightIdx > end) {
    if (arr[index] < arr[leftIdx]) {
      T temp = arr[index];
      arr[index] = arr[leftIdx];
      arr[leftIdx] = temp;
      reheap_down(leftIdx);
    }
  } else {
    if (arr[leftIdx] > arr[rightIdx]) {
      if (arr[index] < arr[leftIdx]) {
        T temp = arr[index];
        arr[index] = arr[leftIdx];
        arr[leftIdx] = temp;
        reheap_down(leftIdx);
      }
    } else {
      if (arr[index] < arr[rightIdx]) {
        T temp = arr[index];
        arr[index] = arr[rightIdx];
        arr[rightIdx] = temp;
        reheap_down(rightIdx);
      }
    }
  }
}

template <typename T> void MaxHeap<T>::insert(T value) {
  if (end == LIMIT - 1) {
    std::cout << "Heap is full. Cannot insert." << std::endl;
  } else {
    arr[++end] = value;
    reheap_up(end);
  }
}

template <typename T> T MaxHeap<T>::remove() {
  if (end == -1) {
    throw UnderflowException();
  }
  T value = arr[0];
  arr[0] = arr[end--];
  reheap_down(0);
  return value;
}

// Min Heap Implementation

template <typename T> MinHeap<T>::MinHeap() {
  end = -1;
}

template <typename T> MinHeap<T>::~MinHeap() {
  delete[] arr;
}

template <typename T> void MinHeap<T>::reheap_up(int index) {
  if (index == 0) {
    return;
  }
  int parentIdx = (index - 1) / 2;
  if (arr[parentIdx] > arr[index]) {
    T temp = arr[parentIdx];
    arr[parentIdx] = arr[index];
    arr[index] = temp;
    reheap_up(parentIdx);
  }
}

template <typename T> void MinHeap<T>::reheap_down(int index) {
  int leftIdx = 2 * index + 1;
  int rightIdx = 2 * index + 2;
  if (leftIdx > end) {
    return;
  } else if (rightIdx > end) {
    if (arr[index] > arr[leftIdx]) {
      T temp = arr[index];
      arr[index] = arr[leftIdx];
      arr[leftIdx] = temp;
      reheap_down(leftIdx);
    }
  } else {
    if (arr[leftIdx] < arr[rightIdx]) {
      if (arr[index] > arr[leftIdx]) {
        T temp = arr[index];
        arr[index] = arr[leftIdx];
        arr[leftIdx] = temp;
        reheap_down(leftIdx);
      }
    } else {
      if (arr[index] > arr[rightIdx]) {
        T temp = arr[index];
        arr[index] = arr[rightIdx];
        arr[rightIdx] = temp;
        reheap_down(rightIdx);
      }
    }
  }
}

template <typename T> void MinHeap<T>::insert(T value) {
  if (end == LIMIT - 1) {
    std::cout << "Heap is full. Cannot insert." << std::endl;
  } else {
    arr[++end] = value;
    reheap_up(end);
  }
}

template <typename T> T MinHeap<T>::remove() {
  if (end == -1) {
    throw UnderflowException();
  }
  T value = arr[0];
  arr[0] = arr[end--];
  reheap_down(0);
  return value;
}