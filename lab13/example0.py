# selection sort recursive

def rec_selection(list):
  if len(list)==1:
    return list
  minimum=min(list)
  list.remove(minimum)
  return [minimum]+rec_selection(list[0:])



liste=[43,342,343,2,34]
print(rec_selection(liste))