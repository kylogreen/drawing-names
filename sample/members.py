# sample/members.py


class Member:
    """Represents a sole member of the group."""

    def __init__(self, name: str, email: str, excluded_member: str = None,
                 wish: str = None):
        """
        Simple constructor for creating a member.
        :param name: the person's name -- mostly nickname
        :param email: the person's email address -- used as the default
        chanel for communicating the results
        :param excluded_member: only one person may be specified as somebody to
        avoid gifting to
        :param wish: one may specify what they wish for
        """
        self.__name = name
        self.__email = email
        self.__excluded_member = excluded_member
        self.__wish = wish

    def __str__(self):
        """
        Override def. __str__ for better readability and for a easier
        debugging process.
        """
        return (f'Member({self.name},{self.email},'
                f'{self.excluded_member},{self.wish})')

    def __eq__(self, other):
        """Override def. __eq__ for simple attribute match"""
        if isinstance(other, type(self)):
            return (self.name == other.name and self.email == other.email and
                    self.excluded_member == other.excluded_member and
                    self.wish == other.wish)

    # simple class for easier testing
    @classmethod
    def bob_factory(cls):
        return cls("Bob", "bob@email.com")

    # Simple setters and getters -- no need to change name and email later on
    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def excluded_member(self):
        return self.__excluded_member

    @property
    def wish(self):
        return self.__wish

    @wish.setter
    def wish(self, wish: str):
        self.__wish = wish


def assign_wishes_to_members(members: list[Member], wishes: dict) \
        -> list[Member]:
    """
    Fill up the members with their respective wishes - if they specified one.
    :param members: list containing the members of the group
    :param wishes: a mapping between names and their specified wishes
    :return: the processed members of the group now containing their wishes too
    """

    # iterate over the members and assign their respective wish
    for member in members:
        if member.name in wishes:
            member.wish = wishes[member.name]

    return members


def get_members_email_from_group(members: list[Member], name: str) -> \
        str:
    """
    Return the given members (name only) email from the given group.
    :param members: the group of members which member is part of
    :param name: our traget member specified by only a name
    :return: the members email address
    """
    for member in members:
        if member.name == name:
            return member.email
