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

    @excluded_member.setter
    def excluded_member(self, excluded_member: str):
        self.__excluded_member = excluded_member

    @property
    def wish(self):
        return self.__wish

    @wish.setter
    def wish(self, wish: str):
        self.__wish = wish
