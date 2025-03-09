// Write a function that takes an array of numbers and returns the sum of the numbers.
// The numbers can be negative or non-integer.
// If the array does not contain any numbers then you should return 0.

num sum(List<num> arr) {
  num out = 0;
  for(num i in arr) {
    out += i;
  }
  return out;
}