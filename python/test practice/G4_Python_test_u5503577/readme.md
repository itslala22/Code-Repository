README
====

****

|Author|u5503577|

****

# E-Business Event Management System
------------------------------

## Explanation
-----------------------------

This E-Business Event Management System is a central component of the event management system and reproting or analysis system based on the events database and customers database, which are implemented as dictionaries in Python, where each key represents a unique event/customer ID and the associated value is another dictionary containing details about the related event/customer.


### Structure of the event database
-----------------------------

The event database in the E-Business Event Management System is structured as a Python dictionary where each event is uniquely identified by an event ID. The structure of the database includes the following information for each event:

Event ID: A unique identifier for each event.
Name: The name of the event.
Speaker: The name of the speaker for the event.
Date: The date of the event, stored as a string in the format "YYYY-MM-DD".
Capacity: The maximum number of attendees for the event.
Attendees: A counter to track the number of attendees registered for the event.
Feedback: A list to store feedback from attendees, typically as numeric ratings or text comments.
Each of these elements is a key in the dictionary, with the respective event details as values. This structure allows for efficient management and retrieval of event-related information within the system.

In addition to the event database, the E-Business Event Management System also includes a customer database. This database is designed to track customer interactions with the events and their accumulated loyalty points. Here's a brief overview of its structure:

Customer ID: A unique identifier for each customer.
Name: The name of the customer.
Loyalty Points: A numerical value representing the loyalty points accumulated by the customer, typically earned through event registrations.
Attended Events: A list of event IDs that the customer has registered for or attended.
This customer database is structured as a Python dictionary, where each customer is uniquely identified by their customer ID. The structure facilitates tracking customer engagement with events and managing their loyalty rewards within the system.


### Key Desecion Making
-------------------

#### Error-handling

It is a crucial aspect to ensure the system runs smoothly and can handle unexpected user inputs or system states. Key considerations for error-handling in this system include:

Input Validation: Checking if user inputs are in the correct format and within expected ranges (e.g., dates in "YYYY-MM-DD" format, capacity as a positive integer).
Handling Non-existent Data: Ensuring the system gracefully handles requests for events or customers that do not exist in the database.
Capacity Management: Preventing over-registration for an event by checking and enforcing the maximum capacity.
Data Type Checking: Ensuring that inputs like names, dates, and feedback are of the correct data type to prevent type errors.
Robust Feedback System: Handling a variety of feedback inputs, including edge cases where no feedback is provided.




## Testing
------------

First of all, the expected user interface should be like:

```
Welcome to E-Business Event Management System!
------------

Event creation and Management
1. Create Event
2. Modify Event
3. Register for Event
4. Check Loyalty Points
------------
Report Mechanism
5. Generate Report
------------
Feedback Mechanism
6. Record Feedback
------------
7. Exit

Enter your choice:
```
As for functions, each fuction has a definition code and the expection outcomes of each functions have both error-handling outcomes and valid outcomes.
Here are all the functions listed:
### And becasue of the limited time, not all error-handling results are listed here, but you could read this in the python code and the comments, sorry for the inconvenience!

### Function 1:
Each fuction has a definition code like this: 

```python
def create_event():
    event_id = input("Enter a unique event ID: ")
    if event_id in events:
        print("An event with this ID already exists. Please use a different ID.")
        return

    name = input("Enter the event name: ")
    speaker = input("Enter the speaker's name: ")
    date = input("Enter the event date (YYYY-MM-DD): ")
    capacity = int(input("Enter the capacity of the event: "))

    events[event_id] = {
        'name': name,
        'speaker': speaker,
        'date': date,
        'capacity': capacity,
        'attendees': 0,
        'feedback': []
    }
    print(f"Event '{name}' created successfully.")
```
And the expection outcomes of each functions have both error-handling outcomes and valid outcomes. Like followings:

Error-handling:
```
Enter your choice: 1
Enter a unique event ID: Event_id_1
An event with this ID already exists. Please use a different ID.
```
Others:
```
Enter your choice: 1
Enter a unique event ID: 123
Enter the event name: name
Enter the speaker's name: wang
Enter the event date (YYYY-MM-DD): 2023-12-12
Enter the capacity of the event: 5
Event 'name' created successfully.

```



### Function 2:

Expected:

```
Enter your choice: 2
Enter event ID: Event_id_1
Select the information you want to modify:
1. Name
2. Speaker
3. Date
4. Capacity
Enter your choice: 1
Enter new name: new meeting
Event 'new meeting' updated.
```

### Function 3:

Expected:

```
Enter your choice: 3
Enter customer ID: customer_id_1
Enter event ID: Event_id_1
Registration successful. Loyalty points updated for customer ID customer_id_1.

Welcome to E-Business Event Management System!

```

### Function 4:

Expected:

```
Enter your choice: 4
Enter customer ID: customer_id_1 
Customer ID: customer_id_1, Total Loyalty Points: 5

Welcome to E-Business Event Management System!

```

### Function 5:

Expected:

```
Enter your choice: 5
Enter event ID: Event_id_1

--- Detailed Report for Event: MKT Campagin ---
Event ID: Event_id_1
Speaker: Alice, Bob
Date: 2023-12-12
Capacity: 7, Attendees: Wang, Li
No feedback received for this event.
Exiting system.

```

### Function 6:

Expected:

```
Enter your choice: 6
Enter event ID: Event_id_1
Enter the feedback:good
Feedback recorded for event MKT Campagin.
```

### Function 7:

Expected:

```
Enter your choice: 7
Exiting system.

```


## The END

--------



