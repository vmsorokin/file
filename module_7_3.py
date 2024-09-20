class WordsFinder:
    def __init__(self, *files_name):
        self.file_names = files_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                text = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            for i, w in enumerate(words):
                if w == word.lower():
                    result[file_name] = i+1
                    break
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())
        return result


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))