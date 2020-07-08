from fuzzyfinder import fuzzyfinder
suggestions = fuzzyfinder('abc', ['abcd', 'defabca', 'aagbec', 'xyz', 'qux'])

print(list(suggestions))