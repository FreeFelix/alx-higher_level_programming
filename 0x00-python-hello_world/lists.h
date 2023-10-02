#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listintiger_s - single linked list structure.
 * @i: passed argunment int
 * @next: node pointed to the next node
 *
 * Description: Single linked with node and structure for
 * Alx high level programming project.
 */
typedef struct listintiger_s
{
	int i;
	struct listintiger_s *next;
} listintiger_t;

size_t print_listintiger(const listintiger_t *h);
listintiger_t *add_nodeint(listintiger_t **head, const int i);
void free_listintiger(listintiger_t *head);
int check_cycle(listintiger_t *list);

#endif

