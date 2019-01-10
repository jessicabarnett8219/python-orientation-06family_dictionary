my_family = {
  "mom": {
    "name": "Stephanie",
    "age": 52
  },
  "dad": {
    "name": "Wayne",
    "age": 55
  },
  "gradnma": {
    "name": "Jean",
    "age": 78
  }
}

family_sentences = {f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' for (family_member, member_values) in my_family.items()}

print(family_sentences)