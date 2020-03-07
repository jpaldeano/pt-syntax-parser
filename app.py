import nltk
from nltk import tokenize
from nltk.corpus import floresta

# Regras para frases em Português
RULES = """
      F -> SN | SN SV | SN OR SV
      OR -> SP V 
      SV -> V | V SN SP | V SN | V adj | V adj SP | V SP | V V | V V SN
      SP -> prp SN | pron-indp SN
      V -> v-pcp | v-inf | v-ger | v-fin | v-pcp
      SN -> art n | n  
      """

"""
    Esta função treina um tagger. O tagger sucintamente é o que atribui o valor a cada token. Segundo os Documento do NLTK, o tagger2 desta função tem uma precisão de 87,02% apróximadamente.
"""


def train_tagger():
    print("Training taggers, please wait...")

    # Simplificar as tags das frases que estão no módulo floresta
    tsents = floresta.tagged_sents()
    tsents = [
        [(w.lower(), simplify_tag(t)) for (w, t) in sent] for sent in tsents if sent
    ]

    tagger0 = nltk.DefaultTagger("n")
    tagger1 = nltk.UnigramTagger(tsents, backoff=tagger0)
    tagger2 = nltk.BigramTagger(tsents, backoff=tagger1)

    return tagger2


"""
    A função simplify tag recebe como argumento um token gerado pela função tagged_sents() do modulo floresta 
    e remove a subclasse da tag.
"""


def simplify_tag(t):
    if "+" in t:
        return t[t.index("+") + 1:]
    else:
        return t


"""
    Função auxiliar que recebe um conjunto de tokens e os agrupa no sua classe.
"""


def group_tokens(tokens):
    group = {}
    for t in tokens:
        if t[1] in group:
            group[t[1]].append(t[0])
        else:
            group[t[1]] = [t[0]]
    return group


"""
    Função que adiciona os tokens do texto às regras gramaticais. 
"""


def add_tokens_to_rules(group, rules):
    for t in group:
        rules = "\n" + rules + t + " -> "
        for i in range(len(group[t])):
            if i == len(group[t]) - 1:
                rules = rules + '"' + group[t][i] + '"'
            else:
                rules = rules + '"' + group[t][i] + '" | '
        rules = rules + "\n"
    return rules


"""
    Esta função recebe um texto como input e os tokens gerados pelo tagger e imprime a árvore sintáctica, caso hajam regas definidas para a mesma.
"""


def get_syntax_tree(text, tokens):
    grouped_tokens = group_tokens(tokens)
    rules = add_tokens_to_rules(grouped_tokens, RULES)

    # Descomentar as duas linhas abaixo para fazer debug, em caso o programa não consiga processar a árvore sintáctica.
    # print(rules)
    # print(tokens)

    grammar = nltk.CFG.fromstring(rules)

    sent = text.split()
    rd_parser = nltk.RecursiveDescentParser(grammar)
    for tree in rd_parser.parse(sent):
        print("Tree: ")
        print(tree)
        break


# O tagger está declarado como variável global para correr ficar em memória durante a execução do Notebook e assim ser mais rápido testar diferentes inputs a partir do Notebook.
TAGGER = train_tagger()
print("Done.")

"""
    A função recebe um texto como parâmetro, transforma o texto em tokens utilizando o tagger anteriormente definido e por fim obtem a árvore sintáctica.
"""


def parse_text(text):
    tokenized_words = tokenize.word_tokenize(text, language="portuguese")
    get_syntax_tree(text, TAGGER.tag(tokenized_words))
