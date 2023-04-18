translation = {
  "CU": "see you",
  ":-)": "I'm happy",
  ":-(": "I'm unhappy",
  ";-)": "wink",
  ":-P": "stick out my tongue",
  "(~.~)": "sleepy",
  "TA": "totally awesome",
  "CCC": "Canadian Computing Competition",
  "CUZ": "because",
  "TY": "thank-you",
  "YW": "you're welcome"
}

while True:
  word = input()
  if word == "TTYL":
    break

  if word in translation.keys(): print(translation[word])
  else: print(word)

print("talk to you later")