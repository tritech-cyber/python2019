n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    print ("numbers ",numbers)
    for number in numbers:
      results.append(number)
      print ("number ",number)clea
  return results

flatten(n)
print
print flatten(n)

