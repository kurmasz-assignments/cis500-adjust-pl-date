
**Important**: If you choose to complete this assignment, please follow this link to create a GitHub repository for your work: <https://classroom.github.com/a/X7giQMMP>

# Adjusting .json Data

In PrairieLearn, assignments are described by `.json` data.  This data 
includes 
1. The assignment's title and other meta-data
2. Information about the assignment's due dates (and how much credit students get for late submissions)
3. The individual problems included in the assignment.

You can see several examples in the `data` directory.

## Your assignment

Write a python script that will adjust the due dates for an assignment. The program should take as input
1. The name of an `.json` file that describes an assignment
2. The "start date" for that assignment. (That is the day the assignment is first used during lecture.)

The program should then produce a new `.json` files with updated `startDate`s and `endDate`s.

* Each different due date is described by a Dictionary in a list named `allowAccess`.
* Ignore any entries that contain `uids`. These are for special cases.
* Make `startDate` equal to the date given by the user.
* If the `credit` field is 95 or greater, then choose `endDate` as follows:
  * If the new start date is a Monday or Tuesday, then `endDate` should be at 11:59 p.m. that Friday.
  * If the new start date is a Wednesday then `endDate` should be 11:59 p.m. the following Tuesday.
  * If the new start date is a Thursday then `endDate` should be 11:59 p.m. the following Wednesday.
  * If the new start date is a Friday then `endDate` should be 11:59 p.m. the following Thursday.
* If the `credit` filed is between 40 and 80, then `endDate` should be at 11:59 p.m. two days after the value when `credit` is 95.
* If the `credit` field is less than 25, `endDate` should be 11:59 p.m. on 25 April, 2025.

Have the new values replace the old values (i.e., overwrite the input file).

You may use `pl_adjust_date.py` as a starting point, if you like.

