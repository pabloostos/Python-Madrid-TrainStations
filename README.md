# Group assignment - Moving Around Madrid

<!-- vscode-markdown-toc -->
* [General Information](#GeneralInformation)
	* [Deadline](#Deadline)
	* [Rubric](#Rubric)
* [Problem](#Problem)
	* [Exercise 1 - counting the number of Metro stations](#Exercise1-countingthenumberofMetrostations)
	* [Exercise 2 - most connected stations](#Exercise2-mostconnectedstations)
	* [Exercise 3 - closest stations](#Exercise3-closeststations)
	* [Exercise 4 - finding a route](#Exercise4-findingaroute)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=false
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='GeneralInformation'></a>General Information

This repository contains the materials for the Group Assignment of Programming Fundamentals with Python.

### <a name='Deadline'></a>Deadline

The exercise must be submited **before** `11/20/2022 23:00 +0100`.  Only code pushed to the Github repository created by Github classroom will be evaluated.

### <a name='Rubric'></a>Rubric

| Section    | Max points |
|------------|------------|
| Exercise 1 | 2 points   |
| Exercise 2 | 2 points   |
| Exercise 3 | 2 points   |
| Exercise 4 | 2 points   |
| All members of the group participated[^1] | 1 points   |
| Code quality | 1 points   |


## <a name='Problem'></a>Problem

In this workgroup exercise you'll be working with the Metro de Madrid stations data.

In order to solve these problems you can create as much auxiliary code as you need, and distribute it in the project as you see fit.  You can create auxiliary packages and modules if you need them.

### <a name='Exercise1-countingthenumberofMetrostations'></a>Exercise 1 - counting the number of Metro stations

Create a function `exercise_1` in `main.py` that returns the number of stations that exist in the Metro network (according to the data you have in the CSV files)

### <a name='Exercise2-mostconnectedstations'></a>Exercise 2 - most connected stations

Create a function `exercise_2` in `main.py` that returns a list of the top 5 stations by number of lines available in them, sorted by which one has more lines available.

### <a name='Exercise3-closeststations'></a>Exercise 3 - closest stations

Create a function `exercise_3` in `main.py` that receives a Metro station name and returns a list with other stations that are one stop away.

### <a name='Exercise4-findingaroute'></a>Exercise 4 - finding a route

Create a function `exercise_4` in `main.py` that receives the names of two Metro stations as parameters, and returns a way to go from one to another, in case there's a way.

The returned data should be a list containing all Metro stations one would need to go through from start to finish.

```python
exercise_4("Concha Espina", "Pirámides")
# Would return something like
# ["Concha Espina", "Cruz del Rayo", "Avenida de América", "Núñez de Balboa", "Príncipe de Vergara", "Retiro", "Banco de España", "Sevilla", "Sol", "Opera", "La Latina", "Puerta de Toledo", "Acacias", "Pirámides"]
```




[^1]: This requirement will be fulfilled if there's at least one commit by each member of the group