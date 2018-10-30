public Map<String, Integer> wordCount(String[] strings) {
  HashMap<String, Integer> map = new HashMap<String, Integer>();
  
  for (String str: strings)
    map.put(str, map.getOrDefault(str, 0)+1);
  
  return map;
}

