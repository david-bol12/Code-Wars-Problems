// This time no story, no theory. The examples below show you how to write function accum:
//
// Examples:
// accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"

String accum(String str) {
  String out = '';
  int x = 0;
  for(String i in str.split('')) {
    out += x > 0 ? '-' : '';
    out += i.toUpperCase() + i.toLowerCase() * x;
    x++;
  }
  return out;
}