# 그림을 그리기 위해 turtle 모듈 임포트
import turtle
# 눈송이를 그리기 위한 점 위치 계산 과정에서 필요한 모듈(삼각함수, 제곱, 제곱근)
import math
# 타입 지정중 튜플과 리스트를 지저와기 위해 필요
from typing import Tuple, List
# 프랙탈을 진행할 단계 수
FRACTAL_LEVEL: int = 10000

# 프랙탈 제작 과정을 보여주는지 여부
SHOW_PROCESS: bool = True
# 주요 클래스
class Main:
# 초기화
    def __init__(self):
        # 터틀 객체를 하나 생성
        self.t: turtle.Turtle = turtle.Turtle()
        # 객체의 기본 설정
        self.t.hideturtle()
        self.t.getscreen().bgcolor("Black")
        self.t.color("White")
        self.t.penup()
        # 캔버스 설정
        turtle.setup(1000, 1000, 100, 100) 
    # 시작부터 끝 좌표까지 설정된 단계만큼 코흐의 곡선을 그림
    def execute(self, loop_num: int, pos1: Tuple[float, float], pos2: Tuple[float, float], show_process: bool = False):
        # 시작 과표와 끝 좌표
        dot_list: List[Tuple[float, float]] = [pos1, pos2]
        # 단계 수 만큼 진행
        for _ in range(loop_num):
        # 다음 단계 저장
            next_dots_list: List[Tuple[float, float]] = [dot_list[0]]
        # 코흐 곡선 규칙에 따라 한 선에서 삼각형을 그림
            for i in range(len(dot_list) - 1):
                next_dots_list += self.one_line(dot_list[i], dot_list[i + 1])[1:]
            # 현재 단계를 다음 단계로
            dot_list = next_dots_list.copy()
            # 단계별 보여주기 유무에 따라 현재 단계를 그려줌
            if show_process:
                self.draw_dots(dot_list)
        # 모든 단계가 진행 후 최종 결과를 그림
        self.draw_dots(dot_list)
    # 점 리스트를 넘기면 그 리스트에 있는 점들을 차례로 그리는 함수
    def draw_dots(self, dots: List[Tuple[float, float]]):
    # 현재 위키에서 리스트 0 번 위치로 이동하는 자국을 없애기 위함
        self.t.penup()
        (init_x, init_y) = dots[0]
        self.t.goto(init_x, init_y)
        # 그리기 시작
        self.t.pendown()
        # 각 점 위치로 이동
        for (x, y) in dots:
            self.t.goto(x, y)
        # 그리기 끝
        self.t.penup()
    # 시작점과 끝점에 따라 코흐 곡선의 단계를 1 회 진행시켰을 때 좌표를 반환하는 함수
    @staticmethod
    def one_line(pos1: Tuple[float, float], pos2: Tuple[float, float]) -> List[Tuple[float, float]]:
        (x1, y1) = pos1
        (x2, y2) = pos2
        # 첫번째 좌표
        positions: List[Tuple[float, float]] = [(x1, y1)]
        # pos1 과 pos2 의 1:2 내분점
        positions.append((
        (2 * x1 + x2) / 3,
        (2 * y1 + y2) / 3
        ))
        # pos1 과 pos2 의 거리
        length: float = math.sqrt(math.pow(x1 - x2, 2) +
        math.pow(y1 - y2, 2))
        # 선분의 각도
        degree: float = math.degrees(math.acos((x2 - x1) / length))
        if y1 > y2:
            degree *= -1
        # 코흐의 곡선 위로 튀어나온 부분의 좌표(처음 지점에서 30 도 각도로 둘 사이의 거리 나누기 루트 3 만큼 움직인 위치)
        positions.append((math.cos(math.radians(30 + degree)) / math.sqrt(3) * length + x1,
        math.sin(math.radians(30 + degree)) / math.sqrt(3) * length + y1))
        # pos1 과 pos2 의 2:1 내분점
        positions.append(((x1 + 2 * x2) / 3,
        (y1 + 2 * y2) / 3))
        # 마지막 지점
        positions.append((x2, y2))
        # 결과 리턴
        return positions
    # 메인 실행부분
if __name__ == "__main__":
# 인스턴스 생성
    main = Main()
# 코흐의 곡선
    main.execute(FRACTAL_LEVEL, (-300, 200), (300, 200), SHOW_PROCESS)
    turtle.mainloop()
