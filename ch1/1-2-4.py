# -*- coding: utf-8 -*-
# filename : tutorial2.py
# Step 1. 생성한 friends 모듈을 import합니다.
import friends as fr

# Step 2. 모듈의 작성자(author)를 출력해 봅니다.
print(fr.author)

# Step 3. 3명의 친구를 추가합니다.
friends_list = []
friends_list = fr.insert_friends(friends_list, '철수')
friends_list = fr.insert_friends(friends_list, '영희')
friends_list = fr.insert_friends(friends_list, '길동')

# Step 4. 등록된 친구를 출력합니다.
fr.display_friends(friends_list)

# Setp 5. 등록된 친구 중 첫번째 친구를 삭제합니다. 삭제한 뒤에 친구목록을 출력합니다.
friends_list = fr.delete_friends(friends_list, 0)
fr.display_friends(friends_list)
