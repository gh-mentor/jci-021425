@workspace /tests create a Python unit test for a function 'filter_ints' that takes an array of integer 'numbers' and an anonymous function 'strategy' in the form: integer => boolean. The function should return a new array of integers that pass the 'strategy' test.


@workspace /tests create a DocTest unit test for a C++ class 'Employees'. The class should have a method 'HighEarners' that takes a function expression 'filter' in the form: double => bool. The method should return a list of employees that pass the 'filter. The test should include a test case that uses a lambda expression to filter employees with a salary greater than 100,000, and less than 10,000. The test should also include edge cases for empty and null employee lists.


Create a XUnit test  for a C++ class 'WordMix'  that contains a public, static method 'palindrome' that takes a string as an argument and returns true if the string can be read the same from right to left or left to right.
requirements:
- The method should be case-insensitive
- The method should not consider spaces or punctuation
- the method should return false if the string is empty or null
Examples:
- bob => true
- kayak => true 
- boat => false
- horse => false
- car => false