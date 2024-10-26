# Space-Shooter-Game
#### Space-Shooter-Game — Game Project on Pygame
A small game developed using the Pygame library in Python. The goal is to hit incoming targets from above with a rocket-powered ball, controlled by a space shuttle. Each successful hit earns 1 point, which accumulates in the score counter. As the score increases, the game becomes more challenging, with alien targets descending faster from above.

#### Stack:
- Python
- Pygame

And other small libraries specified in `requirements.txt`.

## Project Setup on Windows

### - Stack Installing
To begin, install Python: https://www.python.org/downloads/
<br>
Links are provided to the latest version of the language.

### - Cloning a Project from GitHub
Create a root directory on your computer, then open it in your code editor or terminal.
<br>
Next, write this command into the command line:
```powershell
https://github.com/S0fft/Space-Shooter-Game.git .
```
You will see the project files appear in your directory.

### - Creating Virtual Environment
Create virtual environment:
```powershell
python -m venv .venv
```

And activate it:

```powershell
.venv\Scripts\Activate
```

### - Installing Requirements
Next, install packages:

```powershell
python.exe -m pip install --upgrade pip
```
```powershell
pip install -r requirements.txt
```

### - Launching the Game
Then, run game:
```powershell
python main.py
```

<details>
<summary><h2> Project Setup on Unix-Like Systems </h2></summary>
These commands do the same thing as described above but only on Unix systems: 
<br>

### - Stack Installing
Install Python: https://www.python.org/downloads/
<br>
Link are provided to the latest version of the language.

### - Cloning a Project from GitHub
Create a root directory on your computer, then open it in your code editor or terminal.
<br>
Next, write this command into the command line:
```powershell
https://github.com/S0fft/Space-Shooter-Game.git .
```
You will see the project files appear in your directory.

### - Creating Virtual Environment
```bash
python3 -m venv ../venv
```

```bash
source ../venv/bin/activate
```

### - Installing Requirements
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

### - Launching the Game
```bash
python3 main.py
```
</details>