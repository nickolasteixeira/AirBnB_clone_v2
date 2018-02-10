# Synopsis

The Airbnb clone project in which we are creating a copy of the [Airbnb](https://www.airbnb.com/).
Only some features will be implemented and will be listed below once compleated.


## Features

### Command Interpreter

#### Description

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Crete a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object.

#### Usage

To launch the console application in interactive mode simply run:

```./console.py ````

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

#### Commands

Commands | Description
-------- | -----------
help or ?| Displays the documented commands.
quit     | Exits the program.
EOF      | Ends the program. Used when files are passed into the program.



## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

```python3 -m unittest discover tests ```

from the root directory.

