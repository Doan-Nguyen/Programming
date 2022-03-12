# Java For Dummies (Tốc kí)
+ Notes: +22

# Table of Contents
- [Java For Dummies (Tốc kí)](#java_for_dummies)
- [Table of Contents](#table_of_contents)
    - [Introduction <a name="introduction"></a>](#1-introduction)
    - [Part 1: Getting Started <a name="getting_started"></a>](#2-getting_started)
    - [Part 2: Writing your own Java Programs <a name="writing_your_own_java_programs"></a>](#3-writing_your_own_java_programs)
## Introduction <a name="introduction"></a>

### How to use this book

## Part 1: Getting Started <a name="getting_started"></a>

### Chapter 1: All about Java

### Chapter 2: All about Software

### Chapter 3: Using the Basic Building Blocks

+ Java class:
  - Class name as same as file name (class_name.java)
  ```
  public class SimplestClass {
    public static void main(String args[]){
        System.out.println("Olleh Java !");
    }
  }
  ```
  
+ Java method:
  - Assume, you need fix the car. The list of tasks associated with your goal.
    - drive the car into garage
    - show car's problems
    - Wait to done.

  ```
  void fixCar(){
    driveIntoGarage(car, garage_location);
    showProblem(problem);
    payCost(money);
  }
  ```

+ A *method's declaration* tells the computer what happens if you call the method into action
  - A *method* is a list of things to do.

+ The main method in a program
  - Never write code that explicitly calls a *main* method into action.
  - The *main* method is called automatically when the program begins running.

  ![main_method](../figures/main_method.PNG)

+ How you finally tell the computer to do something
  - A statement tells the computer to do something.

  ![tell_computer_do_something](../figures/tell_computer_do_something.PNG)

+ Curly braces {}

  ![outline_turns_into_java_program](../figures/outline_turns_into_java_program.PNG)


## Part 2: Writing your own Java Programs

### Chapter 4: Making the most of variables and their values

#### Goals:
  - Assigning values to things
  - Making things store certain types of values
  - Applying operators to get new values

#### Assignment Statements
  - Assign a value to something (in most cases, this something is a variable)
  - The thing being assigned a value is always on the left side of the equal sign.
  
  ```
  variable = values;
  ```
  
+ Understanding the types of values that variables may have
  - *double* : -1.8x10^{308} to 1.8x10^308
  - *float* : numbers after the decimal point

+ Displaying text
  - System.out.print("Write something)

#### Java's primitive types

![java_primitive_types](../figures/java_primitive_types.PNG)

#### The char type
+ the java type used to store characters *char*

```
class CharDemo{
    public static void main(String args[]){
        char c = 'b';
        char c_big = Character.toUpperCase(c);
        System.out.println(c_big); 
    }
}
```

#### The boolean type
+ A variable of type boolean stores one of two type:
  - true
  - false
  
#### An important declaration

#### Creating new values by applying operators

#### Initialize once, assign often

#### The increment and decrement operators

+ If *++variable*:
  - the computer adds 1 to the variable's value **before** the variable is used.

+ If *variable++*:
  - the computer adds 1 to the variable's value **after** the variable is used.

```
import static java.lang.System.out;

class PreincrementDemo{
    public static void main(String args[]){
        int numberOfBunnies = 10;
        //
        ++numberOfBunnies;
        out.println(numberOfBunnies);  // 11
        int tmp = numberOfBunnies++;
        out.println(tmp);              // 11
        out.println(numberOfBunnies);  // 12
    }
}
```

#### Assignment operators

### Chapter 5: Controlling Program Flow with Decision-Making Statements

### Chapter 6: Controlling Program Flow with Loops

## Part 3: Working with the big picture: Object-Oriented Programming