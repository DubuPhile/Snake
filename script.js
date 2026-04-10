const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const WIDTH = 500;
const HEIGHT = 500;
const block = 20;

let snake, dx, dy, food, score, gameOver;

function resetGame() {
  snake = [
    { x: 300, y: 300 },
    { x: 280, y: 300 },
    { x: 260, y: 300 },
  ];
  dx = block;
  dy = 0;
  food = randomFood();
  score = 0;
  gameOver = false;
}

function randomFood() {
  return {
    x: Math.floor(Math.random() * (WIDTH / block)) * block,
    y: Math.floor(Math.random() * (HEIGHT / block)) * block,
  };
}

function drawRect(x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x, y, block, block);
}

function drawText(text, x, y, size = 20, color = "white") {
  ctx.fillStyle = color;
  ctx.font = `${size}px Arial`;
  ctx.fillText(text, x, y);
}

function update() {
  if (gameOver) return;

  const head = {
    x: snake[0].x + dx,
    y: snake[0].y + dy,
  };

  snake.unshift(head);

  // Eat food
  if (head.x === food.x && head.y === food.y) {
    food = randomFood();
    score++;
  } else {
    snake.pop();
  }

  // Collision
  if (
    head.x < 0 ||
    head.x >= WIDTH ||
    head.y < 0 ||
    head.y >= HEIGHT ||
    snake.slice(1).some((s) => s.x === head.x && s.y === head.y)
  ) {
    gameOver = true;
  }
}

function draw() {
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  if (gameOver) {
    drawText("GAME OVER", 140, 200, 40, "red");
    drawText(`Score: ${score}`, 215, 250);
    drawText("Press R to Try Again", 165, 300);
    drawText("Press Q to Quit", 165, 340);
    return;
  }

  // Snake
  snake.forEach((s) => drawRect(s.x, s.y, "green"));

  // Food
  drawRect(food.x, food.y, "red");

  // Score
  drawText(`Score: ${score}`, 10, 20);
}

function loop() {
  update();
  draw();
}

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowUp" && dy === 0) {
    dx = 0;
    dy = -block;
  } else if (e.key === "ArrowDown" && dy === 0) {
    dx = 0;
    dy = block;
  } else if (e.key === "ArrowLeft" && dx === 0) {
    dx = -block;
    dy = 0;
  } else if (e.key === "ArrowRight" && dx === 0) {
    dx = block;
    dy = 0;
  }

  if (gameOver) {
    if (e.key.toLowerCase() === "r") {
      resetGame();
    } else if (e.key.toLowerCase() === "q") {
      location.reload();
    }
  }
});

resetGame();
setInterval(loop, 100);
