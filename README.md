# Python_Console_Crawler_BOT_application
Python Console Crawler BOT application

Crawler Bot which walks in 2-dimensional plane (X, Y coordinate).
It can only turn left or right, and walk straight. 
It also knows of its current position (X, Y) as well as its direction (North, East, West and South). 
In order to command Crawler Bot to walk, it must be input with a walking command. 
The walking command can be represented with a string consisting of three alphabets R, L and W and a positive integer 
N to indicate the distance of how many positions it has to walk which can be explained as follows:

![Mockup for feature A](https://github.com/Maksim1990/Python_Console_Crawler_BOT_application/blob/master/src/images/img1.png?raw=true)

---

- **R**: Turn 90 degree to the right of Crawler Bot (clockwise)
- **L**: Turn 90 degree to the left of Crawler Bot (counterclockwise)
- **WN**: Walk straight for **N** point(s) where **N** can be any positive integers. 
---

For example, W1 means walking straight for 1 point.

### For launching application run following command:
`python perform_crawling.py`

###### These are test eaxamplea of input strings and output results.

```
1) W5RW5RW2RW1R                => (Result:  x:4,y:3, North) 
2) RRW11RLLW19RRW12LW1		   => (Result:  x:7,y:-12, South) 
3) LLW100W50RW200W10		   => (Result:  x:-210,y:-150, West) 
4) LLLLLW99RRRRRW88LLLRL 	   => (Result:  x:-99,y:88, East) 
5) W55555RW555555W444444W1     => (Result:  x:100000,y:55555, East) 
6) W5W5RW4W1     => (Result:  x:5,y:10, East) 
7) W3RRW5RW4W1     => (Result:  x:-5,y:-2, West) 
8) RLW3RRW5RW4W1L     => (Result:  x:-5,y:-2, South) 
9) lw20wwefwe5fewrrw50rw50 => (Result:  x:25,y:-50, South) 
10) adgaj30W30rrlw34w56 => (Result:  x:90,y:30, East) 
11) adgaj3030rrlw34w56R => (Result:  x:90,y:0, South) 
12) w4fdgdgdfl5r5dfbbd30w10 => (Result:  x:0,y:14, North) 
13) w4fdgdgdflw5r5dfbwbd30w10 => (Result:  x:-5,y:44, North) 
14) w4fdgdgdflw5rw5dfbbd30w10 => (Result:  x:-5,y:544, North) 
15) adada343vwe56lw4fdgdgdflw5rw5dfbbd30w10 => (Result:  x:-544,y:51, West) 
16) W-34RW40 => (Result:  x:40,y:34, East) 
17) 50lw50rrww30 => (Result:  x:-20,y:0, East)
18) rsdfsdrlw34e3rrw4l => (Result:  x:339,y:0, South)
19) rsdfsdrlw34e3rrw41 => (Result:  x:302,y:0, West)
20) 30rlw20w5r20w21lrrw21a3 => (Result:  x:21,y:-188, South)
21) 30lw20w5r20w21lrrw21a3 => (Result:  x:188,y:21, East)
```
