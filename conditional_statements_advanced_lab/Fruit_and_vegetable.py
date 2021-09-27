item = input()
fruit_list = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
veg_list = ['tomato', 'cucumber', 'pepper', 'carrot']
if item in fruit_list:
    print('fruit')
elif item in veg_list:
    print('vegetable')
else:
    print('unknown')