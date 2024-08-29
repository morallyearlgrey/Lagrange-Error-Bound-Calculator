import math

class lagrangeErrorBound:
  def __init__(self, max, approximate, center, n):
    self.m = max
    self.a = approximate
    self.c = center
    self.n = n+1

  def calculateLagrangeErrorBound(self):
    approxPortion = self.a-self.c
    approxPortion = math.pow(approxPortion, self.n)
    numerator = self.m*approxPortion
    denominator = math.factorial(self.n)
    answer = numerator/denominator

    print("Error = " + str(answer))

  def toString(self, num: int):
    print("Problem " + str(num) + " Calculations:\nError = "
          + "(" + str(self.m) + "|" + str(self.a) + " - "
          + str(self.c) + "|" + "^" + str(self.n-1) + "+1" ")"
          + "/" + "(" + str(self.n-1) + "+1)!")

print("Calculating Lagrange Error Bound...\n")

print("---\n")

print("Example Problem 1:")
print("Use the Lagrange error bound to estimate the error in "
      + "\nusing a 4th degree Maclaurin polynomial to approximate "
      + "cos(π/4).\n")
problem1 = lagrangeErrorBound(1, 0.785, 0, 4)
problem1.toString(1)
problem1.calculateLagrangeErrorBound()

print("\n----")

print("\nExample Problem 2:")
print("The fourth degree Maclaurin polynomial for cos x is " +
      "given by p4(x)=1-x^2/2!+x^4/4!. "
      + "\nIf this polynomial is used to approximate cos(0.2), "
      + "what is the Lagrange error bound?\n")
problem2 = lagrangeErrorBound(1, 0.2, 0, 4)
problem2.toString(2)
problem2.calculateLagrangeErrorBound()
