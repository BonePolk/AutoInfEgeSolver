# AutoInfEgeSolver
Bot for solving problems on the website https://inf-ege.sdamgia.ru/

# How to setup
## Download project with git

```
git clone https://github.com/BonePolk/AutoInfEgeSolver.git
cd AutoInfEgeSolver
```

## Install dependencies
run in root directory of project
```
pip install -r requirements.txt
```
## How to get cookie

Go to https://inf-ege.sdamgia.ru/

1.press f12 to open dev tools in your browser

2.open tab network

3.press check box to enable cache

![image](https://github.com/BonePolk/AutoInfEgeSolver/assets/87945722/40ec2f01-a8cb-48a1-baf8-3cefd4a73f08)

2.Register or sign in on website

![image](https://github.com/BonePolk/AutoInfEgeSolver/assets/87945722/ea4e8660-b16b-4a6e-babd-97a05bd223ff)

3.next use in dev tools

![image](https://github.com/BonePolk/AutoInfEgeSolver/assets/87945722/31b74b75-591d-48dd-99ef-5e415ccc3566)

4.open get message request and scroll down. You will such as

![image](https://github.com/BonePolk/AutoInfEgeSolver/assets/87945722/3d294f6a-abf7-47e9-835c-7300dfb0fbf2)

5.press right click on cookie and press "copy value"

![image](https://github.com/BonePolk/AutoInfEgeSolver/assets/87945722/bff3a631-03c0-4217-a805-6284d08dac8f)

6.and paste into api_ege/__init__.py 

![image](https://github.com/BonePolk/AutoInfEgeSolver/assets/87945722/2f542031-b1fe-4a8a-8911-b97641cf423d)

# How to run
Simply run in root directory of project
```
python3 main.py
```
or
```
python main.py
```
