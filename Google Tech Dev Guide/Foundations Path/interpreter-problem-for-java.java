public int interpret(int value, String[] commands, int[] args) {
  int pos = 0;
  
  for (String op: commands) {
    switch(op) {
      case "+":
        value += args[pos];
        break;
      case "-":
        value -= args[pos];
        break;
      case "*":
        value *= args[pos];
        break;
      case "/":
        value /= args[pos];
        break;
      default:
        return -1;
    }
    pos++;
  }
  
  return value;
}

