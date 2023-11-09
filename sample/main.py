# sample/main.py

import input_parser     # parsing and processing the data
import members          # representing the people of the group
import pairing_logic    # maching up gifters with giftees
import communication    # creating secure connection and sending emails

# some constants to configure
SENDER_EMAIL = "sender@gmail.com"
BACKUP_TO_SEND_TO = "backup@gmail.com"
API_KEY = "4242424242424242"
MEMBERS_FILE = r"..\data\members.csv"
WISHES_FILE = r"..\data\wishes.csv"


def main() -> int:
    """The main program - parse/process input, draw the names, send the
    nofitications. Lastly, send yourself a verification email as a backup."""

    # processing and parsing the input data
    group = input_parser.parse_members_from_file(MEMBERS_FILE)
    wishes = input_parser.parse_wishes_from_file(WISHES_FILE)
    group = members.assign_wishes_to_members(group, wishes)

    # create the appropriate pairings
    pairings = pairing_logic.create_pairing(group)

    # for verification
    group_len = len(group)
    counter = 0

    # notify the members via email
    for member in group:
        # select recips name and email
        recipient = pairings[member.name]
        recips_email = members.get_members_email_from_group(group, member.name)

        # mention only the specified wishes in the emails
        if recipient in wishes.keys():
            wish = wishes[recipient]
        else:
            wish = None

        # choose a language for the text to appear in
        display_lang = "EN"

        # craft the message body and adjust it appropriately
        message = communication.craft_message(member.name, recipient, wish,
                                              display_lang)
        # notify the gifter of the drawing results
        successfully_sent = (
            communication.send_email(SENDER_EMAIL, API_KEY, recips_email,
                                     message,
                                     display_lang))

        if successfully_sent:
            counter += 1
            print(f"{counter:02}/{group_len} [{"#"*counter}"
                  f"{"."*(group_len-counter)}]")
        else:
            print("[ERROR] message was not sent correctly for:", member)

    # everything went well - send the verification email
    if counter == group_len:
        pairings_str = pairing_logic.format_pairings(pairings)
        communication.send_verification_email(SENDER_EMAIL, API_KEY,
                                              BACKUP_TO_SEND_TO, pairings_str)
        # be a nice c-lad/c-gal and return 0 :P
        return 0
    else:
        # or otherwise...
        return -1


if __name__ == "__main__":
    main()
