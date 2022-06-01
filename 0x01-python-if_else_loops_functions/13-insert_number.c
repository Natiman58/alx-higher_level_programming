#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <string.h>

/**
 * insert_node - inserts a node with value "number"
 * in a sorted list
 * @head: pointer to the first element of the linked list
 * @number: the number to be inserted
 * Return: the adress of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new;
listint_t *current;
int key;
current = *head;

new = malloc(sizeof(listint_t));
if (new == NULL)
	return (NULL);
new->n = number;
new->next = NULL;

if (*head == NULL)
	*head = new;
else
{
key = new->n;
while (current->next != NULL && current->next->n < key)
	current = current->next;
new->next = current->next;
current->next = new;
}
return (new);
}
