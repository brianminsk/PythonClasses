# Author: Brian Minsk

donor_db = [("Dee Zaster", [10000.00, 1500.00]), 
            ("Owen Money", [7000.00]), 
            ("Shanda Lear", [100.00, 900.00, 1500.00]), 
            ("Joe King", [500.00, 700.00, 500.00]),
            ("Artie Choke", [1600.00, 1800.00])]

main_prompt = "\n".join(("Please choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

thank_you_prompt = "\n".join(("Please type a donor name or type 'list' to show all the donor names:",
          ">>> "))

donation_amount_prompt = "\n".join(("Please type the donation amount:",
          ">>> "))

def send_thank_you():
    """ Prompt the user to type a name or type 'list'. 
    - If the user types 'list' show a list of the donor names and re-prompt.
    - If the user types a name not in the list, add that name to the data structure and use it.
    - If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    - Convert the amount into a number.
    - Add that amount to the donation history of the selected user.
    Compose an email thanking the donor for their generous donation. 
    Print the email to the terminal and return to the original prompt.
    """
    donation_amount = None

    while True:
        response = input(thank_you_prompt).lower()
        if response == "list":
            show_donor_list()
        else:
            if not is_existing_donor(response):
                add_donor(response)
            donation_amount = add_donation(response)
            thank_you_message(response, donation_amount)
            break
            
def show_donor_list():
    """ Print donor names to the screen.
    """
    for donor in donor_db:
        print(donor[0])

def is_existing_donor(donor_name):
    """ Iterate through the donor db to see if the donor_name matches a donor. If so, return True. If not, return False.

    Keyword arguments:
    donor_name - string to match against the donor names in the donor db.
    """
    for donor in donor_db:
        if donor[0].lower() == donor_name.lower():
            return True
    return False

def add_donation(donor_name):
    """ Find the matching donor, prompt the user for a donation amount, 
    and add the donation to the matching donor in the donor db.
    Return the donation amount.

    Keyword arguments:
    donor_name - string to match against the donor names in the donor db.
    """
    selected_donor = None
    for donor in donor_db:
        if donor[0].lower() == donor_name.lower():
            selected_donor = donor

    donation_amount = input(donation_amount_prompt)
    
    selected_donor[1].append(float(donation_amount))

    return float(donation_amount)  

def add_donor(donor_name):
    """ Add a donor to the donor db with empty donation amounts

    Keyword arguments:
    donor_name - string representing the donor name to add to the donor db.
    """
    donor_db.append((donor_name, []))

def thank_you_message(donor_name, donation_amount):
    """ Print a thank you message to the terminal.

    Keyword arguments:
    donor_name = name of the donor
    donation_amount = donation amount as a float
    """
    print("\nDear {},".format(donor_name.title()))
    print("     Thank you very much for your generous donation of ${:.2f}.".format(donation_amount))
    print("     You ROCK!\n")

def create_report():
    """ Print a list of your donors, sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations, and average donation amount as values in each row. 
    The end result should be tabular (values in each column should align with those above and below) and look something like this:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14
    """
    # print header
    print("{:<26}| {:<11}| {:<10}| {:<12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    # print header line
    for __ in range(0,65):
        print("-", end = "")
    print("") # get a new line
    create_report_rows()
    print("")

def create_report_rows():
    """ Create the rows (as described in create_report()) with the data from the donor db, 
    sorted by total donation amount (computed by the sort_key function).
    """
    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)

    for donor in sorted_donor_db:
        total_donation = 0.0
        num_donations = 0
        for donation in donor[1]:
            total_donation += donation
            num_donations += 1
        average_donation = 0.0
        if num_donations > 0:
            average_donation = total_donation / num_donations

        print("{:<26} ${:>11.2f} ${:>10d} ${:>12.2f}".format(donor[0].title(), total_donation, num_donations, average_donation))

def sort_key(donor):
    total = 0.0
    for donation_amount in donor[1]:
        total += donation_amount
    return total
    
def main():
    """ Prompt the user to select an option (send a thank you, create a report, or quit), 
    which invokes the appropriate function. Except for the "quit" response, the others will return to this prompt after finishing.
    """
    while True:
        response = input(main_prompt)
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            break
        else:
            print("Please type '1', '2', or '3' to select one of the available options.")

if __name__ == "__main__":
   main()
