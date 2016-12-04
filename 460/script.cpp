#include <unordered_map>
class Bin;

class Node {
public:
    int key;
    int value;
    int cnt;
    Bin* pbin;
    Node *next, *prev;
    Node(Bin* b, int k, int v):key(k),value(v),cnt(1),pbin(b){}
};

typedef std::unordered_map<int, Node*> Map;

class Bin {
public:
    int base;
    Node *head, *tail;
    Bin *next, *prev;
    Bin(int b):base(b){
        head = new Node(NULL, -1, -1);
        tail = head;
    }
    ~Bin(){
        delete head;
    }
};

class LFUCache {
    Map map;
    Bin* head;
    unsigned int N;
public:
    LFUCache(int capacity){
        N = capacity;
        head = new Bin(1);
    }
    int get(int key){
        if (N==0)
            return -1;
        auto search = map.find(key);
        if (search == map.end()){
            return -1;
        }
        Node* pnode = search->second;

        int b = pnode->cnt;
        Bin* bin = pnode->pbin;
        if (bin->next == NULL){
            bin->next = new Bin(b+1);
            bin->next->prev = bin;
        }

        if (bin->next->base != b+1){
            Bin* nbin = new Bin(b+1);
            nbin->next = bin->next->next;
            nbin->prev = bin;
            bin->next->prev = nbin;
            bin->next = nbin;
        }
        Bin* bnext = bin->next;

        // remove from counter
        pnode->prev->next = pnode->next;
        if (pnode->next)
            pnode->next->prev = pnode->prev;
        if (pnode == bin->tail)
            bin->tail = pnode->prev;

        if (bin->head->next == NULL && bin->base > 1){
            bin->prev->next = bin->next;
            if (bin->next)
                bin->next->prev = bin->prev;
            delete bin;
        }

        // append to the new bin
        bnext->tail->next = pnode;
        pnode->prev = bnext->tail;
        bnext->tail = pnode;
        pnode->pbin = bnext;
        pnode->next = NULL;

        pnode->cnt ++;

        return pnode->value;
    }

    void set(int key, int value){
        if (N==0)
            return;
        auto search = map.find(key);
        Node *pnode;
        if (search == map.end()){
            if (map.size() == N){
                Bin* bin = head;
                // first bin is special
                if (bin->head->next == NULL)
                    bin = bin->next;
                Node* node = bin->head->next;
                map.erase(node->key);
                node->prev->next = node->next;
                if (node->next)
                    node->next->prev = node->prev;
                if (bin->tail == node)
                    bin->tail = bin->head;
                delete node;
            }

            pnode = new Node(head, key, value);
            map.insert({key, pnode});
            head->tail->next = pnode;
            pnode->prev = head->tail;
            head->tail = pnode;
        }
        else {
            pnode = search->second;
            pnode->value = value;
        }
    }

};

