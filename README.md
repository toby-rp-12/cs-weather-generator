# cs-weather-generator
A random weather generator in python.

## Project Overview

This program is a simple Python command-line program that randomly generates daily temperatures for a user-defined number of days within a chosen temperature range.

The program asks the user for:
- The number of days to generate weather for
- A minimum temperature
- A maximum temperature

It then generates a random temperature for each day within the given range.

The project demonstrates basic Python concepts such as input handling, loops, error checking, and random number generation.

## Key Features

- Generates random daily temperatures
- User-defined number of days
- Custom temperature range
- Prevents temperatures below absolute zero
- Ensures the maximum temperature is greater than the minimum
- Uses Python’s built-in `random` module
- Clear command-line output

## How It Works

1. The user enters how many days of weather to generate.
1. The user enters the lowest possible temperature (temperatures below **-460°F*** more or less absolute zero/0º Kelvin,** are rejected).
1. The user enters the highest possible temperature (the value must be higher than the minimum temperature).
1. The program prints a random temperature for each day.

## Example Output
```
  Welcome to weather generator!
  Enter the number of days you want us to generate weather for.
>> 3
  Enter the lowest you want the temprature to go to.
>> 40
  Enter the highest you want the temprature to go to.
>> 75
  Day 1 : 62 ° F
  Day 2 : 44 ° F
  Day 3 : 71 ° F
  Thank you for using weather generator! Restart the program to go again.
```

## How to Set Up and Run

### Requirements

- Python 3.x
- No external libraries required

### Setting up the Program
1. Make sure Python 3 is installed.
1. Save the program. You can call it:
```
weather.py
```
1. Navigate to the folder containing the file.
1. Run the program in python!
