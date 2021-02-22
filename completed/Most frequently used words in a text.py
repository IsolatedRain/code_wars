import collections


def top_3_words(text):
    t = "".join([c if c.isalnum() or c == "'" else " " for c in text.lower()])
    words = t.split()
    return [k for k, v in collections.Counter(words).most_common(3) if k.count("'") != len(k)]


# text = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."
text = "'''"
# text = "  //wont won't won't "
# text = " a a a  b  c c  d d d d  e e e e e"
# text = "uBvcY,.:!qM'FHm.-./TUl,?qM'FHm?/uBvcY/?TUl_,:uBvcY!?//?uBvcY:/TUl.ssp:OVaRFBfDJ ssp!?-; TUl!./:-uBvcY:uBvcY;.?,uBvcY .,:qM'FHm?!;-?uBvcY TUl/TUl-_.ssp?_?-uBvcY !;/!uBvcY--:/-uBvcY:/:,/OVaRFBfDJ;!;--OVaRFBfDJ?OVaRFBfDJ-.TUl/OVaRFBfDJ_/uBvcY_,,;uBvcY?uBvcY-uBvcY_OVaRFBfDJ;:-,/qM'FHm,?uBvcY.uBvcY:!?,.OVaRFBfDJ-_qM'FHm?TUl;?uBvcY//-;OVaRFBfDJ!qM'FHm!TUl;ssp!,?OVaRFBfDJ,-,,:OVaRFBfDJ..?uBvcY_-./:ssp:!;TUl/OVaRFBfDJ,/./ "
# text = "CHAcZDWPU,,!..CHAcZDWPU:;!CHAcZDWPU_,CHAcZDWPU_: CHAcZDWPU/,?CHAcZDWPU/;,-CHAcZDWPU-.,_ CHAcZDWPU:;;CHAcZDWPU?;,.:CHAcZDWPU!CHAcZDWPU.:"
print(top_3_words(text))
