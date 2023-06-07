#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle to it
 * @list: the first list in a linked list
 *
 * Return: 0 if there is no cyle 1 if there is one
 */
int check_cycle(listint_t *list)
{
	/* create a temp variable to holed current list */
	listint_t *temp;
	listint_t *temp2;

	if (list == NULL || list->next == NULL)
		return (0);

	temp = list;
	temp2 = list;
	/* loop throught the list upto the end or we encounter a cycle */
	while (temp && temp->next)
	{
		if (temp2 == temp)
			return (1);
		temp = temp->next;
		/* temp2 jumps two nodes at atime while temp jumps one */
		temp2 = temp2->next->next;
	}

	/* this means no cycle was found */
	return (0);
}
