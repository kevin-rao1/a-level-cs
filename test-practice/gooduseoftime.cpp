#include<iostream>
#include<cstdint>
uint64_t value = 0;
uint64_t count = 0;
char operation;
char a = 'a';
int main() {
  std::cout << "Enter integer (0-99): ";
  std::cin >> value;
  std::cout << "Calculate additive or multiplicative persistence (a or m)? ";
  std::cin >> operation;
  uint64_t count = 0;
  while (value > 9) {
    if (operation == a) {
      value = (value/10) + (value%10);
    } else {
      value = (value/10) * (value%10);
    }
    count++;
  }
  std::cout << "The persistence is: ";
  std::cout << count;
  return 0;
}