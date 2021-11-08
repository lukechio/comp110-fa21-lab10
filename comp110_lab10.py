"""
Module: comp110_lab10

Code for COMP110 Lab Session 10 (Dictionaries and Elections)

Authors:
1) luke chiovare lchiovare@sandiego.edu
2) Natsuki Mogi nmogi@sandiego.edu
"""


import comp110_lab10


def get_election_results(election_filename):
    """ Will read in the election results and make it easier for the user to read in an ordinary fashion
    parameters: Election_filename
    """
    d = {}
    f = open(election_filename, 'r')
    f.readline()
    for line in f:
        fields = line.split(',')
        name = fields[0]
        republican = int(fields[1])
        democrat = int(fields[2])
        other = int(fields[3])
        vote_tuple = (republican, democrat, other)
        d[name] = vote_tuple
    return d


# q = get_election_results("fake_votes.txt")
# print(q)
# exit()


def main():
    """
    Gets election data from a file, then creates a pie chart showing results for
    a user-entered region.
    """

    election_filename = input("Enter the name of the election data file: ")

    # To Do: Step 1 - Call your get_election_results function to get a
    # dictionary with data. The code should go right below this comment.
    get_election_results = {vote_tuple}

    region_name = input("Enter the name of the state you want to graph: ")

    # To Do: Step 2 - Validate that the user-entered region name is a valid one
    # For example, "California" is valid while "Jefferson" is not valid.
    # You should continually re-prompt the user to enter a region name until
    # they enter a valid one. Again, the code should go immediately after this
    # comment.
    # Hint: the "in" operator will be very helpful here.

    # To Do: Step 3 - Use pyplot's pie function to make a pie chart out of the
    # election data for the user-entered region.
    # Each wedge of the pie should be labeled with the candidate's name and
    # should have the "traditional" coloring (red for Republican, blue for
    # Democratic, and black for third-party/other).
    # You should set a label for the pie chart that reads "Election results for
    # California", but modified so that "California" is replaced with whatever
    # region name the user entered.


"""
WARNING: Do NOT modify anything below this point.
"""
if __name__ == "__main__":
    main()
