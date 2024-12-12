def single_root_words (root_word, *other_words ):
    same_words = []
    lowercase_list = [s.lower() for s in other_words]
    for i in range(len(lowercase_list)):
        if root_word.lower() in lowercase_list[i] or lowercase_list[i] in root_word.lower() :
            same_words.append(lowercase_list[i])
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Mable', 'Able', 'Disable', 'Bagel')
