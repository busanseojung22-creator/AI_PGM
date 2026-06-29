dict1 = {"name": "Alice", "age": 30, "city": "New York"}
dict2 = {"name": "Bob", "age": 25, "city": "Los Angeles"}
# for key in dict1: 
#      print(f"{key}: {dic1[key]}")

def create_profile(**info):
     print("=== 프로필 정보 ===")
     for key, value in info.items():
         print(f"{key}: {value}")
 
 create_profile(이름='김철수', 나이=30, 직업='프로그래머', 취미='독서')

