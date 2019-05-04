def receive_tuple_and_dict(*friend, **who):
    """
        参数(形参)前面加 * 代表接收一个元组
        参数(形参)前面加 ** 代表接收一个元组
    :param friend: 朋友
    :param who: 人
    :return:
    """
    print(friend)
    print(who)


human = {
    'name': 'Xiao Tian',
    'age': 'test'
}
friends = ('Xiao Ming', 'Xiao Hui')

receive_tuple_and_dict(*friends, *friends, **human)
receive_tuple_and_dict(*friends, **human)

receive_tuple_and_dict('Xiao Ming', 'Xiao Hui', **human)
receive_tuple_and_dict(*friends, **{'name': 'Xiao Tian', 'age': 'test'})

print(*friends)
print(*human)
