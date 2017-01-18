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

From the give csv file create a list of ```students```

#### Arguments
csv file

#### Return value

list of ```students```

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

* knowledge_level
* energy_level
* laptop

#### Return value
None
