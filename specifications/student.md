# Student

The class should have a method called create_by_csv, which gets a csv file path as an argument (the csv contains all the data needed to instantiate a student object) and gives back a list of students. The class should have a constructor, which calls the Person's constructor, but also set's the attributes above (should raise an error, if any is empty).

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
Person

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge level of the student in programming
* ```energy_level```
  * data type: integer
  * description: current energy level
* ```laptop```
  * data type: class
  * description: student's laptop

## Class methods

### ```create_by_csv```

 Gets a csv file path as an argument (the csv contains all the data needed to instantiate a student object) and gives back a list of students

#### Arguments

csv_file: the file where the datas are stored

#### Return value

```CodecoolClass``` object

## Instance methods

### ```__init__```

The constructor of the object.
Calls parent class Person's constructor and also sets the attributes of this class. If any is empty: raises error.

#### Arguments

All of the arguments of the class itself.

#### Return value
None
