"""
파이썬 벽돌깨기 (Breakout) 게임
- pygame 라이브러리 필요
- 조작: 좌우 방향키 또는 A/D 키로 패들 이동, 스페이스바로 시작/재시작
"""

import sys
import random
import pygame

# ----------------------------
# 기본 설정
# ----------------------------
WIDTH, HEIGHT = 800, 600
FPS = 60

# 색상
BLACK = (15, 15, 25)
WHITE = (240, 240, 240)
PADDLE_COLOR = (80, 200, 255)
BALL_COLOR = (255, 220, 80)
TEXT_COLOR = (255, 255, 255)
BRICK_COLORS = [
    (231, 76, 60),
    (230, 126, 34),
    (241, 196, 15),
    (46, 204, 113),
    (52, 152, 219),
    (155, 89, 182),
]

# 패들 설정
PADDLE_WIDTH, PADDLE_HEIGHT = 110, 16
PADDLE_SPEED = 8

# 공 설정
BALL_RADIUS = 9
BALL_SPEED = 5

# 벽돌 설정
BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_WIDTH = 70
BRICK_HEIGHT = 24
BRICK_GAP = 6
BRICK_TOP_OFFSET = 60
BRICK_LEFT_OFFSET = (WIDTH - (BRICK_COLS * (BRICK_WIDTH + BRICK_GAP) - BRICK_GAP)) // 2

STARTING_LIVES = 3


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(
            (WIDTH - PADDLE_WIDTH) // 2,
            HEIGHT - 40,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
        )

    def move(self, direction):
        self.rect.x += direction * PADDLE_SPEED
        self.rect.x = max(0, min(WIDTH - PADDLE_WIDTH, self.rect.x))

    def draw(self, surface):
        pygame.draw.rect(surface, PADDLE_COLOR, self.rect, border_radius=8)


class Ball:
    def __init__(self, paddle):
        self.paddle = paddle
        self.reset()

    def reset(self):
        self.x = float(self.paddle.rect.centerx)
        self.y = float(self.paddle.rect.top - BALL_RADIUS - 1)
        angle_choices = [-1, 1]
        self.vx = BALL_SPEED * random.choice(angle_choices) * 0.7
        self.vy = -BALL_SPEED
        self.launched = False

    def update(self):
        if not self.launched:
            self.x = self.paddle.rect.centerx
            self.y = self.paddle.rect.top - BALL_RADIUS - 1
            return

        self.x += self.vx
        self.y += self.vy

        # 좌우 벽 충돌
        if self.x - BALL_RADIUS <= 0:
            self.x = BALL_RADIUS
            self.vx *= -1
        elif self.x + BALL_RADIUS >= WIDTH:
            self.x = WIDTH - BALL_RADIUS
            self.vx *= -1

        # 위쪽 벽 충돌
        if self.y - BALL_RADIUS <= 0:
            self.y = BALL_RADIUS
            self.vy *= -1

    def launch(self):
        self.launched = True

    def get_rect(self):
        return pygame.Rect(
            int(self.x - BALL_RADIUS),
            int(self.y - BALL_RADIUS),
            BALL_RADIUS * 2,
            BALL_RADIUS * 2,
        )

    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)


class Brick:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = color
        self.alive = True

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=4)
            pygame.draw.rect(surface, BLACK, self.rect, width=2, border_radius=4)


def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        color = BRICK_COLORS[row % len(BRICK_COLORS)]
        for col in range(BRICK_COLS):
            x = BRICK_LEFT_OFFSET + col * (BRICK_WIDTH + BRICK_GAP)
            y = BRICK_TOP_OFFSET + row * (BRICK_HEIGHT + BRICK_GAP)
            bricks.append(Brick(x, y, color))
    return bricks


def reflect_ball_off_paddle(ball, paddle):
    # 패들의 어디에 맞았는지에 따라 반사각을 다르게 준다
    offset = (ball.x - paddle.rect.centerx) / (PADDLE_WIDTH / 2)
    offset = max(-1, min(1, offset))
    speed = (ball.vx ** 2 + ball.vy ** 2) ** 0.5
    max_angle = 60  # degrees
    angle = offset * max_angle
    import math
    rad = math.radians(angle)
    ball.vx = speed * math.sin(rad)
    ball.vy = -abs(speed * math.cos(rad))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("벽돌깨기 - Breakout")
    clock = pygame.time.Clock()

    font_big = pygame.font.SysFont("malgungothic", 48)
    font_small = pygame.font.SysFont("malgungothic", 24)
    font_tiny = pygame.font.SysFont("malgungothic", 20)

    paddle = Paddle()
    ball = Ball(paddle)
    bricks = create_bricks()

    score = 0
    lives = STARTING_LIVES
    game_over = False
    game_won = False

    def restart_game():
        nonlocal paddle, ball, bricks, score, lives, game_over, game_won
        paddle = Paddle()
        ball = Ball(paddle)
        bricks = create_bricks()
        score = 0
        lives = STARTING_LIVES
        game_over = False
        game_won = False

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over or game_won:
                        restart_game()
                    elif not ball.launched:
                        ball.launch()
                elif event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if not game_over and not game_won:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                paddle.move(-1)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                paddle.move(1)

            ball.update()

            # 패들 충돌
            ball_rect = ball.get_rect()
            if ball.vy > 0 and ball_rect.colliderect(paddle.rect):
                reflect_ball_off_paddle(ball, paddle)
                ball.y = paddle.rect.top - BALL_RADIUS - 1

            # 벽돌 충돌
            ball_rect = ball.get_rect()
            for brick in bricks:
                if brick.alive and ball_rect.colliderect(brick.rect):
                    brick.alive = False
                    score += 10

                    # 충돌 방향에 따라 반사
                    overlap_left = ball_rect.right - brick.rect.left
                    overlap_right = brick.rect.right - ball_rect.left
                    overlap_top = ball_rect.bottom - brick.rect.top
                    overlap_bottom = brick.rect.bottom - ball_rect.top
                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

                    if min_overlap in (overlap_left, overlap_right):
                        ball.vx *= -1
                    else:
                        ball.vy *= -1
                    break

            # 공을 놓쳤을 때
            if ball.y - BALL_RADIUS > HEIGHT:
                lives -= 1
                if lives <= 0:
                    game_over = True
                else:
                    ball.reset()

            # 모든 벽돌 파괴 시 승리
            if all(not b.alive for b in bricks):
                game_won = True

        # ----------------------------
        # 그리기
        # ----------------------------
        screen.fill(BLACK)

        for brick in bricks:
            brick.draw(screen)

        paddle.draw(screen)
        ball.draw(screen)

        # 점수와 목숨 표시
        score_text = font_small.render(f"점수: {score}", True, TEXT_COLOR)
        lives_text = font_small.render(f"목숨: {lives}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

        if not ball.launched and not game_over and not game_won:
            hint = font_tiny.render("스페이스바를 눌러 공을 발사하세요", True, TEXT_COLOR)
            screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2 + 60))

        if game_over:
            msg = font_big.render("GAME OVER", True, (255, 90, 90))
            sub = font_small.render("스페이스바를 눌러 재시작", True, TEXT_COLOR)
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))
            screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 20))

        if game_won:
            msg = font_big.render("YOU WIN!", True, (100, 255, 150))
            sub = font_small.render("스페이스바를 눌러 다시 플레이", True, TEXT_COLOR)
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 40))
            screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2 + 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    