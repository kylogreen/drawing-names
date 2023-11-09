# tests/test_members.py

import pytest
from sample.members import Member
from sample.members import assign_wishes_to_members


@pytest.fixture
def test_example_member_bob():
    return Member("Bob", "bob@email.com")


@pytest.fixture
def test_example_member_alice():
    return Member("Alice", "alice@email.com", "Bob")


@pytest.fixture
def test_example_member_mallory():
    return Member("Mallory", "mallory@email.com",
                  "Alice", "snowflake")


def test_member_bob_factory_equal(test_example_member_bob):
    assert Member.bob_factory() == test_example_member_bob


def test_member_equality_the_same(test_example_member_bob):
    assert Member("Bob", "bob@email.com") == test_example_member_bob


def test_member_equality_not_same(test_example_member_alice):
    assert not (Member("Bob", "bob@email.com")
                == test_example_member_alice)


def test_member_instatiation_without_restriction(test_example_member_bob):
    assert (Member("Bob", "bob@email.com").__str__() ==
            test_example_member_bob.__str__())


def test_member_instatiation_without_restriction_case_miss(
        test_example_member_bob):
    assert not (Member("bob", "bob@email.com").__str__() ==
                test_example_member_bob.__str__())


def test_member_with_excluded_instantiation(test_example_member_alice):
    assert test_example_member_alice.excluded_member == "Bob"


def test_member_adding_wish(test_example_member_bob):
    test_example_member_bob.wish = "snowflake"
    assert "snowflake" == test_example_member_bob.wish


def test_member_with_wish(test_example_member_mallory):
    assert "snowflake" == test_example_member_mallory.wish


@pytest.fixture
def test_example_members_sparse_wishes():
    return [Member("Bob", "bob@email.com"),
            Member("Alice", "alice@email.com", "Bob"),
            Member("Mallory", "mallory@email.com",
                   "Alice", "snowflake")]


@pytest.fixture
def test_example_members_full_wishes():
    return [Member("Bob", "bob@email.com", excluded_member=None,
                   wish="cheesecake"),
            Member("Alice", "alice@email.com", "Bob",
                   "blue pony"),
            Member("Mallory", "mallory@email.com", "Alice",
                   "snowflake")]


@pytest.fixture
def test_example_wishes():
    return {"Bob": "cheesecake", "Alice": "blue pony", "Mallory": "snowflake"}


def test_assigning_wishes_already_full(test_example_members_full_wishes,
                                       test_example_wishes):
    flag = True
    for (m1, m2) in zip(assign_wishes_to_members(
            test_example_members_full_wishes, test_example_wishes),
            test_example_members_full_wishes):
        if not m1 == m2:
            flag = False

    assert flag


def test_assigning_wishes_scarse(test_example_members_sparse_wishes,
                                 test_example_wishes,
                                 test_example_members_full_wishes):
    flag = True
    # check each member separately
    for (m1, m2) in zip(assign_wishes_to_members(
            test_example_members_sparse_wishes, test_example_wishes),
            test_example_members_full_wishes):
        if not m1 == m2:
            flag = False

    assert flag
