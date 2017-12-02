class user_dict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]


n_fans, can_meet = map(int, input().split())
fans_dict = user_dict()
fans_list = []


for _ in range(n_fans):
    x = input().split()

