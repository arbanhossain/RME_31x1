#ifndef DS_H
#define DS_H

#define LIMIT 100

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

#endif