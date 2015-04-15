name = raw_input("Enter file:")

handle = open(name)

clients = dict()

# for line in handle:
#     line = line.rstrip()
#     words = line.split()
#     print words
#     continue

for line in handle:
    line = line.rstrip()
    words = line.split()
    if not words[6] == 'Socket' :
        continue
    wordlen = len(words)
#   client = words[9]
#   clients[client] = clients.get(client, 0) + 1
  
print wordlen      
# print clients
print words