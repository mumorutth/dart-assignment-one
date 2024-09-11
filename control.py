void checkNumber(int number) {
  if (number > 0) {
    print('$number is positive');
  } else if (number < 0) {
    print('$number is negative');
  } else {
    print('$number is zero');
  }
}

void checkVotingEligibility(int age) {
  if (age >= 18) {
    print('Eligible to vote');
  } else {
    print('Not eligible to vote');
  }
}

void main() {
  checkNumber(10);
  checkNumber(-5);
  checkNumber(0);

  checkVotingEligibility(20);
  checkVotingEligibility(16);
}
