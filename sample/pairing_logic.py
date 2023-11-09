# sample/pairing_logic.py
"""
Note:
    Switching from the `random` library to the `secrets` library would be a
    nice upgrade (at least security-wise), but considering the project's
    current security and performance priorities, random was chosen in the end.
"""

import random       # for randomizing the pairings
import time         # for timeout condition
from members import Member      # representing a member of the group


def create_pairing(members: list[Member], timeout: int = 5) -> dict:
    """
    Create the pairings for the group but work only with names.
    :param members: members list
    :param timeout: the timeout measured in minutes (default is 5 min)
    :return: the pairings in the following format:
    <gift-giver-name>:<gift-recevier-name>
    """

    # the final name pairings
    pairings = dict()
    # the group represented as a list of names
    group = list()

    # initialize the collections
    for member in members:
        group.append(member.name)
        pairings[member.name] = None

    # flag to denote a successful pairing for everyone
    successfull = False

    # set the timeout for `timeout` min
    watchdog = time.time() + 60 * timeout

    # try to find a possible pairing for everyone
    while (not successfull) and (time.time() <= watchdog):

        # initialize the recipients, the chosen and the pairings
        current_pairings = pairings.copy()
        already_chosen = list()

        # shuffle the members in place
        random.shuffle(members)

        # iterate over all the members in the group
        for member in members:

            # remove the already assigned people from the recipients
            recipients = list(set(group) - set(already_chosen))

            # check for empty recipients
            if not recipients:
                break

            # avoid self-gifting
            if member.name in recipients:
                recipients.remove(member.name)

            # remove the excluded member as possible recipient if available
            if (member.excluded_member is not None) and (
                    member.excluded_member in recipients):
                recipients.remove(member.excluded_member)

            # check again for empty recipients
            if not recipients:
                break

            # choose one randomly
            chosen = random.choice(recipients)
            # assing the pairing and add to the already chosens
            current_pairings[member.name] = chosen
            already_chosen.append(chosen)

            # once all members are assigned a pair - vefify it and quit
            if member == members[-1]:
                if None not in current_pairings.values():
                    successfull = True
                    pairings = current_pairings

    return pairings


def is_valid_pairing(members: list[Member], pairings: dict) -> bool:
    # compare lengths
    if not len(members) == len(pairings):
        return False

    # each member must be present both as a giver and as a receiver
    for member in members:
        if ((member.name not in pairings.keys())
                or (member.name not in pairings.values())):
            return False

        # restrictions must hold
        if pairings[member.name] == member.excluded_member:
            return False

    for giver, receiver in pairings.items():
        # no self gifting allowed
        if giver == receiver:
            return False

    return True


def format_pairings(pairings: dict) -> str:
    """
    Return the pairings nicely formatted.
    :param pairings: the created pairings
    :return: nicely formatted text representing the pairings
    """

    nicely_formatted_pairings = ""

    for giver, receiver in pairings.items():
        nicely_formatted_pairings += f"{giver} --> {receiver}\n"

    return nicely_formatted_pairings
