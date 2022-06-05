#include "lists.h"
/**
 * reverse - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *temp = *head;
	listint_t *temp2 = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			temp2 = slow_ptr->next;
			break;
		}
		if (!fast_ptr->next)
		{
			temp2 = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}

	reverse(&temp2);

	while (temp2 && temp)
	{
		if (temp->n == temp2->n)
		{
		temp2 = temp2->next;
		temp = temp2->next;
		}
		else
			return (0);
	}
	if (!temp2)
		return (1);
	return (0);
