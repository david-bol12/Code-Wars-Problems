// Your job is simple, if x squared is more than 1000, return
// It's hotter than the sun!!, else, return
// Help yourself to a honeycomb Yorkie for the glovebox.

String apple(dynamic a) {
  int x = 0;
  if(a is String) {
    x = int.parse(a);
  } else {x = a;}
  if(x * x > 1000) {
    return "It's hotter than the sun!!";
  } else {return "Help yourself to a honeycomb Yorkie for the glovebox.";}
}