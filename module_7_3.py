import encodings.utf_8

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        result = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                text = f.read()
                text = text.lower()
                for i in ',.=!?:-':
                    text = text.replace(i, '')
                words = text.split()
                result[file] = words

        return result

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word.lower())
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
