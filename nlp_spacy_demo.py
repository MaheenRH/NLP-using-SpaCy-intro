import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Analyze sample text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(f"{token.text:<15} | {token.pos_:<10} | {token.dep_:<10}")

print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)
