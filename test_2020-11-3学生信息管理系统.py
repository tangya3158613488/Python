# 功能菜单打印
def print_menu():
    print('=' * 30)
    print('欢迎来到学生信息管理系统^^')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示所有学生信息')
    print('0.退出系统')
    
# 新建一个列表，用来保存所有学生信息
stu_info = []
#添加学生信息
def add_stu_info():
    new_name = input('请输入新学生的姓名：>')
    new_sex = input('请输入新学生的性别：>')
    new_phone = input('请输入新学生手机号：>')

    new_info = dict()
    new_info['name'] = new_name
    new_info['sex'] = new_sex
    new_info['phone'] = new_phone

    stu_info.append(new_info)
    
# 删除学生信息
def del_stu_info(student):
    del_num = int(input('请输入要删除的序号：')) - 1
    del student[del_num]
    if len(stu_info) != 0:
        show_stu_info()
    
# 修改学生信息
def modify_stu_info():
    if len(stu_info) != 0:
        stu_id = int(input('请输入学生的序号：>'))
        stu_name = input('请输入学生的姓名：>')
        stu_sex = input('请输入学生的性别（男/女）：>')
        stu_phone = input('请输入学生的电话号码：>')

        stu_info[stu_id - 1]['name'] = stu_name
        stu_info[stu_id - 1]['sex'] = stu_sex
        stu_info[stu_id - 1]['phone'] = stu_phone
    else:
        print('学生信息表为空')

# 显示所有学生信息
def show_stu_info():
    print('学生的信息如下：')
    print('=' * 30)
    print('序号 姓名  性别  手机号码')
    i = 1
    for temp_info in stu_info:
        print('%d    %s  %s  %s' %(i,temp_info['name'],temp_info['sex'],temp_info['phone']))
        i += 1

# 主函数
def main():
    while True:
        print_menu()
        key = input('请选择功能选项：>')
        if key == '1':
            add_stu_info()
        elif key == '2':
            del_stu_info(stu_info)
        elif key == '3':
            modify_stu_info()
        elif key == '4':
            show_stu_info()
        elif key == '0':
            quit_confirm = input('亲，真的要退出吗？（Yes or No）：')
            if quit_confirm == 'Yes':
                print('欢迎下次光临哦！')
                break
            else:
                print('输入有误，请重新输入')


if __name__ == '__main__':
    main()
