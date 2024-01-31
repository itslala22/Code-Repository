# E-Business Event Management System

# Create event and customer databases by using dictionaries to store information
# Event database Example:
events = {
    'Event_id_1': {'name': "MKT Campagin", 'speaker': "Alice, Bob", 'date': "2023-12-12", 'capacity': 7, "attendees": 2, "feedback": []},
    'Event_id_2': {'name': "DM Discussion", 'speaker': "Alice", 'date': "2024-01-30", 'capacity': 8, "attendees": 3, "feedback": []},
    # Add more events as needed
}
# Customer database example:
customers = {
    "customer_id_1":{"name": "Alice", "loyalty_points": 5, "attended_events": []},
    "customer_id_2":{"name": "Bob", "loyalty_points": 8, "attended_events": []},
}

# Assuming each event registration gives a fixed amount of loyalty points
LOYALTY_POINTS_PER_EVENT = 10




# Python Fuctions
# 1. Event creaction and Management Fuctions:

# 1.1 Function to create the event
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


# 1.2 Function to modify an existing event
def modify_event(event_id):
    if event_id in events:
        print("Select the information you want to modify:")
        print("1. Name")
        print("2. Speaker")
        print("3. Date")
        print("4. Capacity")
        modification_choice = input("Enter your choice: ")

        if modification_choice == '1':
            new_name = input("Enter new name: ")
            events[event_id]['name'] = new_name
        elif modification_choice == '2':
            new_speaker = input("Enter new speaker: ")
            events[event_id]['speaker'] = new_speaker
        elif modification_choice == '3':
            new_date = input("Enter new date (YYYY-MM-DD): ")
            events[event_id]['date'] = new_date
        elif modification_choice == '4':
            new_capacity = int(input("Enter new capacity: "))
            events[event_id]['capacity'] = new_capacity
        else:
            print("Invalid choice.")
        
        print(f"Event '{events[event_id]['name']}' updated.")
    else:
        print("Event not found.")


# 1.3 Function to register for an event and accumulate loyalty points
def register_for_event_and_accumulate_points(customer_id, event_id):
    if event_id not in events:
        print("Event does not exist.")
        return

    if events[event_id]['attendees'] >= events[event_id]['capacity']:
        print("This event is already full.")
        return

    # Register the customer for the event
    events[event_id]['attendees'] += 1

    # Update or create the customer record in the customer database
    if customer_id in customers:
        customers[customer_id]['loyalty_points'] += LOYALTY_POINTS_PER_EVENT
        customers[customer_id]['attended_events'].append(event_id)
    else:
        customers[customer_id] = {
            'loyalty_points': LOYALTY_POINTS_PER_EVENT,
            'attended_events': [event_id]
        }

    print(f"Registration successful. Loyalty points updated for customer ID {customer_id}.")



# 1.4 Function to display total loyalty points for a customer
def display_loyalty_points(customer_id):
    if customer_id in customers:
        print(f"Customer ID: {customer_id}, Total Loyalty Points: {customers[customer_id]['loyalty_points']}")
    else:
        print("Customer not found.")




# 2. Report Mechanism Functions:
        
# 2.1 Function to generate a report on event attendance, participant feedback, and other useful metrics
def generate_report_with_feedback(event_id):
    if event_id in events:
        event = events[event_id]
        print(f"\n--- Detailed Report for Event: {event['name']} ---")
        print(f"Event ID: {event_id}")
        print(f"Speaker: {event['speaker']}")
        print(f"Date: {event['date']}")
        print(f"Capacity: {event['capacity']}, Attendees: {event['attendees']}")

        # Display all feedback
        if event['feedback']:
            print("Feedback Received:")
            for i, feedback in enumerate(event['feedback'], 1):
                print(f"  {i}. {feedback}")
        else:
            print("No feedback received for this event.")

        # Additional event-specific metrics can be added here as needed

    else:
        print("Invalid event ID.")




# 3. Feedback Mechanism Functions:

# 3.1 Function to record feedback
def record_feedback(event_id, feedback):
    if event_id in events:
        events[event_id]['feedback'].append(feedback)
        print(f"Feedback recorded for event {events[event_id]['name']}.")
    else:
        print("Invalid event ID.")




# User Interface:
        
def main_menu():
    while True:
        print("\nWelcome to E-Business Event Management System!")
        print("------------")
        print("\nEvent creation and Management")
        print("1. Create Event")
        print("2. Modify Event")
        print("3. Register for Event")
        print("4. Check Loyalty Points")
        print("------------")
        print("Report Mechanism")
        print("5. Generate Report")
        print("------------")
        print("Feedback Mechanism")
        print("6. Record Feedback")
        print("------------")
        print("7. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            create_event()
        
        elif choice == '2':
            event_id = input("Enter event ID: ")
            modify_event(event_id)


        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            event_id = input("Enter event ID: ")
            register_for_event_and_accumulate_points(customer_id, event_id)

        elif choice == '4':
            customer_id = input("Enter customer ID: ")
            display_loyalty_points(customer_id)
            
        elif choice == '5':
            event_id = input("Enter event ID: ")
            generate_report_with_feedback(event_id)
            print("Exiting system.")

        elif choice == '6':
            event_id = input("Enter event ID: ")
            feedback = input("Enter the feedback:")
            record_feedback(event_id, feedback)

        elif choice == '7':
            print("Exiting system.")
            break

        else:
            print("Invalid choice, please try again.") #Error Handling

# Start the system
main_menu()