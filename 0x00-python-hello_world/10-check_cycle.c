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

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (0);

	if (list == NULL || list->next == NULL)
		return (0);

	temp = list->next;
	/* loop throught the list upto the end or we encounter a cycle */
	while (temp)
	{
		/* if the next struct points to the first node it has a cycle */
		if (temp->next == list)
			return (1);

		temp = temp->next;
	}

	/* this means no cycle was found */
	free(temp);
	return (0);
}
