from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Stefi", 2, 20, 10)
        self.enemy = Hero("007", 2, 20, 10)
    
    def test_correct_initialization(self):
        self.assertEqual("Stefi", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(10, self.hero.damage)
    
    def test_correct_enemy_hero_name(self):
        self.enemy.username = self.hero.username
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(e.exception))
    
    def test_if_hero_health_is_not_enough(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))
    
    def test_if_enemy_hero_health_is_not_enough(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))
    
    def test_if_battle_is_draw(self):
        self.assertEqual("Draw", self.hero.battle(self.enemy))
    
    def test_if_hero_win_battle(self):
        self.hero.damage = 20
        self.enemy.damage = 2
        result = self.hero.battle(self.enemy)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(21, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual("You win", result)
    
    def test_if_hero_loses_battle(self):
        self.hero.damage = 2
        self.enemy.damage = 20
        result = self.hero.battle(self.enemy)
        self.assertEqual(3, self.enemy.level)
        self.assertEqual(21, self.enemy.health)
        self.assertEqual(25, self.enemy.damage)
        self.assertEqual("You lose", result)
    
    def test_str_representation(self):
        expected = (f"Hero {self.hero.username}: {self.hero.level} lvl\n"
                    f"Health: {self.hero.health}\nDamage: {self.hero.damage}\n")
        self.assertEqual(expected, str(self.hero))


if __name__ == '__main__':
    main()
