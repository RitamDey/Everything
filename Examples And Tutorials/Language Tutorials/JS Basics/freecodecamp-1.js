var count = 0;

function cc(card) {
  // Only change code below this line
  switch (card) {
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count += 1;
      break;
    
    case 10:
    case "J":
    case "Q":
    case "K":
    case "A":
      count -= 1;
      break;
    
    default:
      break;
  }
  
  
  return count + ((count > 0) ? " Bet": " Hold");
  //if (count > 0)
//	return count + " Bet";
  //else
//	return count + " Hold";
  // Only change code above this line
}


cc(7); cc(8);
console.log(cc(9));
