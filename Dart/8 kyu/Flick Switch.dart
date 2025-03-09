// Create a function that always returns True/true for every item in a given list.
// However, if an element is the word 'flick', switch to always returning the opposite boolean value.

List<bool> flickSwitch(List<String> lst) {
  List<bool> out = [];
  bool state = true;
  for (String i in lst) {
    if(i == 'flick'){
      state = !state;
    }
    out.add(state);
  }
  return out;
}