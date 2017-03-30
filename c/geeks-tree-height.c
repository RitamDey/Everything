#include<stdio.h>
#include<stdlib.h>


/**
* Geeks for Geeks example of finding binary tree's height
* http://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
**/
struct node 
{
    int data;
    struct node* left;
    struct node* right;
};
 
/* Compute the "maxDepth" of a tree -- the number of 
    nodes along the longest path from the root node 
    down to the farthest leaf node.*/
int maxDepth(struct node* node) 
{
   if (node==NULL) 
       return 0;
   else
   {
       /* compute the depth of each subtree */
       int lDepth = maxDepth(node->left);
       int rDepth = maxDepth(node->right);
       printf("Node: %d's left depth is %d and right depth is %d\n",node->data, lDepth, rDepth);
 
       /* use the larger one */
       if (lDepth > rDepth) 
           return(lDepth+1);
       else if (rDepth > lDepth) 
           return(rDepth+1);
       else if(rDepth == lDepth)
           return lDepth+1;
   }
} 
 
/* Helper function that allocates a new node with the
   given data and NULL left and right pointers. */
struct node* newNode(int data) 
{
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;                                                       
    return(node);
}
   
int main()
{
    struct node *root = newNode(1);
 
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5); 
   
    printf("Hight of tree is %d\n", maxDepth(root));
    return 0;
}


