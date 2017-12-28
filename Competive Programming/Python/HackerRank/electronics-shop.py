max_money, num_keyboard, num_mouse = map(int, input().split())
keyboard = sorted(map(int, input().split()))
mouse = sorted(map(int, input().split()))
price = [i+j for i in keyboard for j in mouse if i+j <= max_money]

print(max(price))
