##### README.md
###### 15-Sep-2024

Launch PyCharm | New project | FarmaCheatSheet
```
FarmaCheatSheet
~/GitHub/SteveProXNA/OpenAItesting
source bin activate
```
IMPORTANT: if Python Interpreter not set and/or Virtual Environment not available then:
```
File | Settings... | Project: Python Interpreter | Add Interpreter | Add Local Interpreter
source bin activate
```

Copy Farma Foundation __requirements.txt__ from [here](https://github.com/Farama-Foundation/Gymnasium/blob/main/docs/requirements.txt).

[Pre-Requisites](https://gymnasium.farama.org)
```
pip install -r requirements.txt
pip install --upgrade pip
```

[ClassicControl](https://gymnasium.farama.org/environments/classic_control)
```
pip install gymnasium
```

[ToyText](https://gymnasium.farama.org/environments/toy_text)
```
pip install gymnasium
```

[Box2D](https://gymnasium.farama.org/environments/box2d)
```
pip install gymnasium
pip install Box2D
```

[muJoCo](https://gymnasium.farama.org/environments/mujoco)
```
pip install -r requirements.txt
pip install --upgrade pip
pip install mujoco==2.3.0
```

[Atari](https://gymnasium.farama.org/environments/atari)
```
pip install -r requirements.txt
pip install --upgrade pip
pip install gymnasium[atari]
pip install gymnasium[accept-rom-license]
```