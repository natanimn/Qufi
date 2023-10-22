from .. import config


def letter_dict() -> dict:
    vowels = ['a', ['u', 'uu'], ['i', 'ii'], ['aa'], ['e', 'ee'], '\'', ['o', 'oo']]
    consonants = ['h', 'l', 'm', 'r', 's', 'sh', 'q', 'b', 'v', 't', 'ch', 'n', 'ny', '\'', 'k', 'w', 'z', 'zy', 'y',
                  'd', 'j', 'g', 'x', 'c', 'ph', 'ts', 'f', 'p']
    all_letter_dict = {}
    the_dh = list("ዸꬉꬊꬋꬌꬍꬎ")
    for cons, letter in zip(consonants, config.GEEZ_LETTERS):
        for vowel in vowels:
            ind = vowels.index(vowel)
            c = "" if cons == '\'' else cons
            if vowel == "'":
                vowel = ""
            if vowel == '' and c == "": continue
            
            if isinstance(vowel, list):
                for v in vowel:
                    all_letter_dict[c+v] = chr(ord(letter)+ind) + ('፞' if v != 'aa' and len(v) == 2 else '')
            else:
                all_letter_dict[c+vowel] = chr(ord(letter) + ind)

    for vowel, dh in zip(vowels, the_dh):
        if vowel == '\'': vowel = ''
        if isinstance(vowel, list):
            for v in vowel:
                all_letter_dict["dh" + v] = dh + ('፞' if v != 'aa' and len(v) == 2 else '')
        else:  
            all_letter_dict['dh'+vowel] = dh
    return all_letter_dict
