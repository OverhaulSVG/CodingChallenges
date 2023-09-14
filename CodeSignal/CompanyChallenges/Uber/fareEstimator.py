def solution(ride_time: int, ride_distance: int, cost_per_minute: list, cost_per_mile: list -> list):
  """
  The function should receive the parameters, which are ints and lists.
  Then create a list comprenhension that takes the two lists, zip them, iterate over them, 
  multiply the ride time per cost time and ride dist per cost dist, add both values and then return the list
  """
  return [ride_time * cost_time + ride_distance * cost_dis for cost_time, cost_dis in zip(cost_per_minute,cost_per_mile)]

