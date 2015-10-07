<snippet>
<content>
<![CDATA[
# allocate
Models a room allocation system for Amity(A company office/hostel facility). 

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

allocate takes a list of employees which can be either staff or fellows, from either a .txt or .csv file and allocates them randomly to office rooms and living spaces.

## Features
* Runtime error handling: users can correct format errors in data that is being processed without having to terminate the program.
* People can be allocated to three types of living rooms: male, female or mixed. Mixed is the default if the person's gender is not specified.
* Data is persistent. So even if you terminate the program and start again, the data and changes you were working on still exist.
* Input can be from either a .txt or .csv file.
* Output can be in a .txt or .csv file.
* Display list of allocations.
* Display unallocated people.
* Display members of a room.

## Installation
Run `python setup.py install` in the root directory.

## Usage


## Credits
Thanks to God, myself and the vending machine at amity. And Chidi for allowing extra time to work on this project :)

## License


]]>
</content>
</snippet>
