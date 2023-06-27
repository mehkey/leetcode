from collections import defaultdict
class TimeMap:
  def __init__(self):
      self.memo = defaultdict(list)
  def set(self, key: str, value: str, timestamp: int) -> None:
      # store a timestamp, value pair in the list
      self.memo[key].append([timestamp, value])
  def get(self, key: str, timestamp: int) -> str:
      # binary search on timestamp in the list
      index = bisect.bisect(self.memo[key], [timestamp+1]) -1
      if index < 0:
          return ""
      return self.memo[key][index][1]



https://algomonster.medium.com/python-treemap-c0f4b4b966ba