def main(word):
  for i in range(len(word)):
	  if not word[i] == word[len(word) - 1 - i]:
		  return False
  return True

print(main('1661'))
