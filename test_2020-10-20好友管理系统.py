#coding=utf-8
friends = []
print(u'欢迎使用好友管理系统')
print(u'1：添加好友')
print(u'2：删除好友')
print(u'3：备注好友')
print(u'4：展示好友')
print(u'5：退出')
while True:
    num = int(input(u"请输入您的选项："))
    if num == 1:
        add_friend = input(u"请输入要添加的好友：")
        friends.append(add_friend)
        print(u'添加好友成功！')
    elif num == 2:
        del_friend = input(u"请输入要删除的好友名字：")
        friends.remove(del_friend)
        print(u'删除成功！')
    elif num == 3:
        before_friend = input(u"请输入要修改的好友名字：")
        after_friend = input(u"请输入修改后的好友名字：")
        friend_index = friends.index(before_friend)
        friends[friend_index] = after_friend
        print(u"备注成功！")
    elif num == 4:
        if len(friends) == 0:
            print(u"好友列表为空")
        else:
            for i in friends:
                print(i)
    elif num == 5:
        print(u"欢迎下次光临！")
        break
