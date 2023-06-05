print('小宝')

pokemons = []
for pokemon_number in range(20):    #在这里，range()函数返回一系列数字，其唯一的用途是告诉python要循环多少次
    new_pokemon = {'HP':108,'WG':130,'WF':95,'TG':80,'TF':85,'SD':102}   #在每次循环都创建一直宝可梦（他的能力值）
    pokemons.append(new_pokemon)    #并将其附加到列表pokemons的末尾

for pokemon in pokemons[:5]:    #使用一个切片来打印前五的宝可梦
     print(pokemon)
print('一共创建烈咬陆鲨:' + str(len(pokemons)) + '只')   #打印列表的长度，以验证确实创建了20只宝可梦（烈咬陆鲨）

# username_password = {
#     'rocky':'wjh@124578',
#     'steven':'s235689',
#     'Gien':'ml051593',
#     'wang_jh':'wjh124578'
# }

# while True:
#     username = input('请输入您的账号：')
#     if username in username_password:
#         break
#     else:
#         print('您输入的账号名称不正确，请重新输入～')
#         continue

# a = 5
# while True:
#     password = input('请输入您的密码：')
#     if username_password[username] == password:
#         print('登陆成功！！！')
#         break
#     else:
#         a -= 1
#         print('您输入的密码不正确，还剩下{}次机会'.format(a))
#         continue


# a = "ADNIQDOKQIDK"
# print(a.lower())






ab = 366+78+88+93+88+105+33
print(ab)
