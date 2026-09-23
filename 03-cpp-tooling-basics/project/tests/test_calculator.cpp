#include <gtest/gtest.h>

#include "calculator.h"

TEST(CalculatorTest, Add) {
  Calculator calculator;
  EXPECT_EQ(calculator.add(2, 3), 5);
}

TEST(CalculatorTest, Subtract) {
  Calculator calculator;
  EXPECT_EQ(calculator.subtract(5, 1), 4);
}

TEST(CalculatorTest, Multiply) {
  Calculator calculator;
  EXPECT_EQ(calculator.multiply(4, 6), 24);
}

TEST(CalculatorTest, Divide) {
  Calculator calculator;
  EXPECT_DOUBLE_EQ(calculator.divide(10, 4), 2.5);
}

TEST(CalculatorTest, DivideByZeroThrows) {
  Calculator calculator;
  EXPECT_THROW(calculator.divide(1, 0), std::invalid_argument);
}
