void convertAndDisplay(String numberStr) {
  int intValue = stringToInt(numberStr);
  double doubleValue = stringToDouble(numberStr);

  print('Converted String to int: $intValue');
  print('Converted String to double: $doubleValue');
}

void main() {
  convertAndDisplay('789');
}
