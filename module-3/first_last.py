def remove_first_and_last(list_to_clean):
	_, *content, _ = list_to_clean
	return content

html = ['<h1>', 'Some Content', '</h1>']
print(remove_first_and_last(html))

html_2 = ['<h1>', 'Some Content', 'More', 'Even More', '</h1>']
print(remove_first_and_last(html_2))