
```
Please show me the steps and JavaScript code for a class library that models a company.. Adherance to solid principles is important. Include the following classes:

1. `Company` class:
   - Properties:
     - `name` (String)
     - `departments` (Array)
   - Methods:
     - `constructor(name)`
     - `addDepartment(department)`
     - `getDetails()`
     - `getDepartments()`

2. `Department` class:
   - Properties:
     - `id` (Number)
     - `name` (String)
     - `employees` (Array)
   - Methods:
     - `constructor(id, name)`
     - `getId()`
     - `getName()`
     - `addEmployee(employee)`
     - `removeEmployee(employee)`
     - `getDetails()`
     - `getEmployees()`

3. `Employee` class:
   - Properties:
     - `id` (Number)
     - `name` (String)
     - `salary` (Number)
   - Methods:
     - `constructor(id, name, salary)`
     - `getId()`
     - `getName()`
     - `getSalary()`
     - `getDetails()`

4. `Developer` class (extends `Employee`):
   - Properties:
     - `programmingLanguage` (String)
   - Methods:
     - `constructor(id, name, salary, programmingLanguage)`
     - `getDetails()`

5. `Manager` class (extends `Employee`):
   - Properties:
     - `department` (String)
   - Methods:
     - `constructor(id, name, salary, department)`
     - `getDetails()`
```

```
Next, recommend where exception handling should be implemented in the 'CompanyLibrary' package. Provide a rationale for your recommendations.
```

```
Next use jest to add tests for the classes in the 'CompanyLibrary' package. The tests should cover the following scenarios:

1. `Company` class:
   - Test the `constructor` method
   - Test the `addDepartment` method
   - Test the `getDetails` method
   - Test the `getDepartments` method
2. `Department` class:
   - Test the `constructor` method
   - Test the `getId` method
   - Test the `getName` method
   - Test the `addEmployee` method
   - Test the `removeEmployee` method
   - Test the `getDetails` method
   - Test the `getEmployees` method
3. `Employee` class:
    - Test the `constructor` method
    - Test the `getId` method
    - Test the `getName` method
    - Test the `getSalary` method
    - Test the `getDetails` method
4. `Developer` class:
    - Test the `constructor` method
    - Test the `getDetails` method
```
