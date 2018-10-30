public Map<String, String> pairs(String[] strings) {
  Map<String, String> map = new HashMap<String, String>();
  
  for (String str: strings)
    map.put(String.valueOf(str.charAt(0)), 
            String.valueOf(str.charAt(str.length()-1)));
  
  return map;
}

