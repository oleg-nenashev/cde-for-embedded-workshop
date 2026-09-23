#include <iostream>

#include "calculator.h"

int main() {
  Calculator calculator;
  std::cout << "2 + 3 = " << calculator.add(2, 3) << '\n';
  std::cout << "5 - 1 = " << calculator.subtract(5, 1) << '\n';
  std::cout << "4 * 6 = " << calculator.multiply(4, 6) << '\n';
  std::cout << "10 / 4 = " << calculator.divide(10, 4) << '\n';
  return 0;
}
