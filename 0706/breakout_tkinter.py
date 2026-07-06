"""
파이썬 벽돌깨기 (Breakout) - tkinter 버전
외부 라이브러리 설치가 필요 없습니다 (tkinter는 파이썬 표준 라이브러리).

조작법:
- 왼쪽/오른쪽 방향키: 패들 이동
- 스페이스바: 공 발사 / 게임오버·승리 후 재시작
"""

import tkinter as tk
import random

WIDTH, HEIGHT = 800, 600

PADDLE_WIDTH, PADDLE_HEIGHT = 110, 16
PADDLE_SPEED = 25

BALL_SIZE = 16
BALL_SPEED = 5

BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_WIDTH = 70
BRICK_HEIGHT = 24
BRICK_GAP = 6
BRICK_TOP_OFFSET = 60
BRICK_LEFT_OFFSET = (WIDTH - (BRICK_COLS * (BRICK_WIDTH + BRICK_GAP) - BRICK_GAP)) // 2

BRICK_COLORS = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6"]

STARTING_LIVES = 3
FPS_MS = 16  # 약 60fps


class Breakout:
    def __init__(self, root):
        self.root = root
        self.root.title("벽돌깨기 - Breakout")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#0f0f19", highlightthickness=0)
        self.canvas.pack()

        self.root.bind("<Left>", lambda e: self.set_direction(-1))
        self.root.bind("<Right>", lambda e: self.set_direction(1))
        self.root.bind("<KeyRelease-Left>", lambda e: self.clear_direction(-1))
        self.root.bind("<KeyRelease-Right>", lambda e: self.clear_direction(1))
        self.root.bind("<a>", lambda e: self.set_direction(-1))
        self.root.bind("<d>", lambda e: self.set_direction(1))
        self.root.bind("<KeyRelease-a>", lambda e: self.clear_direction(-1))
        self.root.bind("<KeyRelease-d>", lambda e: self.clear_direction(1))
        self.root.bind("<space>", self.on_space)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.direction = 0
        self.new_game()
        self.loop()

    # ------------------------------------------------------------
    def new_game(self):
        self.canvas.delete("all")

        self.score = 0
        self.lives = STARTING_LIVES
        self.game_over = False
        self.game_won = False
        self.launched = False

        # 패들
        px = (WIDTH - PADDLE_WIDTH) // 2
        py = HEIGHT - 40
        self.paddle = self.canvas.create_rectangle(
            px, py, px + PADDLE_WIDTH, py + PADDLE_HEIGHT,
            fill="#50c8ff", outline=""
        )

        # 공
        self.ball_vx = BALL_SPEED * random.choice([-1, 1]) * 0.7
        self.ball_vy = -BALL_SPEED
        self.ball = self.canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill="#ffdc50", outline="")
        self.reset_ball_position()

        # 벽돌
        self.bricks = []
        for row in range(BRICK_ROWS):
            color = BRICK_COLORS[row % len(BRICK_COLORS)]
            for col in range(BRICK_COLS):
                x = BRICK_LEFT_OFFSET + col * (BRICK_WIDTH + BRICK_GAP)
                y = BRICK_TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_GAP)
                brick_id = self.canvas.create_rectangle(
                    x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT,
                    fill=color, outline="#0f0f19", width=2
                )
                self.bricks.append(brick_id)

        # 텍스트
        self.score_text = self.canvas.create_text(
            60, 20, text=f"점수: {self.score}", fill="white", font=("맑은 고딕", 14)
        )
        self.lives_text = self.canvas.create_text(
            WIDTH - 60, 20, text=f"목숨: {self.lives}", fill="white", font=("맑은 고딕", 14)
        )
        self.hint_text = self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 + 60,
            text="스페이스바를 눌러 공을 발사하세요",
            fill="white", font=("맑은 고딕", 12)
        )
        self.message_text = self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 - 20, text="", fill="white", font=("맑은 고딕", 32, "bold")
        )
        self.submessage_text = self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2 + 20, text="", fill="white", font=("맑은 고딕", 14)
        )

    def reset_ball_position(self):
        px1, py1, px2, py2 = self.canvas.coords(self.paddle)
        cx = (px1 + px2) / 2
        bx = cx - BALL_SIZE / 2
        by = py1 - BALL_SIZE - 1
        self.canvas.coords(self.ball, bx, by, bx + BALL_SIZE, by + BALL_SIZE)
        self.launched = False
        self.canvas.itemconfig(self.hint_text, text="스페이스바를 눌러 공을 발사하세요")

    # ------------------------------------------------------------
    def set_direction(self, d):
        self.direction = d

    def clear_direction(self, d):
        if self.direction == d:
            self.direction = 0

    def on_space(self, event=None):
        if self.game_over or self.game_won:
            self.new_game()
        elif not self.launched:
            self.launched = True
            self.canvas.itemconfig(self.hint_text, text="")

    # ------------------------------------------------------------
    def move_paddle(self):
        if self.game_over or self.game_won:
            return
        x1, y1, x2, y2 = self.canvas.coords(self.paddle)
        dx = self.direction * PADDLE_SPEED
        new_x1 = x1 + dx
        new_x2 = x2 + dx
        if new_x1 < 0:
            dx = -x1
        elif new_x2 > WIDTH:
            dx = WIDTH - x2
        self.canvas.move(self.paddle, dx, 0)

    def move_ball(self):
        if not self.launched or self.game_over or self.game_won:
            if not self.launched:
                self.reset_ball_position()
            return

        self.canvas.move(self.ball, self.ball_vx, self.ball_vy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)

        # 좌우 벽
        if bx1 <= 0:
            self.canvas.move(self.ball, -bx1, 0)
            self.ball_vx *= -1
        elif bx2 >= WIDTH:
            self.canvas.move(self.ball, WIDTH - bx2, 0)
            self.ball_vx *= -1

        # 위쪽 벽
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        if by1 <= 0:
            self.canvas.move(self.ball, 0, -by1)
            self.ball_vy *= -1

        # 패들 충돌
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        px1, py1, px2, py2 = self.canvas.coords(self.paddle)
        if self.ball_vy > 0 and by2 >= py1 and by1 <= py2 and bx2 >= px1 and bx1 <= px2:
            self.reflect_off_paddle(px1, px2)

        # 벽돌 충돌
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        hit = self.canvas.find_overlapping(bx1, by1, bx2, by2)
        for item in hit:
            if item in self.bricks:
                self.bricks.remove(item)
                self.canvas.delete(item)
                self.score += 10
                self.canvas.itemconfig(self.score_text, text=f"점수: {self.score}")

                self.ball_vy *= -1
                break

        # 바닥으로 떨어짐
        bx1, by1, bx2, by2 = self.canvas.coords(self.ball)
        if by1 > HEIGHT:
            self.lives -= 1
            self.canvas.itemconfig(self.lives_text, text=f"목숨: {self.lives}")
            if self.lives <= 0:
                self.trigger_game_over()
            else:
                self.reset_ball_position()

        if not self.bricks and not self.game_won:
            self.trigger_win()

    def reflect_off_paddle(self, px1, px2):
        paddle_center = (px1 + px2) / 2
        bx1, by1_, bx2, by2 = self.canvas.coords(self.ball)
        ball_center = (bx1 + bx2) / 2
        offset = (ball_center - paddle_center) / ((px2 - px1) / 2)
        offset = max(-1, min(1, offset))

        import math
        speed = (self.ball_vx ** 2 + self.ball_vy ** 2) ** 0.5
        max_angle = 60
        angle = math.radians(offset * max_angle)
        self.ball_vx = speed * math.sin(angle)
        self.ball_vy = -abs(speed * math.cos(angle))

        # 패들 위로 위치 보정 (파묻힘 방지)
        py_top = self.canvas.coords(self.paddle)[1]
        bx1, _, bx2, _ = self.canvas.coords(self.ball)
        self.canvas.coords(self.ball, bx1, py_top - BALL_SIZE - 1, bx2, py_top - 1)

    def trigger_game_over(self):
        self.game_over = True
        self.canvas.itemconfig(self.message_text, text="GAME OVER", fill="#ff5a5a")
        self.canvas.itemconfig(self.submessage_text, text="스페이스바를 눌러 재시작")

    def trigger_win(self):
        self.game_won = True
        self.canvas.itemconfig(self.message_text, text="YOU WIN!", fill="#64ff96")
        self.canvas.itemconfig(self.submessage_text, text="스페이스바를 눌러 다시 플레이")

    # ------------------------------------------------------------
    def loop(self):
        self.move_paddle()
        self.move_ball()
        self.root.after(FPS_MS, self.loop)


def main():
    root = tk.Tk()
    root.resizable(False, False)
    app = Breakout(root)
    root.mainloop()


if __name__ == "__main__":
    main()
