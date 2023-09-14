def solution(departure, destination):
    xDist = abs(departure[0] - destination[0])
    yDist = abs(departure[1] - destination[1])
    """
    We need to detect 3 things:
      * if the coordinates in X or Y for both depature and destination are float
      * if depature and destination are both in the same block
      * and if they are not in the same street
    If both of them are float, and they are on the same block, it means that we need to make additional calculations. If they are on the same street, we can make the simple calculation.
    If one of these conditions is not true, the calculations are straightforward and just need to calculate the delta between coordinates (dX = X1 - X2, dY = Y1 - Y2).
    See the following cases to understand better:
    Case 1: A = [0.4,1] and B = [0.9,3], when evaluating the below conditions, both X are float, the floor of both is 0 so it means they are on the same block, and the streets (Y) are not the same.
    Case 2: A = [0.4,1] and B = [3.5,1], both X are float, but the floor for both are not the same and the streets the same.
    Case 3: A = [0.4,1] and B = [2.7,3], both X are float, but the floor for both are not the same and the streets are not the same.
    Case 4: A = [1,2] and B = [3,4], if the coordinates have only 1 float on X or Y, or don't have any float on the coords, we can pass the condition evaluation.
    Only Case 1 satisfies the 3 conditions.

    We need to evaluate then using Floor or Ceil, in order to find the minimum distance:
      Case 1: |floor(0.4) - 0.4| = 0.4 --> |ceil(0.4) - 0.4| = 0.6 
              |floor(0.9) - 0.9| = 0.9 --> |ceil(0.9) - 0.9| = 0.1
              min(0.4 + 0.9 , 0.6 + 0.1) = 0,7

              Explanation: When evaluating floor, going from 0.4 to 0 and then from 0 to 0.9, we get a total distance of 1.3, meanwhile when evaluating ceil, going from 0.4 to 1, and then from 1 
              to 0.9, the total distance is 0.7
    
    """
    if (math.floor(departure[0]) != departure[0] and math.floor(destination[0]) != destination[0] and
        math.floor(departure[0]) == math.floor(destination[0]) and
        departure[1] != destination[1]):
        xDist = min(abs(departure[0] - math.floor(departure[0]) + destination[0] - math.floor(destination[0])),
                    abs(departure[0] - math.ceil(departure[0])  + destination[0] - math.ceil(destination[0])))
    elif (math.floor(departure[1]) != departure[1] and math.floor(destination[1]) != destination[1] and
          math.floor(departure[1]) == math.floor(destination[1]) and
          departure[0] != destination[0]):
        yDist = min(abs(departure[1] - math.floor(departure[1]) + destination[1] - math.floor(destination[1])),
                    abs(departure[1] - math.ceil(departure[1])  + destination[1] - math.ceil(destination[1])))
    
    return xDist + yDist
