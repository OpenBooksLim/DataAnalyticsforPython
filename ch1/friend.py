# -*- coding: utf-8 -*-
# filename : friend.py
class friend:
    def set_info(self, name, height):
        self.name = name
        self.height = height

    def print_info(self):
        print('---------------')
        print('이름 : ', self.name)
        print('신장 : ', self.height)
        print('---------------')

if __name__ == "__main__":
    each_friend = friend()
    print(each_friend)

    each_friend.set_info('철수', 180)
    print(each_friend.name + '는 키가 ' + str(each_friend.height) + '입니다.')

    each_friend.print_info()