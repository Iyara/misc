name = raw_input("Enter file:")

handle = open(name)

clients = dict()



for line in handle:
    line = line.rstrip()
    words = line.split()
#    print words
#    print len(words)
    if len(words) < 7 :
        continue
    if not words[6] == 'Socket' :
        continue
    comma = line.find(',')
    endpos = line.find(',',comma + 2)
    clientplus = line[comma + 2:endpos]
    
    client = clientplus[13:]
    
#    print client
    clients[client] = clients.get(client, 0) + 1
  
       
print clients
    