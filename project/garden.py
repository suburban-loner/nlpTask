import spacy

nlp = spacy.load("en_core_web_sm")

garden_sentences = [
    "The chicken is ready to eat because it's been cooked for hours.",
    "I convinced her children are noisy."
]

garden_sentences += [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

for sentence in garden_sentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    for token in doc:
        t = f"\tToken: {token.text}, Named Entity: {token.ent_type_}"
        print(t)

for sentence in garden_sentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    for token in doc:
        t = f"\tToken: {token.text}, Entity: {token.pos_}"
        print(t)

print(spacy.explain("GPE"))
print(spacy.explain("SCONJ"))

# 1st. GPE represents Countries, cities, states. It does not make sene in the sentence: "The cotton clothing is made of grows in Mississippi." 
# as this sentence is grammatically incorrect.

# 2nd. SCONJ represents subordinating conjunction. It makes sense in the sentence: "The chicken is ready to eat because it's been cooked for hours." 
# as it indicates the reason why the chicken is ready to eat.
