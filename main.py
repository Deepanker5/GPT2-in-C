import tiktoken

f = open("GPT-2-c/train.txt", "r")
enc = tiktoken.encoding_for_model("gpt2")
tokens = enc.encode(f.read())
text = enc.decode(tokens)
print(text)