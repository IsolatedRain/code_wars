import collections


def mutations(alice, bob, word, first):
    aliceWords = [w for w in alice if len(set(w)) == 4]
    bobWords = [w for w in bob if len(set(w)) == 4]
    usedWords = {word}
    curTurn = first
    curWord = word

    def oneLetterDiff(w1, w2):
        cnt = 0
        for i in range(4):
            if w1[i] != w2[i]:
                cnt += 1
        return cnt == 1

    valid = False
    for w in bobWords + aliceWords:
        if oneLetterDiff(w, curWord):
            valid = True
            break
    if not valid: return -1

    while 1:
        curWords = aliceWords if not curTurn else bobWords
        provided = False
        for w in curWords:
            if w not in usedWords:
                if oneLetterDiff(w, curWord):
                    usedWords.add(w)
                    curWord = w
                    curTurn ^= 1
                    provided = True
                    break
        if not provided:
            return curTurn ^ 1


alice = ['down', 'vier', 'ragg', 'flip', 'nobs', 'sulu', 'shmo', 'quit', 'nerd', 'cete', 'frau', 'airy', 'gals', 'shew',
         'blur', 'tuck', 'quai', 'pyic', 'plot', 'salt', 'nits', 'caid', 'soja', 'byes', 'konk', 'ouph', 'brad', 'sudd',
         'buhr', 'like', 'whir', 'obis', 'yaud', 'jell', 'waps', 'burp', 'sate', 'fess', 'maya', 'kane', 'ahem', 'pyre',
         'zoos', 'oboe', 'yays', 'modi', 'ulva', 'pony', 'baas', 'mote', 'ansa', 'alee', 'chut', 'wise', 'dent', 'kith',
         'odea', 'flog', 'mots', 'salp', 'doby', 'cosy', 'souk', 'ryot', 'nibs', 'vary', 'word', 'twin', 'heed', 'pals',
         'flop', 'zebu', 'eels', 'soph', 'yoke', 'rise', 'mind', 'toon', 'talc', 'case', 'ions', 'kart', 'jube', 'hide',
         'hive', 'deco', 'hest', 'mawn', 'raps', 'hips', 'zero', 'bolo', 'core', 'beds', 'kbar', 'slid', 'kana', 'bode',
         'fans', 'gaed', 'yutz', 'tabu', 'haem', 'brig', 'tufa', 'anon', 'quin', 'rukh', 'fogs', 'lash', 'gips', 'dont',
         'joky', 'rial', 'baht', 'cuif', 'self', 'pols', 'agly', 'wins', 'staw', 'kyes', 'djin', 'date', 'rent', 'murk',
         'land', 'drek', 'brim', 'nope', 'rami', 'phew', 'vara', 'teth', 'nett', 'base', 'dahl', 'cots', 'pons', 'zeal',
         'icon', 'spin', 'feds', 'opal', 'arks', 'stot', 'agin', 'sunk', 'weds', 'bosh', 'bill', 'alit', 'wool', 'plan',
         'wage', 'glee', 'mail', 'ebbs', 'aery', 'duns', 'went', 'bops', 'rynd', 'mils', 'lome', 'numb', 'fins', 'sown',
         'drug', 'geld', 'gree', 'noel', 'eros', 'golf', 'pork', 'bros', 'wept', 'dost', 'kefs', 'buys', 'surf', 'moms',
         'eyes', 'avid', 'neum', 'kick', 'moue', 'tink', 'doat', 'spar', 'syph', 'bred', 'pews', 'vide', 'open', 'bail',
         'sang', 'clue', 'lilt', 'bosk', 'vale', 'monk', 'curd', 'eyer', 'pass', 'mayo', 'jabs', 'veto', 'levy', 'aria',
         'said', 'hone', 'blip', 'fuji', 'pent', 'legs', 'prat', 'duet', 'posh', 'docs', 'show', 'oaks', 'hyla', 'luff',
         'sima', 'hili', 'rail', 'coil', 'jowl', 'odic', 'exam', 'sobs', 'khaf', 'mend', 'vade', 'buzz', 'taxa', 'file',
         'math', 'doux', 'hilt', 'awed', 'wast', 'kobo', 'shoe', 'bola', 'tahr', 'grab', 'sage', 'gite', 'cuff', 'tuft',
         'kilt', 'hind', 'peke', 'rump', 'deke', 'desk', 'zyme', 'send', 'caff', 'cook', 'babe', 'eyry', 'wary', 'carn',
         'awny', 'tuts', 'five', 'merl', 'time', 'saps', 'deft', 'dull', 'weir', 'ford', 'acre', 'orca', 'sues', 'yawn',
         'cleg', 'rend', 'want', 'chai', 'lien', 'enol', 'typy', 'fats', 'obol', 'mano', 'kepi', 'peat', 'lull', 'vega',
         'anil', 'path', 'cave', 'liar', 'doty', 'pule', 'nook', 'last', 'obit', 'bock', 'orle', 'deus', 'defy', 'slop',
         'cozy', 'jink', 'kirs', 'ness', 'sext', 'kufi', 'koan', 'saut', 'okes', 'yank', 'whom', 'view', 'polk', 'vino',
         'goat', 'lily', 'font', 'moas', 'scup', 'afro', 'wake', 'ulan', 'pose', 'dare', 'romp', 'migs', 'seed', 'filo',
         'puny', 'tolu', 'taut', 'pupa', 'quad', 'pita', 'jefe', 'raga', 'smew', 'secs', 'kora', 'hams', 'tent', 'awes',
         'toys', 'pock', 'rack', 'earl', 'wigs', 'meow', 'sike', 'furs', 'jauk', 'firm', 'rind', 'hole', 'shah', 'spue',
         'foal', 'iglu', 'puma', 'sped', 'swab', 'errs', 'most', 'raja', 'pull', 'rule', 'jota', 'isms', 'verb', 'wove',
         'pact', 'each', 'alba', 'gear', 'foin', 'seen', 'spud', 'dais', 'zarf', 'faro', 'sill', 'abri', 'syli', 'lube',
         'bort', 'lane', 'yowe', 'juke', 'plod', 'rote', 'weld', 'brie', 'dams', 'sulk', 'sews', 'wind', 'cola', 'seer',
         'tape', 'bear', 'apex', 'join', 'feel', 'aril', 'sift', 'cape', 'hems', 'carb', 'duce', 'busy', 'wert', 'kook',
         'crus', 'camo', 'shri', 'odah', 'rags', 'baby', 'wans', 'kyak', 'teas', 'rhus', 'keel', 'slam', 'tune', 'rins',
         'fere', 'mitt', 'moor', 'wail', 'lens', 'wilt', 'coni', 'lead', 'cute', 'yaws', 'bund', 'quey', 'rias', 'lose',
         'scan', 'tiff', 'omit', 'titi', 'vasa', 'dome', 'icky', 'guid', 'barb', 'ghis', 'haji', 'curf', 'huff', 'coif',
         'fish', 'duad', 'dose', 'tref', 'rays', 'eths', 'emmy', 'oils', 'ikon', 'gent', 'jess', 'jail', 'hyle', 'goes',
         'roof', 'drip', 'kune', 'gaes', 'tens', 'dram', 'sins', 'sing', 'macs', 'grew', 'aqua', 'elms', 'yack', 'axle',
         'upas', 'epee', 'pant', 'guvs', 'spew', 'plow', 'dunt', 'kiva', 'dubs', 'amps']

bob = ['peep', 'fall', 'lout', 'nark', 'pika', 'arch', 'dorp', 'salp', 'hong', 'mixt', 'fret', 'tuft', 'book', 'chin',
       'heir', 'nite', 'lips', 'axal', 'wont', 'mura', 'beer', 'oxer', 'hate', 'teff', 'alan', 'dyes', 'tuns', 'quid',
       'piso', 'gulp', 'cows', 'neck', 'rows', 'tsar', 'kaas', 'joss', 'alas', 'pest', 'rams', 'hisn', 'odes', 'marc',
       'dice', 'ohia', 'mash', 'yeuk', 'sybo', 'kufi', 'slay', 'ilka', 'goby', 'coif', 'pons', 'nook', 'nose', 'inly',
       'cake', 'wynd', 'grit', 'baff', 'eyra', 'yens', 'cosy', 'also', 'pert', 'esse', 'cham', 'pros', 'ammo', 'khat',
       'foss', 'surf', 'blew', 'hemp', 'mead', 'echo', 'tows', 'walk', 'wark', 'oots', 'nema', 'vita', 'hawk', 'defy',
       'bing', 'peat', 'mozo', 'jupe', 'pads', 'yuga', 'ritz', 'lieu', 'roms', 'baps', 'tong', 'spin', 'sign', 'seam',
       'jamb', 'nolo', 'fubs', 'whap', 'tump', 'olid', 'hyle', 'filo', 'disk', 'curr', 'core', 'girt', 'sink', 'ansa',
       'opes', 'upon', 'iggs', 'pugh', 'star', 'warm', 'raft', 'bedu', 'dins', 'skis', 'refs', 'bids', 'wage', 'bots',
       'kirs', 'puns', 'ludo', 'rush', 'mush', 'dawk', 'kyte', 'duly', 'draw', 'says', 'liri', 'lazy', 'whip', 'folk',
       'kibe', 'jape', 'ruin', 'nala', 'mall', 'didy', 'newt', 'doxy', 'migs', 'rope', 'rote', 'rato', 'cred', 'curs',
       'moth', 'dues', 'nags', 'ulan', 'bree', 'envy', 'sigh', 'asea', 'yaup', 'tads', 'over', 'cams', 'nips', 'drop',
       'etic', 'cero', 'pure', 'bise', 'tace', 'koto', 'vigs', 'fort', 'tern', 'shad', 'mels', 'furs', 'fowl', 'darn',
       'rook', 'taco', 'axed', 'tang', 'muns', 'polo', 'blob', 'faun', 'kifs', 'lady', 'cots', 'tyke', 'prez', 'duke',
       'ford', 'rife', 'noes', 'ichs', 'gien', 'dojo', 'ohms', 'dash', 'whig', 'gain', 'sots', 'tole', 'rolf', 'beef',
       'kyar', 'send', 'farm', 'each', 'nest', 'fest', 'glam', 'soys', 'oohs', 'snye', 'lave', 'posy', 'bris', 'nogs',
       'poet', 'jota', 'murr', 'hyps', 'typo', 'oaks', 'mary', 'moas', 'pans', 'gars', 'span', 'spit', 'mosh', 'ague',
       'data', 'yods', 'reek', 'mint', 'pein', 'pies', 'mast', 'bugs', 'hose', 'boom', 'oldy', 'gama', 'tend', 'glut',
       'odah', 'ooze', 'live', 'felt', 'chit', 'smog', 'city', 'burn', 'wiry', 'fuci', 'less', 'clon', 'gimp', 'jarl',
       'tony', 'whom', 'orca', 'ebbs', 'ride', 'eddy', 'coda', 'worm', 'waes', 'wool', 'gits', 'dork', 'coin', 'vane',
       'mako', 'slaw', 'snug', 'olla', 'bell', 'herb', 'turn', 'merk', 'rums', 'gibs', 'shod', 'inia', 'clam', 'fled',
       'fogs', 'mums', 'form', 'bike', 'muss', 'wiss', 'bubo', 'fawn', 'fogy', 'limo', 'derv', 'rimu', 'umps', 'alls',
       'tews', 'cyma', 'fink', 'loop', 'davy', 'mads', 'agha', 'cede', 'agee', 'howk', 'helm', 'pend', 'sake', 'noms',
       'girn', 'sing', 'zins', 'aver', 'sari', 'hili', 'boll', 'rude', 'yell', 'pias', 'ties', 'mara', 'kaif', 'pied',
       'lewd', 'holt', 'hoke', 'bels', 'fuss', 'glib', 'tint', 'imps', 'harl', 'gyre', 'muds', 'soft', 'dots', 'yolk',
       'sups', 'sees', 'pair', 'pipy', 'dags', 'loom', 'kabs', 'balm', 'beta', 'knew', 'lept', 'dual', 'geck', 'eche',
       'chew', 'oath', 'dubs', 'meou', 'jade', 'glow', 'dons', 'inro', 'dare', 'quit', 'lulu', 'forb', 'amus', 'weep',
       'zinc', 'kids', 'leku', 'caff', 'grat', 'jabs', 'loin', 'doum', 'germ', 'ryot', 'blin', 'biff', 'reft', 'they',
       'wane', 'lark', 'mitt', 'dirk', 'beak', 'ankh', 'boor', 'path', 'lakh', 'expo', 'yarn', 'rede', 'sori', 'sike',
       'amok', 'buff', 'asps', 'plus', 'pope', 'aura', 'snot', 'yows', 'lear', 'tops', 'gosh', 'perp', 'nevi', 'zeps',
       'torc', 'suet', 'tugs', 'libs', 'lain', 'loot', 'rink', 'dewy', 'weka', 'fets', 'ecru', 'john', 'clue', 'bort',
       'wynn', 'jink', 'edhs', 'flew', 'rate', 'dreg', 'mood', 'mace', 'yurt', 'guru', 'abri', 'mora', 'bunk', 'sage',
       'mina', 'ages', 'quay', 'areg', 'luge', 'sows', 'owly', 'espy', 'then', 'pawn', 'idol', 'bend', 'duns', 'beck',
       'sent', 'syce', 'must', 'fuds', 'vina', 'mark', 'cess', 'bane', 'give', 'opal', 'voes', 'boyo', 'oust', 'berm',
       'fado', 'owes', 'glim', 'jive', 'hams', 'fact', 'guff', 'nosy', 'doms', 'acme', 'halt', 'swad', 'lump', 'calf',
       'sans', 'jake', 'ants', 'zoic', 'head', 'bias', 'cion', 'sure', 'code', 'pepo']
args = [alice, bob, "sate", 1]
print(mutations(*args))
