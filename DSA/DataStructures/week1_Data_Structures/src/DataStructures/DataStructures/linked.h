/*


Reference: https://cis.stvincent.edu/html/tutorials/swd/lists/lists.html
*/



#include <iostream>
#include <memory>
#include <string>


struct LinkedList {
	int data;
	struct LinkedList* link; // tro toi node ke tiep
};


typedef struct LinkedList* node;

node CreateNode(int value) {

}