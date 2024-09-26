import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()
def test_get_available_friend_rec():
    # Arrange
    amandas_data = clean_wave_4_data()

# amandas_data =
# {
#     "watched": [
#         FANTASY_1b, 
#         FANTASY_2b, 
#         FANTASY_3b, 
#         ACTION_1b, 
#         INTRIGUE_1b, 
#         INTRIGUE_2b
#         ],  
#     "friends": [
#         {
#             "watched": [
#                 FANTASY_1b,
#                 FANTASY_3b,
#                 FANTASY_4b,
#                 HORROR_1b,
#             ]
#         },
#         {
#             "watched": [
#                 FANTASY_1b,
#                 FANTASY_4b,
#                 ACTION_1b,
#                 INTRIGUE_1b,
#                 INTRIGUE_3b,
#             ]
#         }  
#     ],
#     "subscriptions": ["netflix", "hulu"]
# }

    # Act
    recommendations = get_available_recs(amandas_data)

# recommendations = 
# [
#     FANTASY_4b,
#     HORROR_1b
# ]

    # Assert
    assert len(recommendations) == 2
    assert HORROR_1b in recommendations
    assert FANTASY_4b in recommendations
    assert amandas_data == clean_wave_4_data()

# @pytest.mark.skip()
def test_no_available_friend_recs():
    # Arrange
    amandas_data = {
        "subscriptions": ["hulu", "disney+"],
        "watched": [],
        "friends": [
            {
                "watched": [HORROR_1b]
            },
            {
                "watched": [FANTASY_3b]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Assert
    assert len(recommendations) == 0

# @pytest.mark.skip()
def test_no_available_friend_recs_watched_all():
    # Arrange
    amandas_data = {
        "subscriptions": ["netflix", "amazon"],
        "watched": [HORROR_1b, FANTASY_3b],
        "friends": [
            {
                "watched": [HORROR_1b]
            },
            {
                "watched": [FANTASY_3b]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) == 0
