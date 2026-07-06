class Shape:
    def __init__(self, name):
        self.name = name
        
    def area(self):
        # 자식 클래스에서 반드시 이 메서드를 오버라이딩하도록 강제하는 장치입니다.
        raise NotImplementedError("Subclasses must implement this method")

# 1. Circle 클래스 수정
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle") # 부모 생성자에 이름 전달
        self.radius = radius       # Circle만의 고유 속성
        
    def area(self):                # area 메서드 정상 정의
        return 3.14159 * (self.radius ** 2)

# 2. Rectangle 클래스 수정
class Rectangle(Shape):            # 클래스명 오타 수정
    def __init__(self, width, height): # 매개변수 오타(wifth) 수정
        super().__init__("Rectangle")  # super() 괄호 누락 및 들여쓰기 수정
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height


# 3. 리스트 및 반복문 오타 수정
shapeList = [Circle(5), Rectangle(4, 5)]

for shape in shapeList: # 변수명 대소문자 통일
    # shaple -> shape 오타 수정, 소수점 2자리 깔끔하게 출력(:.2f)
    print(f"{shape.name} area: {shape.area():.2f}")