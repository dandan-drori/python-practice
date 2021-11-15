def main():
  word = input('Enter a word: ')
  is_palindrome = True
  for i in range(len(word)):
    if not word[i] == word[len(word) - 1 - i]:
      print('The word is NOT a palindrome')
      is_palindrome = False
      break
  if is_palindrome:
    print('The word IS a palindrome')
  while input('Play Again? Y/N ').upper() == 'Y':
    main()

main()
