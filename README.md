<snippet>
<content>
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
To run tests, in the root directory after installing coverage run `coverage run -m unittest discover tests` then run `coverage report -m unittest discover tests` to get percentage coverage. To run tests without coverage simply run
`python -m unittest discover tests`.

###### Starting the program
After successful installation, open your command line and run `python`. When the python interpreter opens run
`from allocate.operation import *`. Then run `main()` to start the program.

###### Help
Type `help` to get a list of commands you can run. Type `help <command>` to know more about each command. 
e.g. `help pre_populate`

###### Pre-populate
You must run `pre_populate` to create and pre-populate the database.

###### Batch Allocate
Run `batch_allocate <fullpathtofile>` to load data from either a .txt or .csv file
(e.g. `batch_allocate C:\Users\Andela\test.txt`). Don't worry about '\' or '/' the program takes care of that.

###### Format of input files
Each line hold data for one person only in the following format:
`<FIRSTNAME> <LASTNAME> <FELLOW|STAFF> <Y|N> <MALE|FEMALE>`
<MALE|FEMALE> is optional, if not stated fellow will be added to a mixed room. i.e.
```
ANDREW PHILLIPS	FELLOW	Y
MATTHEW O'CONNOR	STAFF
JOHN ADEWALE	FELLOW	N
IYANU ALIMI		FELLOW	Y
AHMED AKUBE		STAFF
TOSIN ADE     Y
```

###### Get Allocation
Run `get_allocation` to display all rooms with people allocated to them. If a room has no one, it is shown as empty.

###### Print Allocation
Run `print_allocation` prints out room allocation into a file stored in the user's root directory.

###### Get Unallocated
Run `get_unallocated` to display people that haven't yet been allocated to offices or living spaces.

###### Add Room
Run `add_room` to add a new room.

###### Get Room
Run `get_room` to display the occupants of a room.

###### Reset
Run `reset` to clear the database of all data. Remember to run `pre_populate` to add back deleted offices and living spaces.

###### Quit
Run `quit` to close the program.


## Credits
Thanks to God, myself and the vending machine at amity. And Chidi for allowing extra time to work on this project :)

## License
MIT License 
</content>
</snippet>
