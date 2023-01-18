#include <iostream>
#include <exception>

#include "DS.h"

struct UnderflowException : public std::exception
{

};

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