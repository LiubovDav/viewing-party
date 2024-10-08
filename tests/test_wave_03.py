import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()
def test_my_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Assert
    assert len(amandas_unique_movies) == 2
    assert FANTASY_2 in amandas_unique_movies
    assert INTRIGUE_2 in amandas_unique_movies
    assert amandas_data == clean_wave_3_data()

# @pytest.mark.skip()
def test_my_not_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()
    amandas_data["watched"] = []

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Assert
    assert len(amandas_unique_movies) == 0

# @pytest.mark.skip()
def test_friends_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Assert
    assert len(friends_unique_movies) == 3
    assert INTRIGUE_3 in friends_unique_movies
    assert HORROR_1 in friends_unique_movies
    assert FANTASY_4 in friends_unique_movies
    assert amandas_data == clean_wave_3_data()

# @pytest.mark.skip()
def test_friends_unique_movies_not_duplicated():
    # Arrange
    amandas_data = clean_wave_3_data()
    amandas_data["friends"][0]["watched"].append(INTRIGUE_3)


# amandas_data = 
# {
#     "watched": [
#         FANTASY_1, 
#         FANTASY_2, 
#         FANTASY_3, 
#         ACTION_1, 
#         INTRIGUE_1, 
#         INTRIGUE_2
#         ],
#     "friends": [
#         {
#             "watched": [
#                 FANTASY_1,
#                 FANTASY_3,
#                 FANTASY_4,
#                 HORROR_1,
#                 INTRIGUE_3
#             ]
#         },
#         {
#             "watched": [
#                 FANTASY_1,
#                 ACTION_1,
#                 INTRIGUE_1,
#                 INTRIGUE_3,
#             ]
#         }
#     ]
# }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

# friends_unique_movies = 
# [
#     FANTASY_4,
#     HORROR_1,
#     INTRIGUE_3
# ]

    # Assert
    assert len(friends_unique_movies) == 3

    # raise Exception("Test needs to be completed.")
    # *************************************************************************************************
    # ****** Add assertions here to test that the correct movies are in friends_unique_movies **********
    # **************************************************************************************************

    assert friends_unique_movies[0]["title"] == FANTASY_4["title"]
    assert friends_unique_movies[1]["title"] == HORROR_1["title"]
    assert friends_unique_movies[2]["title"] == INTRIGUE_3["title"]


# @pytest.mark.skip()
def test_friends_not_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [
            HORROR_1,
            FANTASY_1,
            INTRIGUE_1
        ],
        "friends": [
            {
                "watched": [
                    HORROR_1,
                    FANTASY_1,
                ]
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Assert
    assert len(friends_unique_movies) == 0
