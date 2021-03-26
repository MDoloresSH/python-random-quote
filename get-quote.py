import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  
  if (rnd == last):
    print("The penultimate quote: " + quotes[rnd-1], "The last quote: " + quotes[rnd])
  elif  (rnd < last and rnd > 0):
    print("Two quotes : ",quotes[rnd-1], quotes[rnd+1])
  else:
    print("The first quote: " + quotes[rnd])
    
    
if __name__== "__main__":
  primary()
