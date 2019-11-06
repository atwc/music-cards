#
#
# BIPBIP ZIZIK
# Unit test for CardList class
#
#

import unittest

from cards.CardReader import CardBdd


class CardLisTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bdd = CardBdd('https://bipbipzizik.firebaseio.com/', 'cards_test')
        cls.bdd.delete()
        cls.bdd.write_card(user="user1",
                       name="name1",
                       comment="comment1",
                       ids="id1",
                       mode="mode1",
                       action="command",
                       data="data1")

        cls.bdd.write_card(user="user2",
                       name="name2",
                       comment="comment2",
                       ids="id2",
                       mode="mode2",
                       action="spotify:album",
                       data="data2")

        cls.bdd.write_card(user="user3",
                       name="name3",
                       comment="comment3",
                       ids="id3",
                       mode="mode3",
                       action="spotify:playlist",
                       data="data3")

        cls.bdd.write_card(user="user4",
                       name="name4",
                       comment="comment4",
                       ids="id4",
                       mode="mode4",
                       action="spotify:track",
                       data="data4")

        cls.bdd.write_card(user="user5",
                       name="name5",
                       comment="comment5",
                       ids="id5",
                       mode="mode5",
                       action="tunein",
                       data="data5")

    # def setUp(self):
        # nothing yet

    def test_read_card(self):
        card_expected = {  "user": "user5",
                           "name": "name5",
                           "comment": "comment5",
                           "ids": "id5",
                           "mode": "mode5",
                           "action": "tunein",
                           "data": "data5"}

        card = self.bdd.get_card("id5")

        self.assertEqual(card.parameters, card_expected)

    def test_read_card_command(self):

        command_expected = "data1"
        card = self.bdd.get_card("id1")
        mode = card.get_mode()
        command = card.get_command()

        self.assertEqual(mode, "mode1")
        self.assertEqual(command, command_expected)

        command_expected = "spotify/now/spotify:album:data2"
        card = self.bdd.get_card("id2")
        mode = card.get_mode()
        command = card.get_command()

        self.assertEqual(mode, "mode2")
        self.assertEqual(command, command_expected)

        command_expected = "spotify/now/spotify:user:spotify:playlist:data3"
        card = self.bdd.get_card("id3")
        mode = card.get_mode()
        command = card.get_command()

        self.assertEqual(mode, "mode3")
        self.assertEqual(command, command_expected)

        command_expected = "spotify/now/spotify:track:data4"
        card = self.bdd.get_card("id4")
        mode = card.get_mode()
        command = card.get_command()

        self.assertEqual(mode, "mode4")
        self.assertEqual(command, command_expected)

        command_expected = "tunein/play/data5"
        card = self.bdd.get_card("id5")
        mode = card.get_mode()
        command = card.get_command()

        self.assertEqual(mode, "mode5")
        self.assertEqual(command, command_expected)


if __name__ == '__main__':

    unittest.main()

