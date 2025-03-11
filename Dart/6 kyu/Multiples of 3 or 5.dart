// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
//
// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
//
// Additionally, if the number is negative, return 0.
//
// Note: If the number is a multiple of both 3 and 5, only count it once.

int solution(int n) {
  int total = 0;
  for(int multiple = 0; (multiple * 3) < n; multiple++) {
    total += multiple * 3;
  }
  for(int multiple = 0; (multiple * 5) < n; multiple++) {
    total += multiple * 5;
  }
  for(int multiple = 0; (multiple * 15) < n; multiple++) {
    total -= multiple * 15;
  }
  return total;
}