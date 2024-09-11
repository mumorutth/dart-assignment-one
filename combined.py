void main() {
  List<int> numbers = [3, 8, 15, 22, 105];

  for (int number in numbers) {
    print('Number: $number');

    // Check if the number is even or odd
    if (number % 2 == 0) {
      print('$number is even');
    } else {
      print('$number is odd');
    }

    // Categorize the number
    switch (number) {
      case int n when n >= 1 && n <= 10:
        print('$number is small');
        break;
      case int n when n >= 11 && n <= 100:
        print('$number is medium');
        break;
      case int n when n > 100:
        print('$number is large');
        break;
      default:
        print('$number is out of range');
    }
  }
}
