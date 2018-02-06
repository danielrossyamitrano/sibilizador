class CharLine:
    def __init__(self, word):
        self.word = word
        self.char_line = [(char, self.char_type(char)) for char in word]
        self.type_line = ''.join(chartype for char, chartype in self.char_line)

    @staticmethod
    def char_type(char):
        if char in ['a', 'á', 'e', 'é', 'o', 'ó', 'í', 'ú']:
            return 'V'  # strong vowel
        if char in ['i', 'u']:
            return 'v'  # week vowel
        if char == 'x' or char == 's':
            return char
        else:
            return 'c'

    def split_by(self, finder, where):
        split_point = self.type_line.find(finder)
        if split_point != -1:
            chl1, chl2 = CharLine(self.word[0:split_point + where]), CharLine(self.word[split_point + where:])
            # chl1, chl2 = self.split(split_point, where)
            return chl1, chl2
        return self, False

    def __str__(self):
        return '<' + self.word + ':' + self.type_line + '>'

    def __repr__(self):
        return '<' + repr(self.word) + ':' + self.type_line + '>'


class Silabizer:
    def __init__(self):
        self.grammar = [('VV', 1), ('cccc', 2), ('xcc', 1), ('ccx', 2), ('csc', 2), ('xc', 1), ('cc', 1), ('vcc', 2),
                        ('Vcc', 2), ('sc', 1), ('cs', 1), ('Vc', 1), ('vc', 1), ('Vs', 1), ('vs', 1), ('vxv', 1),
                        ('VxV', 1), ('vxV', 1), ('Vxv', 1)]

    def split(self, chars):
        for split_rule, where in self.grammar:
            first, second = chars.split_by(split_rule, where)
            if second:
                if first.type_line in ['c', 's', 'x', 'cs'] or second.type_line in ['c', 's', 'x', 'cs']:
                    print('skip1', first.word, second.word, split_rule, chars.type_line)
                    continue
                if first.type_line[-1] == 'c' and second.word[0] in ['l', 'r']:
                    print('skip2', first.word, second.word, split_rule, chars.type_line)
                    continue
                if first.word[-1] == 'l' and second.word[-1] == 'l':
                    print('skip3', first.word, second.word, split_rule, chars.type_line)
                    continue
                if first.word[-1] == 'r' and second.word[-1] == 'r':
                    print('skip4', first.word, second.word, split_rule, chars.type_line)
                    continue
                if first.word[-1] == 'c' and second.word[-1] == 'h':
                    print('skip5', first.word, second.word, split_rule, chars.type_line)
                    continue
                return self.split(first) + self.split(second)
        return [chars]

    def __call__(self, word):
        return self.split(CharLine(word))


s = Silabizer()

print(s('esdrújula'))
