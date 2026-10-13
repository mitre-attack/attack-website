const AGAME_DEFAULT_GAME_MODE = "Medium";

const AGAME_BOARD_MAX_ROWS = 15;

const AGAME_PADDLE_WIDTH = 180;
const AGAME_PADDLE_HEIGHT = 20;
const AGAME_PADDLE_VELOCITY_X = 20;

const AGAME_BALL_WIDTH = 10;
const AGAME_BALL_HEIGHT = 10;
const AGAME_BALL_VELOCITY_X = 25;
const AGAME_BALL_VELOCITY_Y = 10;

const AGAME_BLOCK_X_OFFSET = 10;
const AGAME_BLOCK_Y_OFFSET = 45;
const AGAME_MIN_BLOCK_HEIGHT = 35;

const AGAME_SCORE_INCREMENT = 100;
const AGAME_SCORE_BONUS = 10000;

class Board {
  constructor() {
    this.padding = 20;
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.context = null;
  }

  setupBoard() {
    let board = document.getElementById("board");
    board.style.left = this.padding + "px";
    board.style.top = this.padding + "px";
    board.style.backgroundColor = game.theme.currentPreset.backgroundColor;
    board.height = this.height;
    board.width = this.width;
    board.style.borderTop = "5px solid " + game.theme.currentPreset.borderColor;
    board.style.borderLeft = "5px solid " + game.theme.currentPreset.borderColor;
    board.style.borderRight = "5px solid " + game.theme.currentPreset.borderColor;
    this.context = board.getContext("2d");
    this.resizeBoard();
  }

  resizeBoard() {
    this.width = window.innerWidth - 2 * this.padding;
    this.height = window.innerHeight - 2 * this.padding;
    let board = document.getElementById("board");
    board.height = this.height;
    board.width = this.width;
  }
}

class Paddle {
  constructor(width, height, velocityX) {
    this.width = width;
    this.height = height;
    this.velocityX = velocityX;
    this.x = null;
    this.y = null;
  }

  get left() {
    return this.x;
  }
  get right() {
    return this.x + this.width;
  }
  get top() {
    return this.y;
  }
  get bottom() {
    return this.y + this.height;
  }

  generatePaddleData(boardWidth, boardHeight) {
    this.x = boardWidth / 2 - this.width / 2;
    this.y = boardHeight - this.height - 5;
  }
}

class Ball {
  constructor(width, height, velocityX, velocityY) {
    this.width = width;
    this.height = height;
    this.velocityX = velocityX;
    this.velocityY = velocityY;
    this.x = null;
    this.y = null;
  }

  get left() {
    return this.x;
  }
  get right() {
    return this.x + this.width;
  }
  get top() {
    return this.y;
  }
  get bottom() {
    return this.y + this.height;
  }

  generateInitialBall(boardWidth, boardHeight) {
    this.x = boardWidth * 0.5;
    this.y = boardHeight * 0.7;
    this.velocityX = Math.random() < 0.5 ? -this.velocityX : this.velocityX;
  }
}

class Block {
  constructor(width, height, x, y, wordsArray, fontSize) {
    this.width = width;
    this.height = height;
    this.x = x;
    this.y = y;
    this.wordsArray = wordsArray;
    this.fontSize = fontSize;
    this.break = false;
  }
  get left() {
    return this.x;
  }
  get right() {
    return this.x + this.width;
  }
  get top() {
    return this.y;
  }
  get bottom() {
    return this.y + this.height;
  }
}

class GameState {
  constructor() {
    this.gameHistory = [];
    this.initialState();
    this.isSmallScreen = window.innerWidth <= 480;
  }
  initialState() {
    this.score = 0;
    this.lives = 3;
    this.gameOver = false;
    this.gamePaused = true;
    this.gameStarted = false;
    this.levelCompleted = false;
    this.blockCount = 0;
    this.keyState = {};
    this.minBallVelocityX = AGAME_BALL_VELOCITY_X * -1;
    this.maxBallVelocityX = AGAME_BALL_VELOCITY_X;
    this.difficulty = AGAME_DEFAULT_GAME_MODE;
  }
}

class GameDifficulty {
  constructor(name, velocity) {
    this.name = name;
    this.velocity = velocity;
  }
}

class Level {
  constructor() {
    this.currentLevel = 1;
  }
  nextLevel() {
    this.currentLevel++;
    game.state.score += AGAME_SCORE_BONUS;
    game.attackMatrix = createAttackMatrix();
    game.createBlocks();
    game.theme.changeTheme(this.currentLevel);
    game.theme.applyTheme();
  }
  displayLevel = () => {
    if (!game.state.isSmallScreen) {
      game.board.context.fillStyle = game.theme.textColor;
      game.board.context.font = "20px sans-serif";
      game.board.context.fillText("Level: " + this.currentLevel, game.board.width - 200, 25);
    }
  };
}

class Theme {
  constructor() {
    this.presets = [
      {
        title: "Default",
        borderColor: "red",
        backgroundColor: "#303030",
        textColor: "white",
        blockColor: "white",
        blockTextColor: "black",
        // paddleColor: "lightgreen",
        paddleColor: "red",
        ballColor: "white",
        messageBoxBgColor: "red",
        messageBoxTextColor: "white",
        hudActiveTextColor: "white",
        hudPausedTextColor: "red",
      },
      {
        title: "Ocean",
        borderColor: "darkblue",
        backgroundColor: "#000080",
        textColor: "white",
        blockColor: "lightblue",
        blockTextColor: "darkblue",
        paddleColor: "white",
        ballColor: "white",
        messageBoxBgColor: "lightblue",
        messageBoxTextColor: "darkblue",
        hudActiveTextColor: "white",
        hudPausedTextColor: "lightblue",
      },
      {
        title: "Forest",
        borderColor: "darkgreen",
        backgroundColor: "#006400",
        textColor: "white",
        blockColor: "lightgreen",
        blockTextColor: "darkgreen",
        paddleColor: "white",
        ballColor: "white",
        messageBoxBgColor: "lightgreen",
        messageBoxTextColor: "darkgreen",
        hudActiveTextColor: "white",
        hudPausedTextColor: "lightgreen",
      },
      {
        title: "Desert",
        borderColor: "darkred",
        backgroundColor: "#8B4513",
        textColor: "white",
        blockColor: "peachpuff",
        blockTextColor: "darkred",
        paddleColor: "white",
        ballColor: "white",
        messageBoxBgColor: "peachpuff",
        messageBoxTextColor: "darkred",
        hudActiveTextColor: "white",
        hudPausedTextColor: "peachpuff",
      },
      {
        title: "Mint",
        borderColor: "darkgreen",
        backgroundColor: "#98FB98",
        textColor: "darkgreen",
        blockColor: "white",
        blockTextColor: "darkgreen",
        paddleColor: "darkgreen",
        ballColor: "darkgreen",
        messageBoxBgColor: "white",
        messageBoxTextColor: "darkgreen",
        hudActiveTextColor: "darkgreen",
        hudPausedTextColor: "white",
      },
      {
        title: "Lavender",
        borderColor: "darkviolet",
        backgroundColor: "#E6E6FA",
        textColor: "darkviolet",
        blockColor: "white",
        blockTextColor: "darkviolet",
        paddleColor: "darkviolet",
        ballColor: "darkviolet",
        messageBoxBgColor: "white",
        messageBoxTextColor: "darkviolet",
        hudActiveTextColor: "darkviolet",
        hudPausedTextColor: "white",
      },
      {
        title: "Rose",
        borderColor: "darkred",
        backgroundColor: "#FFC0CB",
        textColor: "darkred",
        blockColor: "white",
        blockTextColor: "darkred",
        paddleColor: "darkred",
        ballColor: "darkred",
        messageBoxBgColor: "white",
        messageBoxTextColor: "darkred",
        hudActiveTextColor: "darkred",
        hudPausedTextColor: "white",
      },
      {
        title: "Sky",
        borderColor: "darkblue",
        backgroundColor: "#87CEEB",
        textColor: "darkblue",
        blockColor: "white",
        blockTextColor: "darkblue",
        paddleColor: "darkblue",
        ballColor: "darkblue",
        messageBoxBgColor: "white",
        messageBoxTextColor: "darkblue",
        hudActiveTextColor: "darkblue",
        hudPausedTextColor: "white",
      },
    ];
    this.currentPreset = this.presets[0];
    console.log(this.currentPreset);
  }
  changeTheme(level) {
    this.currentPreset = this.presets[(level - 1) % this.presets.length];
    console.log("Changed theme to: " + this.currentPreset.title);
  }
  applyTheme() {
    game.board.context.canvas.style.borderColor = this.currentPreset.borderColor;
    game.board.context.canvas.style.backgroundColor = this.currentPreset.backgroundColor;
    game.paddle.color = this.currentPreset.paddleColor;
    game.ball.color = this.currentPreset.ballColor;
    game.blocks.forEach((block) => {
      block.color = this.currentPreset.blockColor;
      block.textColor = this.currentPreset.blockTextColor;
    });
  }
}

class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.size = Math.random() * 5 + 1;
    this.speedX = Math.random() * 3 - 1.5;
    this.speedY = Math.random() * 3 - 1.5;
    this.color = color;
  }

  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    if (this.size > 0.1) this.size -= 0.1;
  }

  draw() {
    game.board.context.fillStyle = this.color;
    game.board.context.strokeStyle = "red";
    game.board.context.lineWidth = 2;
    game.board.context.beginPath();
    game.board.context.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    game.board.context.closePath();
    game.board.context.fill();
    game.board.context.stroke();
  }
}

class ParticleSystem {
  constructor() {
    this.particles = [];
    this.fireworks = [];
  }
  createExplosion(x, y, count, color) {
    for (let i = 0; i < count; i++) {
      this.particles.push(new Particle(x, y, color));
    }
  }

  updateParticles() {
    for (let i = 0; i < this.particles.length; i++) {
      this.particles[i].update();
      if (this.particles[i].size <= 0.1) {
        this.particles.splice(i, 1);
        i--;
      }
    }
  }

  drawParticles() {
    for (let i = 0; i < this.particles.length; i++) {
      this.particles[i].draw();
    }
  }

  updateFireworks() {
    for (let i = 0; i < this.fireworks.length; i++) {
      this.fireworks[i].update();
      if (this.fireworks[i].exploded) {
        this.createExplosion(this.fireworks[i].x, this.fireworks[i].y, 100, this.fireworks[i].color);
        this.fireworks.splice(i, 1);
        i--;
      }
    }
  }

  drawFireworks() {
    for (let i = 0; i < this.fireworks.length; i++) {
      this.fireworks[i].draw();
    }
  }
}

class Firework {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.velocityX = (Math.random() - 0.5) * 6;
    this.velocityY = Math.random() * -3 - 10;
    this.color = this.getRandomColor();
    this.exploded = false;
  }

  getRandomColor() {
    const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];
    return colors[Math.floor(Math.random() * colors.length)];
  }

  update() {
    this.x += this.velocityX;
    this.y += this.velocityY;
    this.velocityY += 0.1; // Gravity
    if (this.velocityY >= 0) {
      this.explode();
    }
  }

  explode() {
    this.exploded = true;
    for (let i = 0; i < 50; i++) {
      game.particleSystem.particles.push(new Particle(this.x, this.y, this.color));
    }
  }

  draw() {
    game.board.context.fillStyle = this.color;
    game.board.context.beginPath();
    game.board.context.arc(this.x, this.y, 2, 0, Math.PI * 2);
    game.board.context.fill();
  }
}

class Game {
  constructor() {
    this.board = new Board();
    this.paddle = new Paddle(AGAME_PADDLE_WIDTH, AGAME_PADDLE_HEIGHT, AGAME_PADDLE_VELOCITY_X);
    this.ball = new Ball(AGAME_BALL_WIDTH, AGAME_BALL_HEIGHT, AGAME_BALL_VELOCITY_X, AGAME_BALL_VELOCITY_Y);
    this.level = new Level();
    this.theme = new Theme();
    this.state = new GameState();
    this.animationId = null;
    this.blocks = [];
    this.attackMatrix = null;
    this.particleSystem = new ParticleSystem();
    this.EASY_DIFFICULTY = new GameDifficulty("Easy", 4.5);
    this.MEDIUM_DIFFICULTY = new GameDifficulty("Medium", 7.5);
    this.HARD_DIFFICULTY = new GameDifficulty("Hard", 10.5);
  }

  // Setup methods
  setup = () => {
    try {
      this.setupCanvas();
      this.setupGame();
      this.setupEventListeners();
    } catch (error) {
      console.error("Error during setup: ", error);
    }
  };

  setupCanvas = () => {
    try {
      this.board.setupBoard();
      if (this.state.isSmallScreen) {
        this.paddle.width = this.board.width * 0.2;
      }
      this.paddle.generatePaddleData(this.board.width, this.board.height);
      this.ball.generateInitialBall(this.board.width, this.board.height);
      this.state.gamePaused = true;
    } catch (error) {
      console.error("Error setting up the canvas: ", error);
    }
  };

  setupGame = () => {
    try {
      this.theme.applyTheme();
      this.attackMatrix = createAttackMatrix();
      this.blockRows = this.attackMatrix.length;
      this.blockColumns = this.attackMatrix[0].length;
      this.createBlocks();
      this.displayStartScreen();
    } catch (error) {
      console.error("Error setting up the game: ", error);
    }
  };

  setupEventListeners = () => {
    try {
      window.addEventListener("resize", this.handleResize);
      this.setupKeyboardListeners();
      this.setupMouseListeners();
      this.setupTouchListeners();
    } catch (error) {
      console.error("Error setting up event listeners: ", error);
    }
  };

  setupKeyboardListeners = () => {
    document.addEventListener("keydown", (e) => {
      this.state.keyState[e.code] = true;
      if (e.code === "ArrowLeft") {
        this.handleArrowLeftKey();
      } else if (e.code === "ArrowRight") {
        this.handleArrowRightKey();
      } else if (e.code === "Space") {
        this.handleSpaceKey();
      }
    });

    document.addEventListener("keyup", (e) => {
      this.state.keyState[e.code] = false;
    });
  };

  setupMouseListeners = () => {
    this.board.context.canvas.addEventListener("mousemove", (e) => {
      if (!this.state.gamePaused) {
        const rect = this.board.context.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        let newPaddleX = x - this.paddle.width / 2;
        if (newPaddleX < 0) {
          newPaddleX = 0;
        } else if (newPaddleX > this.board.width - this.paddle.width) {
          newPaddleX = this.board.width - this.paddle.width;
        }
        this.paddle.x = newPaddleX;
      }
    });

    this.board.context.canvas.addEventListener("click", (e) => {
      if (!this.state.gameStarted) {
        const rect = this.board.context.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        this.buttons.forEach((button) => {
          if (x > button.x && x < button.x + button.width && y > button.y && y < button.y + button.height) {
            this.setDifficulty(button.difficulty);
            this.startGame();
          }
        });
      } else if (this.state.gameOver) {
        const rect = this.board.context.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        // Calculate the button dimensions and positions
        const buttonWidth = 200;
        const buttonHeight = 50;
        const padding = 10;
        const messageHeight = 64; // Assuming the message font size is 64px
        const messageY = (this.board.height - messageHeight) / 2;
        const buttonsY = messageY + messageHeight + padding;
        const twitterButtonX = (this.board.width - buttonWidth) / 2;
        const twitterButtonY = buttonsY;
        const blueskyButtonX = (this.board.width - buttonWidth) / 2;
        const blueskyButtonY = twitterButtonY + buttonHeight + padding;
        const startOverButtonX = (this.board.width - buttonWidth) / 2;
        const startOverButtonY = blueskyButtonY + buttonHeight + padding;
        const percentageComplete = this.getPercentageComplete();
        // Check if "Share on Twitter" button was clicked
        if (x > twitterButtonX && x < twitterButtonX + buttonWidth && y > twitterButtonY && y < twitterButtonY + buttonHeight) {
          window.open(this.generateTwitterShareLink(percentageComplete, false), "_blank");
        }
        // Check if "Share on Bluesky" button was clicked
        if (x > blueskyButtonX && x < blueskyButtonX + buttonWidth && y > blueskyButtonY && y < blueskyButtonY + buttonHeight) {
          window.open(this.generateBlueskyShareLink(percentageComplete, false), "_blank");
        }
        // Check if "Start Over" button was clicked
        if (x > startOverButtonX && x < startOverButtonX + buttonWidth && y > startOverButtonY && y < startOverButtonY + buttonHeight) {
          this.resetGame();
        }
      } else if (this.state.levelCompleted) {
        const rect = this.board.context.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        // Calculate the button dimensions and positions
        const buttonWidth = 200;
        const buttonHeight = 50;
        const padding = 10;
        const messageHeight = 64; // Assuming the message font size is 64px
        const messageY = (this.board.height - messageHeight) / 2;
        const buttonsY = messageY + messageHeight + padding;
        const twitterButtonX = (this.board.width - buttonWidth) / 2;
        const twitterButtonY = buttonsY;
        const blueskyButtonX = (this.board.width - buttonWidth) / 2;
        const blueskyButtonY = twitterButtonY + buttonHeight + padding;
        const nextLevelButtonX = (this.board.width - buttonWidth) / 2;
        const nextLevelButtonY = blueskyButtonY + buttonHeight + padding;
        // Check if "Share on Twitter" button was clicked
        if (x > twitterButtonX && x < twitterButtonX + buttonWidth && y > twitterButtonY && y < twitterButtonY + buttonHeight) {
          window.open(this.generateTwitterShareLink(100, true), "_blank");
        }
        // Check if "Share on Bluesky" button was clicked
        if (x > blueskyButtonX && x < blueskyButtonX + buttonWidth && y > blueskyButtonY && y < blueskyButtonY + buttonHeight) {
          window.open(this.generateBlueskyShareLink(100, true), "_blank");
        }
        // Check if "Next Level" button was clicked
        if (x > nextLevelButtonX && x < nextLevelButtonX + buttonWidth && y > nextLevelButtonY && y < nextLevelButtonY + buttonHeight) {
          this.state.levelCompleted = false;
          this.level.nextLevel();
          this.state.gamePaused = false;
          cancelAnimationFrame(this.animationId);
          this.animationId = requestAnimationFrame(this.gameLoop);
        }
        // Prevent the click event from advancing the level
        return;
      } else {
        if (this.state.gamePaused) {
          this.state.gamePaused = false;
          cancelAnimationFrame(this.animationId);
          this.animationId = requestAnimationFrame(this.gameLoop);
        } else if (this.state.gameOver) {
          this.resetGame();
        }
      }
    });

    this.board.context.canvas.addEventListener("click", this.handleThemeChangeClick);
  };

  setupTouchListeners = () => {
    this.board.context.canvas.addEventListener(
      "touchmove",
      (e) => {
        if (!this.state.gamePaused) {
          const rect = this.board.context.canvas.getBoundingClientRect();
          const x = e.touches[0].clientX - rect.left;
          let newPaddleX = x - this.paddle.width / 2;
          if (newPaddleX < 0) {
            newPaddleX = 0;
          } else if (newPaddleX > this.board.width - this.paddle.width) {
            newPaddleX = this.board.width - this.paddle.width;
          }
          this.paddle.x = newPaddleX;
        }
        e.preventDefault();
      },
      { passive: false }
    );
  };

  drawDifficultyButtons = () => {
    const buttonWidth = 100;
    const buttonHeight = 50;
    const buttonY = this.board.height - 100;
    const buttonSpacing = 20;
    this.buttons = [
      {
        difficulty: this.EASY_DIFFICULTY,
        x: this.board.width / 2 - buttonWidth * 1.5 - buttonSpacing,
        y: buttonY,
        width: buttonWidth,
        height: buttonHeight,
      },
      {
        difficulty: this.MEDIUM_DIFFICULTY,
        x: this.board.width / 2 - buttonWidth / 2,
        y: buttonY,
        width: buttonWidth,
        height: buttonHeight,
      },
      {
        difficulty: this.HARD_DIFFICULTY,
        x: this.board.width / 2 + buttonWidth / 2 + buttonSpacing,
        y: buttonY,
        width: buttonWidth,
        height: buttonHeight,
      },
    ];
    this.buttons.forEach((button) => {
      this.board.context.fillStyle = "lightgray";
      this.board.context.fillRect(button.x, button.y, button.width, button.height);
      this.board.context.fillStyle = "black";
      this.board.context.font = "20px sans-serif";
      this.board.context.textAlign = "center";
      this.board.context.textBaseline = "middle";
      this.board.context.fillText(button.difficulty.name, button.x + button.width / 2, button.y + button.height / 2);
    });
    this.board.context.textAlign = "start";
    this.board.context.textBaseline = "alphabetic";
  };

  drawLevelCompleteButtons = () => {
    if (this.state.levelCompleted) {
      const buttonWidth = 200;
      const buttonHeight = 50;
      const padding = 10;
      // Calculate the y coordinate for the buttons
      const messageHeight = 64; // Assuming the message font size is 64px
      const messageY = (this.board.height - messageHeight) / 2;
      const buttonsY = messageY + messageHeight + padding;
      // Draw "Share on Twitter" button
      const twitterButtonX = (this.board.width - buttonWidth) / 2;
      const twitterButtonY = buttonsY;
      this.board.context.fillStyle = "#1DA1F2"; // Twitter's brand color
      this.board.context.fillRect(twitterButtonX, twitterButtonY, buttonWidth, buttonHeight);
      this.board.context.fillStyle = "white";
      this.board.context.font = "20px sans-serif";
      this.board.context.textAlign = "center";
      this.board.context.textBaseline = "middle";
      this.board.context.fillText("Share on X (Twitter)", twitterButtonX + buttonWidth / 2, twitterButtonY + buttonHeight / 2);

      // Draw "Share on Bluesky" button
      const blueskyButtonX = (this.board.width - buttonWidth) / 2;
      const blueskyButtonY = twitterButtonY + buttonHeight + padding;
      this.board.context.fillStyle = "#0070FF";
      this.board.context.fillRect(blueskyButtonX, blueskyButtonY, buttonWidth, buttonHeight);
      this.board.context.fillStyle = "white";
      this.board.context.fillText("Share on Bluesky", blueskyButtonX + buttonWidth / 2, blueskyButtonY + buttonHeight / 2);

      // Draw "Next Level" button
      const nextLevelButtonX = (this.board.width - buttonWidth) / 2;
      const nextLevelButtonY = blueskyButtonY + buttonHeight + padding;
      this.board.context.fillStyle = "#4CAF50";
      this.board.context.fillRect(nextLevelButtonX, nextLevelButtonY, buttonWidth, buttonHeight);
      this.board.context.fillStyle = "white";
      this.board.context.fillText("Next Level", nextLevelButtonX + buttonWidth / 2, nextLevelButtonY + buttonHeight / 2);

      // Reset text alignment and baseline
      this.board.context.textAlign = "start";
      this.board.context.textBaseline = "alphabetic";
    }
  };

  // Game loop methods
  gameLoop = () => {
    this.update();
    this.draw();
    if (!this.state.gameOver) {
      this.animationId = requestAnimationFrame(this.gameLoop);
    }
  };

  update = () => {
    this.particleSystem.updateParticles();
    this.particleSystem.updateFireworks();
    if (!this.state.gamePaused) {
      if (this.state.keyState["ArrowLeft"]) {
        this.handleArrowLeftKey();
      }
      if (this.state.keyState["ArrowRight"]) {
        this.handleArrowRightKey();
      }
      this.handleBallCollision();
      this.checkBallBounds();
      this.checkNextLevel();
      // Update ball's position
      this.ball.x += this.ball.velocityX;
      this.ball.y += this.ball.velocityY;
    }
    if (this.state.gameOver) {
      if (this.state.keyState["Space"]) {
        this.resetGame();
      }
      this.displayGameOverMessage();
      return;
    }
  };

  draw = () => {
    this.clearCanvas();
    this.drawPaddle();
    this.drawBall();
    this.drawBlocks();
    this.displayScore();
    this.displayLives();
    this.level.displayLevel();
    this.displayDifficulty();
    this.displayPauseMessage();
    this.displayLevelCompleteMessage();
    this.displayGameOverMessage();
    this.particleSystem.drawParticles();
    this.particleSystem.drawFireworks();
  };

  startGame = () => {
    this.state.gameStarted = true;
    this.state.gamePaused = false;
    this.animationId = requestAnimationFrame(this.gameLoop);
  };

  // Block creation methods
  createBlocks = () => {
    this.blocks = [];
    this.state.blockCount = 0;
    let blockWidth = this.calculateBlockWidth();
    let maxBlockHeight = Math.max(((this.board.height * 2) / 3 - AGAME_BLOCK_Y_OFFSET) / this.blockRows - 10, AGAME_MIN_BLOCK_HEIGHT);

    // Create the blocks with the maximum block height
    for (let row = 0; row < Math.min(this.blockRows, AGAME_BOARD_MAX_ROWS); row++) {
      for (let column = 0; column < this.blockColumns; column++) {
        let combinedWords = this.attackMatrix[row][column];
        if (combinedWords) {
          let wordsArray = this.splitWordsToFitBlock(combinedWords, blockWidth);
          let fontSize = this.calculateFontSize(blockWidth, wordsArray.length);
          if (fontSize > maxBlockHeight) {
            fontSize = maxBlockHeight;
          }
          this.board.context.font = fontSize + "px sans-serif";
          let newBlock = this.createBlockObject(column, row, blockWidth, maxBlockHeight, wordsArray, fontSize);
          this.blocks.push(newBlock);
          this.state.blockCount++;
        }
      }
    }
  };

  calculateFontSize = (blockWidth, blockHeight) => {
    const area = blockWidth * blockHeight;
    const averageTextLength = 50;
    const fontSize = Math.sqrt(area / averageTextLength);
    return Math.max(10, Math.min(fontSize, 20));
  };

  calculateBlockWidth = () => {
    return (this.board.width - 2 * AGAME_BLOCK_X_OFFSET) / this.blockColumns;
  };

  splitWordsToFitBlock = (combinedWords, blockWidth) => {
    let wordsArray = [];
    let currentText = "";
    let fontSize = this.calculateFontSize(blockWidth, combinedWords.split(" ").length);
    this.board.context.font = fontSize + "px sans-serif";
    for (let word of combinedWords.split(" ")) {
      let testText = currentText === "" ? word : currentText + " " + word;
      let textWidth = this.board.context.measureText(testText).width;
      if (textWidth > blockWidth - 10) {
        wordsArray.push(currentText);
        currentText = word;
      } else {
        currentText = testText;
      }
    }
    wordsArray.push(currentText);
    return wordsArray;
  };

  createBlockObject = (column, row, blockWidth, blockHeight, wordsArray, fontSize) => {
    let newBlock = new Block(
      blockWidth,
      blockHeight,
      AGAME_BLOCK_X_OFFSET + column * blockWidth,
      AGAME_BLOCK_Y_OFFSET + row * blockHeight,
      wordsArray,
      fontSize
    );
    newBlock.textX = newBlock.x + 5; // Add some padding from the left
    newBlock.textY = newBlock.y + 20; // Add some padding from the top
    return newBlock;
  };

  // Drawing methods
  clearCanvas = () => {
    this.board.context.clearRect(0, 0, this.board.width, this.board.height);
  };

  drawPaddle = () => {
    // Set the fill style to a solid color
    this.board.context.fillStyle = "darkgray";

    // Draw the main rectangle for the paddle
    this.board.context.fillRect(this.paddle.x, this.paddle.y, this.paddle.width, this.paddle.height);

    // Draw horizontal lines across the paddle
    this.board.context.strokeStyle = "black";
    this.board.context.lineWidth = 1;
    for (let y = this.paddle.y; y < this.paddle.y + this.paddle.height; y += 5) {
      this.board.context.beginPath();
      this.board.context.moveTo(this.paddle.x, y);
      this.board.context.lineTo(this.paddle.x + this.paddle.width, y);
      this.board.context.stroke();
    }

    // Draw vertical lines at the edges of the paddle
    this.board.context.strokeStyle = "gray";
    this.board.context.lineWidth = 6;
    this.board.context.beginPath();
    this.board.context.moveTo(this.paddle.x, this.paddle.y);
    this.board.context.lineTo(this.paddle.x, this.paddle.y + this.paddle.height);
    this.board.context.stroke();

    this.board.context.beginPath();
    this.board.context.moveTo(this.paddle.x + this.paddle.width, this.paddle.y);
    this.board.context.lineTo(this.paddle.x + this.paddle.width, this.paddle.y + this.paddle.height);
    this.board.context.stroke();
  };

  drawBall = () => {
    this.board.context.fillStyle = game.theme.currentPreset.ballColor;
    this.board.context.beginPath();
    this.board.context.arc(this.ball.x + this.ball.width / 2, this.ball.y + this.ball.height / 2, this.ball.width / 2, 0, Math.PI * 2);
    this.board.context.fill();
  };

  drawBlocks = () => {
    for (let block of this.blocks) {
      if (!block.break) {
        this.board.context.fillStyle = game.theme.currentPreset.blockColor;
        this.board.context.fillRect(block.x, block.y, block.width, block.height);
        this.board.context.strokeStyle = "black";
        this.board.context.lineWidth = 3;
        this.board.context.strokeRect(block.x, block.y, block.width, block.height);
        this.drawBlockText(block);
      }
    }
  };

  drawBlockText = (block) => {
    this.board.context.fillStyle = game.theme.currentPreset.blockTextColor;
    this.board.context.font = block.fontSize + "px sans-serif";
    let textY = block.textY;
    for (let word of block.wordsArray) {
      this.board.context.fillText(word, block.textX, textY);
      textY += block.fontSize + 5;
    }
  };

  displayDifficulty = () => {
    if (!this.state.isSmallScreen) {
      this.board.context.fillStyle = this.state.gamePaused
        ? game.theme.currentPreset.hudPausedTextColor
        : game.theme.currentPreset.hudActiveTextColor;
      this.board.context.font = "20px sans-serif";
      this.board.context.fillText("Difficulty: " + this.state.difficulty, this.board.width - 450, 25);
    }
  };

  displayLives = () => {
    this.board.context.fillStyle = this.state.gamePaused
      ? game.theme.currentPreset.hudPausedTextColor
      : game.theme.currentPreset.hudActiveTextColor;
    this.board.context.font = "20px sans-serif";
    this.board.context.fillText("Lives: " + this.state.lives, this.board.width - 100, 25);
  };

  getPercentageComplete = () => {
    const totalBlocks = this.blocks.length;
    const remainingBlocks = this.state.blockCount;
    const blocksBroken = totalBlocks - remainingBlocks;
    let percentageBroken = (blocksBroken / totalBlocks) * 100;
    return percentageBroken.toFixed(0);
  };

  displayScore = () => {
    const totalBlocks = this.blocks.length;
    const remainingBlocks = this.state.blockCount;
    const blocksBroken = totalBlocks - remainingBlocks;
    const percentageBroken = (blocksBroken / totalBlocks) * 100;

    this.board.context.fillStyle = this.state.gamePaused
      ? game.theme.currentPreset.hudPausedTextColor
      : game.theme.currentPreset.hudActiveTextColor;
    this.board.context.font = "20px sans-serif";
    this.board.context.fillText("MITRE Coverage: " + percentageBroken.toFixed(0) + "%", 10, 25);
    if (!this.state.isSmallScreen) {
      const percentageTextWidth = this.board.context.measureText("MITRE Coverage: " + percentageBroken.toFixed(0) + "%").width;
      this.board.context.fillText("Score: " + this.state.score, 10 + percentageTextWidth + 20, 25); // 20 is the space between the two texts
    }
  };

  splitMessageIntoLines = (message, maxWidth) => {
    const words = message.split(" ");
    const lines = [];
    let currentLine = words[0];

    for (let i = 1; i < words.length; i++) {
      let word = words[i];
      if (word.includes("\n")) {
        const splitWord = word.split("\n");
        currentLine += " " + splitWord[0];
        lines.push(currentLine);
        currentLine = splitWord[1];
      } else {
        const width = this.board.context.measureText(currentLine + " " + word).width;
        if (width < maxWidth) {
          currentLine += " " + word;
        } else {
          lines.push(currentLine);
          currentLine = word;
        }
      }
    }
    lines.push(currentLine);
    return lines;
  };

  displayGameHistory = () => {
    if (this.state.gameHistory.length > 0) {
      let topScores = this.state.gameHistory.sort((a, b) => b.score - a.score).slice(0, 3);
      this.board.context.fillStyle = "white";
      this.board.context.font = "20px sans-serif";

      // Draw table headers
      const headers = ["Rank", "Difficulty", "MITRE Coverage", "Score"];
      const columnWidth = this.board.width / headers.length;
      headers.forEach((header, index) => {
        this.board.context.fillText(header, columnWidth * index + 10, this.board.height / 2 + 210);
      });

      // Draw table rows
      topScores.forEach((game, index) => {
        const rowY = this.board.height / 2 + 240 + index * 30;
        this.board.context.fillText(index + 1, 10, rowY);
        this.board.context.fillText(game.difficulty, columnWidth + 10, rowY);
        this.board.context.fillText(game.percentageBroken + "%", columnWidth * 2 + 10, rowY);
        this.board.context.fillText(game.score, columnWidth * 3 + 10, rowY);
      });
    }
  };

  displayMessage = (condition, message) => {
    if (condition) {
      // Draw a fancy background rectangle box
      this.board.context.fillStyle = this.theme.currentPreset.messageBoxBgColor;
      this.board.context.strokeStyle = this.theme.currentPreset.borderColor;
      this.board.context.lineWidth = 10;
      this.board.context.font = this.state.isSmallScreen ? "50px sans-serif" : "64px sans-serif";

      const padding = 20;
      const lineHeight = this.state.isSmallScreen ? 50 : 64;

      // Split the message into lines
      const boxWidth = this.board.width * 0.8;
      const lines = this.splitMessageIntoLines(message, boxWidth);

      // Calculate the size of the message box
      const boxHeight = lines.length * lineHeight + padding * 2;
      const boxX = (this.board.width - boxWidth) / 2;
      const boxY = (this.board.height - boxHeight) / 2 - 100;
      // Draw the message box
      this.board.context.fillStyle = this.theme.currentPreset.messageBoxBgColor;
      this.board.context.globalAlpha = 0.7;
      this.board.context.fillRect(boxX, boxY, boxWidth, boxHeight);
      this.board.context.globalAlpha = 1;
      // Display the message
      this.board.context.fillStyle = this.theme.currentPreset.messageBoxTextColor;
      this.board.context.font = this.state.isSmallScreen ? "50px sans-serif" : "64px sans-serif";
      this.board.context.textAlign = "center";
      for (let i = 0; i < lines.length; i++) {
        this.board.context.fillText(lines[i], this.board.width / 2, boxY + (i + 1) * lineHeight);
      }
      this.board.context.textAlign = "start";
    }
  };

  displayPauseMessage = () => {
    if (this.state.gamePaused && !this.state.gameOver && !this.state.levelCompleted) {
      const message = this.state.lives < 3 ? `Lives Remaining: ${this.state.lives}` : "PAUSED";
      this.displayMessage(true, message);
    }
  };

  displayLevelCompleteMessage = () => {
    const message = `100% MITRE Coverage Achieved!!!`;
    this.displayMessage(this.state.levelCompleted, message);
    this.drawLevelCompleteButtons();
  };

  displayGameOverMessage = () => {
    const message = "GAME OVER";
    this.displayMessage(this.state.gameOver, message);
    if (this.state.gameOver) {
      this.drawGameOverButtons();
    }
  };

  drawGameOverButtons = () => {
    const buttonWidth = 200;
    const buttonHeight = 50;
    const padding = 10;
    const messageHeight = 64; // Assuming the message font size is 64px
    const messageY = (this.board.height - messageHeight) / 2;
    const buttonsY = messageY + messageHeight + padding;
    // Draw "Share on Twitter" button
    const twitterButtonX = (this.board.width - buttonWidth) / 2;
    const twitterButtonY = buttonsY;
    this.board.context.fillStyle = "#1DA1F2";
    this.board.context.fillRect(twitterButtonX, twitterButtonY, buttonWidth, buttonHeight);
    this.board.context.fillStyle = "white";
    this.board.context.font = "20px sans-serif";
    this.board.context.textAlign = "center";
    this.board.context.textBaseline = "middle";
    this.board.context.fillText("Share on X (Twitter)", twitterButtonX + buttonWidth / 2, twitterButtonY + buttonHeight / 2);
    // Draw "Share on Bluesky" button
    const blueskyButtonX = (this.board.width - buttonWidth) / 2;
    const blueskyButtonY = twitterButtonY + buttonHeight + padding;
    this.board.context.fillStyle = "#0070FF";
    this.board.context.fillRect(blueskyButtonX, blueskyButtonY, buttonWidth, buttonHeight);
    this.board.context.fillStyle = "white";
    this.board.context.fillText("Share on Bluesky", blueskyButtonX + buttonWidth / 2, blueskyButtonY + buttonHeight / 2);
    // Draw "Start Over" button
    const startOverButtonX = (this.board.width - buttonWidth) / 2;
    const startOverButtonY = blueskyButtonY + buttonHeight + padding;
    this.board.context.fillStyle = "#4CAF50";
    this.board.context.fillRect(startOverButtonX, startOverButtonY, buttonWidth, buttonHeight);
    this.board.context.fillStyle = "white";
    this.board.context.fillText("Start Over", startOverButtonX + buttonWidth / 2, startOverButtonY + buttonHeight / 2);
    // Reset text alignment and baseline
    this.board.context.textAlign = "start";
    this.board.context.textBaseline = "alphabetic";
  };

  displayStartScreen = () => {
    this.createBlocks();
    this.drawBlocks();

    const message = "Can you get 100% MITRE Coverage?";
    this.displayMessage(true, message);
    this.displayGameHistory();
    this.drawDifficultyButtons();

    // Draw the theme change button
    const buttonText = "Randomize!";
    const buttonWidth = 150;
    const buttonHeight = 50;
    const padding = 20;
    const buttonX = this.board.width - buttonWidth - padding;
    const buttonY = padding;
    const borderRadius = 15;
    this.board.context.fillStyle = this.theme.currentPreset.blockColor;
    this.roundRect(buttonX, buttonY, buttonWidth, buttonHeight, borderRadius, true, false);
    // Add a border to the button
    this.board.context.strokeStyle = this.theme.currentPreset.borderColor;
    this.board.context.lineWidth = 5;
    this.roundRect(buttonX, buttonY, buttonWidth, buttonHeight, borderRadius, false, true);
    // Draw the button text
    this.board.context.fillStyle = this.theme.currentPreset.blockTextColor;
    this.board.context.font = "20px sans-serif";
    this.board.context.textAlign = "center";
    this.board.context.fillText(buttonText, buttonX + buttonWidth / 2, buttonY + buttonHeight / 2 + 5);
    this.board.context.textAlign = "start";
    if (this.state.isSmallScreen) {
      const smallScreenMessage = "Best played on larger screens";
      const messageWidth = this.board.context.measureText(smallScreenMessage).width;
      const boxWidth = messageWidth + 20;
      const boxHeight = 30;
      const boxX = (this.board.width - boxWidth) / 2;
      const boxY = this.board.height / 2 - 250 - boxHeight / 2;
      // Draw the shaded box
      this.board.context.fillStyle = "rgba(0, 0, 0, 0.75)";
      this.board.context.fillRect(boxX, boxY, boxWidth, boxHeight);
      // Draw the text on top of the box
      this.board.context.fillStyle = "red";
      this.board.context.font = "20px sans-serif";
      this.board.context.textAlign = "center";
      this.board.context.fillText(smallScreenMessage, this.board.width / 2, this.board.height / 2 - 245);
      this.board.context.textAlign = "start";
    }
  };

  handleResize = () => {
    this.board.resizeBoard();
    this.paddle.generatePaddleData(this.board.width, this.board.height);
    this.ball.generateInitialBall(this.board.width, this.board.height);
    if (!this.state.gameStarted) {
      this.displayStartScreen();
    } else {
      this.setupGame();
      this.draw();
    }
  };

  roundRect = (x, y, width, height, radius, fill, stroke) => {
    if (typeof stroke === "undefined") {
      stroke = true;
    }
    if (typeof radius === "undefined") {
      radius = 5;
    }
    if (typeof radius === "number") {
      radius = { tl: radius, tr: radius, br: radius, bl: radius };
    } else {
      var defaultRadius = { tl: 0, tr: 0, br: 0, bl: 0 };
      for (var side in defaultRadius) {
        radius[side] = radius[side] || defaultRadius[side];
      }
    }
    this.board.context.beginPath();
    this.board.context.moveTo(x + radius.tl, y);
    this.board.context.lineTo(x + width - radius.tr, y);
    this.board.context.quadraticCurveTo(x + width, y, x + width, y + radius.tr);
    this.board.context.lineTo(x + width, y + height - radius.br);
    this.board.context.quadraticCurveTo(x + width, y + height, x + width - radius.br, y + height);
    this.board.context.lineTo(x + radius.bl, y + height);
    this.board.context.quadraticCurveTo(x, y + height, x, y + height - radius.bl);
    this.board.context.lineTo(x, y + radius.tl);
    this.board.context.quadraticCurveTo(x, y, x + radius.tl, y);
    this.board.context.closePath();
    if (fill) {
      this.board.context.fill();
    }
    if (stroke) {
      this.board.context.stroke();
    }
  };

  // Collision detection methods
  checkCollision = (object1, object2) => {
    return object1.left < object2.right && object1.right > object2.left && object1.top < object2.bottom && object1.bottom > object2.top;
  };

  handleBallCollision = () => {
    if (this.checkCollision(this.ball, this.paddle)) {
      // Check if ball hit the paddle
      if (this.ball.y < this.paddle.y) {
        this.ball.velocityY = Math.abs(this.ball.velocityY) * -1;
        // Calculate the four zones of the paddle
        let paddleZone1 = this.paddle.x + this.paddle.width * 0.1;
        let paddleZone2 = this.paddle.x + this.paddle.width * 0.5;
        let paddleZone3 = this.paddle.x + this.paddle.width * 0.9;
        // Check which zone the ball hit and adjust the X velocity accordingly
        if (this.ball.x < paddleZone1) {
          this.ball.velocityX = Math.max(this.ball.velocityX - 2, this.state.minBallVelocityX);
        } else if (this.ball.x < paddleZone2) {
          this.ball.velocityX = Math.max(this.ball.velocityX - 1, this.state.minBallVelocityX);
        } else if (this.ball.x < paddleZone3) {
          this.ball.velocityX = Math.min(this.ball.velocityX + 1, this.state.maxBallVelocityX);
        } else {
          this.ball.velocityX = Math.min(this.ball.velocityX + 2, this.state.maxBallVelocityX);
        }
      }
    }

    for (let i = 0; i < this.blocks.length; i++) {
      let block = this.blocks[i];
      if (!block.break && this.checkCollision(this.ball, block)) {
        this.blockCollision(block);
      }
    }
  };

  blockCollision = (block) => {
    this.particleSystem.createExplosion(block.x + block.width / 2, block.y + block.height / 2, 50, "orange");
    block.break = true;
    let scoreIncrement = AGAME_SCORE_INCREMENT;
    if (this.state.difficulty === "Medium") {
      scoreIncrement *= 2;
    } else if (this.state.difficulty === "Hard") {
      scoreIncrement *= 3;
    }
    this.state.score += scoreIncrement;
    this.state.blockCount -= 1;
    // Calculate the differences between the ball and block positions
    let diffTop = Math.abs(this.ball.bottom - block.top);
    let diffBottom = Math.abs(this.ball.top - block.bottom);
    let diffLeft = Math.abs(this.ball.right - block.left);
    let diffRight = Math.abs(this.ball.left - block.right);
    // Find the smallest difference
    let minDiff = Math.min(diffTop, diffBottom, diffLeft, diffRight);
    // Reverse the appropriate velocity based on the smallest difference
    switch (minDiff) {
      // Ball hits top of block, goes up
      case diffTop:
        this.ball.velocityY = Math.abs(this.ball.velocityY) * -1;
        break;

      // Ball hits bottom of block, goes down
      case diffBottom:
        this.ball.velocityY = Math.abs(this.ball.velocityY);
        break;

      // Ball hits left of block, goes left
      case diffLeft:
        this.ball.velocityX = Math.abs(this.ball.velocityX) * -1;
        break;

      // Ball hits right of block, goes right
      case diffRight:
        this.ball.velocityX = Math.abs(this.ball.velocityX);
        break;
    }
  };

  checkBallBounds = () => {
    if (this.ball.y <= 0) {
      this.ball.velocityY *= -1;
    } else if (this.ball.x <= 0 || this.ball.x + this.ball.width >= this.board.width) {
      this.ball.velocityX *= -1;
    } else if (this.ball.y + this.ball.height >= this.board.height) {
      this.state.lives -= 1;
      if (this.state.lives === 0) {
        this.state.gameOver = true;
        const totalBlocks = this.blocks.length;
        const remainingBlocks = this.state.blockCount;
        const blocksBroken = totalBlocks - remainingBlocks;
        const percentageBroken = (blocksBroken / totalBlocks) * 100;
        this.state.gameHistory.push({
          difficulty: this.state.difficulty,
          percentageBroken: percentageBroken.toFixed(0),
          score: this.state.score,
        });
      } else {
        this.ball.generateInitialBall(this.board.width, this.board.height);
        this.state.gamePaused = true;
      }
    }
  };

  checkNextLevel = () => {
    if (this.state.blockCount == 0) {
      this.state.levelCompleted = true;
      // fireworks!
      for (let i = 0; i < 10; i++) {
        const x = Math.random() * this.board.width;
        const y = this.board.height;
        this.particleSystem.fireworks.push(new Firework(x, y));
      }
      this.state.gamePaused = true;
    }
  };

  outOfBounds = (xPosition) => {
    return xPosition < 0 || xPosition > this.board.width - this.paddle.width;
  };

  handleArrowLeftKey = () => {
    if (!this.state.gamePaused) {
      const nextPaddleX = this.paddle.x - this.paddle.velocityX;
      if (!this.outOfBounds(nextPaddleX)) {
        this.paddle.x = nextPaddleX;
      } else {
        this.paddle.x = 0;
      }
    }
  };

  handleArrowRightKey = () => {
    if (!this.state.gamePaused) {
      const nextPaddleX = this.paddle.x + this.paddle.velocityX;
      if (!this.outOfBounds(nextPaddleX)) {
        this.paddle.x = nextPaddleX;
      } else {
        this.paddle.x = this.board.width - this.paddle.width;
      }
    }
  };

  handleSpaceKey = () => {
    if (!this.state.gameStarted) {
      this.setDifficulty(this.MEDIUM_DIFFICULTY);
      this.startGame();
    } else if (this.state.gameOver) {
      this.resetGame();
    } else if (!this.state.gamePaused) {
      this.state.gamePaused = true;
      cancelAnimationFrame(this.animationId);
      this.displayPauseMessage();
    } else {
      this.state.gamePaused = false;
      cancelAnimationFrame(this.animationId);
      this.animationId = requestAnimationFrame(this.gameLoop);
    }
  };

  handleNextLevelClick = () => {
    this.board.context.canvas.removeEventListener("click", this.handleNextLevelClick);
    this.state.gamePaused = false;
    this.level.nextLevel();
    this.state.levelCompleted = false;
  };

  handleThemeChangeClick = (e) => {
    const rect = this.board.context.canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const buttonWidth = 150;
    const buttonHeight = 50;
    const padding = 20;
    const buttonX = this.board.width - buttonWidth - padding;
    const buttonY = padding;
    if (x > buttonX && x < buttonX + buttonWidth && y > buttonY && y < buttonY + buttonHeight) {
      const randomLevel = Math.floor(Math.random() * this.theme.presets.length) + 1;
      this.theme.changeTheme(randomLevel);
      this.theme.applyTheme();
      this.displayStartScreen();
    }
  };

  setDifficulty = (difficulty) => {
    this.ball.velocityX = difficulty.velocity;
    this.ball.velocityY = difficulty.velocity;
    this.state.minBallVelocityX = -difficulty.velocity;
    this.state.maxBallVelocityX = difficulty.velocity;
    this.state.difficulty = difficulty.name;
  };

  resetGame = () => {
    this.state.initialState();
    this.setupCanvas();
    this.setupGame();
  };

  winSayings = [
    `100% MITRE coverage! Crushing those cyber threats like a boss! 😎`,
    `100% MITRE coverage! I'm on a winning streak! 🔥`,
    `100% MITRE coverage! I'm unstoppable! 🚀`,
    `Achieved 100% MITRE coverage! Cyber threats, you're going down! 🔥`,
    `Achieved 100% MITRE coverage! Cyber threats, you've met your match! 🎯`,
    `Achieved 100% MITRE coverage! Cybersecurity, consider yourself conquered! 💪`,
    `Achieved 100% MITRE coverage! Cybersecurity, consider yourself defeated! 💪`,
    `Achieved 100% MITRE coverage! Cybersecurity, you've met your match! 🎯`,
    `Achieved 100% MITRE coverage! That's how it's done! 🎯`,
    `Just aced 100% MITRE coverage! I'm on a roll! 🚀`,
    `Just aced 100% MITRE coverage! I'm on top of the world! 🌍`,
    `Just aced 100% MITRE coverage! I'm unstoppable! 💪`,
    `Just aced 100% MITRE coverage! Who's the cybersecurity champ now? 🏆`,
    `Just hit 100% MITRE coverage! Can't stop, won't stop! 🎲`,
    `Just hit 100% MITRE coverage! I'm a cybersecurity superhero! 🦸‍♂️`,
    `Just hit 100% MITRE coverage! I'm a cybersecurity superstar! 🌟`,
    `Just hit 100% MITRE coverage! I'm a cybersecurity wizard! 🧙‍♂️`,
    `Just hit 100% MITRE coverage! I'm on fire! 🔥`,
    `Just hit 100% MITRE coverage! I'm on top of my game! 🏆`,
    `Just scored 100% MITRE coverage! Cybersecurity game strong! 💪`,
    `Just smashed 100% MITRE coverage! Taking cybersecurity to the next level! 📈`,
    `Nailed 100% MITRE coverage today! Can't touch this! 💪`,
    `Nailed 100% MITRE coverage! Cybersecurity, consider yourself conquered! 💪`,
    `Nailed 100% MITRE coverage! I'm a cybersecurity ninja! 🥷`,
    `Nailed 100% MITRE coverage! I'm a game changer! 🎲`,
    `Nailed 100% MITRE coverage! I'm a game changer! 🚀`,
    `Scored 100% MITRE coverage! Cyber threats, beware! 🔥`,
    `Scored 100% MITRE coverage! Cyber threats, you're going down! 🔥`,
    `Scored 100% MITRE coverage! Cyber threats, you've met your match! 🎯`,
    `Scored 100% MITRE coverage! Cybersecurity has got nothing on me! 🚀`,
    `🎉 Just got 100% MITRE coverage! Feeling like a cybersecurity pro! 💻🔒`,
    `🎊 Celebrating 100% MITRE coverage! Winning never felt so good!`,
    `💥 Boom! 100% MITRE coverage! Cyber threats, consider yourself defeated!`,
    `💥 Boom! 100% MITRE coverage! I'm a cybersecurity rockstar! 🎸`,
    `💥 Boom! 100% MITRE coverage! I'm a cybersecurity superstar! 🌟`,
    `💯% MITRE coverage achieved! I'm on a roll! 🎲`,
    `💯% MITRE coverage! I'm on a winning streak! 🎲`,
    `💯% MITRE coverage! I'm on top of my game!`,
    `💯% MITRE coverage! I'm on top of the world! 🌍`,
    `🔥 Just hit 100% MITRE coverage! I'm on fire!`,
  ];

  verbs = ["achieved", "got", "managed", "managed to get", "reached", "scored"];
  phrases = [
    "I'm getting closer to 100%!",
    "I'm not stopping until I get 100%!",
    "I'm not there yet, but I'm making progress!",
    "I'm not there yet, but I'm not giving up!",
    "I'm on the path to 100%!",
    "Not quite 100%, but I'll get there!",
    "I'm getting closer to full coverage!",
    "I'm making progress towards 100%!",
    "Next time, I'm aiming for 100%!",
    "I won't stop until I reach 100%!",
    "I'm on my way to full coverage!",
    "I'm not giving up until I reach 100%!",
    "I'm determined to get 100% next time!",
    "Not bad, but I can do better!",
    "I'm on my way to 100%!",
  ];
  emojis = ["💪", "🚀", "🏃‍♂️", "📈", "🎯", "🧗‍♂️"];

  getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
  }

  generateGameOverSaying(percentageComplete) {
    const verb = this.getRandomElement(this.verbs);
    const phrase = this.getRandomElement(this.phrases);
    const emoji = this.getRandomElement(this.emojis);
    return `I ${verb} ${percentageComplete}% MITRE coverage. ${phrase} ${emoji}`;
  }

  generateTwitterShareLink = (percentageComplete, isWin) => {
    let attackhandle = "@mitreattack";
    let hashtag = isWin ? "#igotfullattackcoverage" : "#igotpartialattackcoverage";
    let randomSaying = isWin
      ? this.winSayings[Math.floor(Math.random() * this.winSayings.length)]
      : this.generateGameOverSaying(percentageComplete);

    const gameUrl = encodeURIComponent(document.location.href);
    const text = encodeURIComponent(`${randomSaying} ${hashtag} ${attackhandle}`);
    return `https://twitter.com/intent/tweet?text=${text}&url=${gameUrl}`;
  };

  generateBlueskyShareLink = (percentageComplete, isWin) => {
    let attackhandle = "@attack.mitre.org";
    let hashtag = isWin ? "#igotfullattackcoverage" : "#igotpartialattackcoverage";
    let randomSaying = isWin
      ? this.winSayings[Math.floor(Math.random() * this.winSayings.length)]
      : this.generateGameOverSaying(percentageComplete);

    const gameUrl = document.location.href;
    const text = encodeURIComponent(`${randomSaying} ${hashtag} ${attackhandle}. Play the game here: ${gameUrl}`);
    return `https://bsky.app/intent/compose?text=${text}`;
  };
}

let game = new Game();

window.onload = function () {
  game.setup();
};
