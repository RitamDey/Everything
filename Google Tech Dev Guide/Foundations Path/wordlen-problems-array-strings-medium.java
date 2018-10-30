public Map<String, Integer> wordLen(String[] strings) {
  Map<String, Integer> map = new HashMap<String, Integer>();
  
  for (String str: strings) {
    if (!map.containsKey(str))
      map.put(str, str.length());
  }
  
  return map;
}

