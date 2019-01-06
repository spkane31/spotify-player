from operator import itemgetter

def OrderSong(filename):
  """This will take the given filename and run a word count on it, and return the results
  in a different file. """

  with open(filename, 'r') as f:
    content = f.read()

  new = content.split('\n')

  ListScore = []
  try:
    for part in new:
      indiv = part.split(',')

      # Gets the vote score for a song
      score = (int(indiv[-2].replace(' ','')) - int(indiv[-1].replace(' ','')))

      # adds the vote score to that songs list
      indiv.append(score)
      # adds that song back to full song list
      ListScore.append(indiv)

  except:
    pass

  OrganizedList = sorted(ListScore,key=itemgetter(-1))
  OrganizedList = OrganizedList[::-1]
  with open("app/queue.txt", "w") as f:
    for q in OrganizedList:
      write_string = str(q[0]).replace(',','') + ", " + str(q[1][1:]).replace(',','') + ", " + str(q[2][1:]) + ", " + str(q[3][1:]) + "," + str(q[-3]) + "," + str(q[-2])+"\n"
      f.write("%s" % write_string)

  return OrganizedList

def remove(cookie):
  results = open("app/queue.txt", "r")
  data =[]
  queue = []
  with open("app/queue.txt", "r") as f:
    data = f.readlines()

  for d in data:
    d = d.split(',')
    if cookie not in d[2]:
      queue += [d]

  with open("app/queue.txt", "w") as f:
    for q in queue:
      write_string = str(q[0]).replace(',','') + ", " + str(q[1][1:]).replace(',','') + ", " + str(q[2][1:]) + ", " + str(q[3][1:]) + "," + str(q[-2]) + "," + str(q[-1])
      f.write("%s" % write_string)

(OrderSong('app/queue.txt'))
remove('2zYzyRzz6pRmhPzyfMEC8s')
