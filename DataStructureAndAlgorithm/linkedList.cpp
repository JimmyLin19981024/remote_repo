#include <iostream>
using namespace std;

class Node
{
public:
    double data;
    Node* next;
};

class linkedList
{
public:
    linkedList();
    ~linkedList();
    void diplayList();
    Node* addNewNode(int index, double value);
    int findNode(double value);
    int deleteNode(double value);
private:
    Node* head;
    int length;
};

linkedList::linkedList()
{
    this->head = NULL;
    this->length = 0;
}

linkedList::~linkedList()
{
    Node* next = head;
    Node* cur = NULL;
    while (next!=NULL)
    {
        cur = next;
        next = next.next;
        delete cur;
    }
}

int main(int argc, const char * argv[]) {
    return 0;
}
