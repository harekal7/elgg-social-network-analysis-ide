import snaide

for page in snaide.get_all_pages():
	print page["name"]
g = snaide.get_all_pages()

for i in g:
  print i["name"]
