# SOLUTION 1
# Class Photos

# Complexity
# Average:  Time: O(nlog(n))  | Space: O(1)
# Worst:    Time: | Space:
# where n is the number of students

def classPhotos(redShirtHeights, blueShirtHeights):

  redShirtHeights.sort(reverse=True)
  blueShirtHeights.sort(reserver=True)

  shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"

  for idx in range(len(redShirtHeights)):
    redShirtHeight = redShirtHeights[idx]
    blueShirtHeight = blueShirtHeights[idx]

    if shirtColorInFirstRow == "RED":
      if redShirtHeight >= blueShirtHeight:
        return False

    else:
      if blueShirtHeight >= redShirtHeight:
        return False
  
  return False
