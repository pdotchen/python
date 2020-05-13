class Monster():
    def __init__(self, name, hp=20):
        dict_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3, 'whirlwind': 3, 'earthquake': 2,
                        'double_hit': 4, 'wait': 0}
        self.name = name
        self.type = "Normal"
        self.current_hp = hp
        self.max_hp = hp
        self.exp = 0
        self.attacks = {'wait': 0}
        self.possible_attacks = dict_attacks

    def add_attack(self, attack_name):
        if attack_name in self.attacks:
            return False
        if attack_name not in self.possible_attacks:
            return False
        if len(self.attacks) == 0:
            self.attacks['wait'] = self.possible_attacks['wait']

        org_attacks = dict()  # from lecture 17, professor code
        for key in self.attacks.keys():
            value = self.attacks[key]
            if value in org_attacks.keys():
                org_attacks[value].append(key)
            else:
                org_attacks[value] = [key]

        min_point = min(org_attacks.keys())

        min_attack = org_attacks[min_point]

        lowest_attack = 'zzz'
        for attack in min_attack:
            if attack < lowest_attack:
                lowest_attack = attack

        if len(self.attacks) == 4:
            self.attacks.pop(lowest_attack)

        self.attacks[attack_name] = self.possible_attacks[attack_name]
        return True

    def remove_attack(self, attack_name):
        if len(self.attacks) == 0:
            self.attacks['wait'] = self.possible_attacks['wait']

        if self.attacks == {'wait': 0}:
            return True

        if attack_name in self.attacks:
            self.attacks.pop(attack_name)
            return True
        else:
            return False

    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp


def monster_fight(monster1, monster2):
    first = monster1
    second = monster2
    if first.attacks == {'wait': 0} and second.attacks == {'wait': 0}:
        return -1, None, None
    round_num = 0
    counter1 = 0
    counter2 = 0
    moves1 = []
    moves2 = []
    attack_value1 = sorted(first.attacks.values(), reverse=True)
    attack_value2 = sorted(second.attacks.values(), reverse=True)
    attack_key1 = sorted(first.attacks, key=lambda x: (x[1]), reverse=True)
    attack_key2 = sorted(second.attacks, key=lambda x: (x[1]), reverse=True)
    for y in range(len(attack_value1) - 1):
        if attack_value1[y] == attack_value1[y + 1]:
            if attack_key1[y] > attack_key1[y + 1]:
                temp = attack_key1[y]
                attack_key1[y] = attack_key1[y + 1]
                attack_key1[y + 1] = temp
    for x in range(len(attack_value2) - 1):
        if attack_value2[x] == attack_value2[x + 1]:
            if attack_key2[x] > attack_key2[x + 1]:
                temp = attack_key2[x]
                attack_key2[x] = attack_key2[x + 1]
                attack_key2[x + 1] = temp

    while first.current_hp > 0 and second.current_hp > 0:
        round_num += 1
        second.current_hp -= attack_value1[counter1]
        moves1.append(attack_key1[counter1])
        counter1 += 1
        if counter1 >= len(attack_key1):
            counter1 = 0
        if second.current_hp <= 0:
            break
        first.current_hp -= attack_value2[counter2]
        moves2.append(attack_key2[counter2])
        counter2 += 1
        if counter2 >= len(attack_key2):
            counter2 = 0

    if first.current_hp <= 0:
        winner_mon = second
        second.win_fight()
        first.lose_fight()
        return round_num, winner_mon, moves2
    elif second.current_hp <= 0:
        winner_mon = first
        first.win_fight()
        second.lose_fight()
        return round_num, winner_mon, moves1


class Ghost(Monster):
    def win_fight(self):
        num = self.exp
        self.exp += 5
        self.current_hp = self.max_hp
        if (10 - num % 10) <= 5:
            self.max_hp += 5
            self.current_hp = self.max_hp

    def lose_fight(self):
        num = self.exp
        self.exp += 1
        self.current_hp = self.max_hp
        if (10 - num % 10) <= 1:
            self.max_hp += 5
            self.current_hp = self.max_hp


class Dragon(Monster):
    def win_fight(self):
        self.exp += 5
        self.current_hp = self.max_hp
        if self.exp >= 10:
            tens = self.exp // 10
            for x, y in self.attacks.items():
                self.attacks[x] = y + tens

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp
        if self.exp >= 10:
            tens = self.exp // 10
            for x, y in self.attacks.items():
                self.attacks[x] = y + tens
