public Map<String, Integer> word0(String[] strings) {
  Map<String, Integer> map = new HashMap<String, Integer>();
  
  for (String str: strings)
    map.put(str, 0);
  
  return map;
}

