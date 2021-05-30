from silabilizador import Silabilizador


def acentuador(word: str):
    s = Silabilizador()(word)
    if len(s) == 1:
        return word, 'monosílabo'

    split_word = '-'.join([str(syll) for syll in s])
    vocales_con_tilde = ['á', 'é', 'í', 'ó', 'ú']
    vocales_sin_tilde = ['a', 'e', 'i', 'o', 'u']
    consonantes = ['n', 's']
    ends = vocales_con_tilde + vocales_sin_tilde + consonantes

    nsv = word[-1] in ends  # word ends in N, S or vowel
    ultima = any([vocal in s[-1].word for vocal in vocales_con_tilde])
    anteultima = len(s) >= 2 and any([vocal in s[-2].word for vocal in vocales_con_tilde])
    antepenultima = len(s) >= 3 and any([vocal in s[-3].word for vocal in vocales_con_tilde])

    if antepenultima:
        return split_word, 'esdrújula'
    elif (nsv and ultima) or not ultima:
        return split_word, 'aguda'
    elif (nsv and not anteultima) or anteultima:
        return split_word, 'grave'
