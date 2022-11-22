def appliquer_cycle(cycle, tab) : 
  val1 = tab[cycle[0]]
  for i in range(1, len(cycle)) : 
    val2 = tab[cycle[i]]
    tab[cycle[i]] = val1
    val1 = val2 
  tab[cycle[0]] = val1 
  return tab 

tab = eval(input())
cycle = eval(input()) 

print(appliquer_cycle(cycle, tab)) 
