# sample/input_parser.py

import csv  # parsing csv files
from sample.members import Member  # representing each of the members


def parse_members_from_file(members_file: str) -> list:
    """
    Parse the members of the group from the specified csv file.
    Disclaimer: No input sanitization of any kind is done here!
    :param members_file: csv file containing the members of the group
    -- each member on a separate line
    -- must adhere to the following format
    <name>,<email>,<(optional)excluded-member>
    :return: a list of member objects
    """

    # a list containing the processed members
    parsed_members = list()

    # leave new line mode as universal (default)
    with open(members_file, mode='r', encoding="utf-8") as f_handle:
        reader = csv.reader(f_handle)
        # line by line assign the data to the respective attributes
        for line in reader:
            name = line.pop(0)
            email = line.pop(0)
            excluded_member = None
            if line:
                excluded_member = line.pop(0)

            # create respective member object
            member = Member(name, email, excluded_member)
            # add member to the members list
            parsed_members.append(member)

    return parsed_members


def parse_wishes_from_file(wishes_file: str) -> dict:
    """
    Read in the provided `wishes_file` and process it by creating a mapping
    between a member (referred here only by name) and his/her wishes.
    :param wishes_file: containing the specified wishes
    -- format after generating the csv file containing the responses for the
    Google Forms:
    "<timestamp>,"<name>","<wish-available>","(optional)<specifiec-wish>"
    :return: a map between a members name and his/her wishes
    """

    # mappings between name and wish
    wishes = dict()

    # leave new line mode as universal (default)
    with open(wishes_file, mode='r', encoding="utf-8") as f_handle:
        reader = csv.reader(f_handle)
        # skip the header line
        reader.__next__()
        # line by line assign the data to the respective attributes
        for line in reader:
            # skip if no wish was specified
            if line[2] == "No":
                continue
            wishes[line[1]] = line[3]

    return wishes
