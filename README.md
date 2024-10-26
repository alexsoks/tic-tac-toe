# Tic-tac-toe Project

<h2>Description</h2>

<p>This Python-powered Tic-Tac-Toe game offers an engaging experience with both single-player and multiplayer modes. The game board is displayed using a simple, clear layout of three stacked lists of characters, making it easy for players to follow along.

In single-player mode, users can test their skills against a thoughtfully designed bot that mirrors realistic human decision-making, providing a challenging and immersive opponent. Multiplayer mode allows two players to face off, entering their names to personalize the experience as they take turns competing for the win.

The program also includes efficient algorithms to detect wins and draws, ensuring smooth gameplay. With its blend of simplicity and strategic depth, this game delivers a fun and realistic take on classic Tic-Tac-Toe, whether you're up for a quick match against the bot or a friendly duel with another player.</p>

<br><br>

<h2>Program walk-through</h2>
<p>Choose between single-player and multiplayer modes with entries 's' or 'm' </p>

<img width="495" alt="Screenshot 2024-10-26 at 11 25 54" src="https://github.com/user-attachments/assets/26952202-e906-43be-8b16-fe27a656a176">

<p>multiplayer mode prompts both players to enter their names</p>

<img width="549" alt="Screenshot 2024-10-26 at 11 51 30" src="https://github.com/user-attachments/assets/d6ba8433-8cdf-4157-8865-6db1e895310b">

<p> The empty game board is displayed and player 1 is prompted to make a move </p>

<img width="483" alt="Screenshot 2024-10-26 at 11 53 22" src="https://github.com/user-attachments/assets/e796adde-1494-4dd2-912d-8f2a4a00f73f">

<p>The game uses a straightforward coordinate system with indices ranging from 0 to 2, making it easy to select positions on the 3x3 grid. Players can enter row and column coordinates within this 0–2 range to place their moves, following a simple and intuitive layout that mirrors standard list indexing in Python. The updated version of the board, with the marker located in the position specified, is now displayed</p>

<img width="522" alt="Screenshot 2024-10-26 at 12 03 02" src="https://github.com/user-attachments/assets/efec1adc-8c71-42c7-a827-1a70c2e4b3cd">

<p>This process alternates betweeen the 2 players until a win or a draw is detected</p>

<img width="415" alt="Screenshot 2024-10-26 at 12 05 27" src="https://github.com/user-attachments/assets/5ba5c5df-2d57-438a-a1fb-616cc4f5dfb4">

<br><br>

<p> Playing in single-player mode follows a similar pattern to that above. During the bot's turn, an algorithm enables the programme to identify potential winning moves or block the player's winning opportunities. However, the bot only acts on these moves with a given probability, mimicking the chance that a human opponent might overlook a strategic opportunity. This adds a layer of realism and unpredictability to the bot’s gameplay.  </p>

<img width="526" alt="Screenshot 2024-10-26 at 12 19 02" src="https://github.com/user-attachments/assets/228c04df-f24d-4d92-aba1-55f4e9c7be16">







