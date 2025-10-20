import random
import curses #للتعامل مع الواجهة النصية
screen=curses.initscr()
curses.curs_set(0) #اخفاء المؤشر
screen_hight,screen_width=screen.getmaxyx() #الحصول على ابعاد الشاشة
window=curses.newwin(screen_hight,screen_width,0,0) #انشاء نافذة جديدة بحجم الشاشة
window.keypad(1) #تعيين مفاتيح الاسهم
window.timeout(100) #تعيين مهلة الادخال
snake_x=screen_width//4
snake_y=screen_hight//2
snake=[
    [snake_y,snake_x],
    [snake_y,snake_x-1],
    [snake_y,snake_x-2]
]
food=[screen_hight//2,screen_width//2]
window.addch(food[0],food[1],curses.ACS_PI) #رسم الطعام على الشاشة
key=curses.KEY_RIGHT #تعيين الاتجاه للحركة
while True:
    next_key=window.getch()
    key=key if next_key==-1 else next_key
    #التحقق من الاصطدام
    if snake[0][0] in [0,screen_hight-1] or snake[0][1] in [0,screen_width-1] or snake[0] in snake[1:]:
     curses.endwin()
     quit()
    new_head=[snake[0][0],snake[0][1]]
    if key==curses.KEY_DOWN:
       new_head[0]+=1
    elif key==curses.KEY_UP:
       new_head[0]-=1
    elif key==curses.KEY_RIGHT:
       new_head[1]
       new_head[1]+=1
    elif key==curses.KEY_LEFT:
       new_head[1]-=1
    snake.insert(0,new_head)
    if snake[0]==food:
       food=None
       while food is None: #البحث عن موقع جديد للطعام
          new_food=[
             random.randint(1,screen_hight-1),
             random.randint(1,screen_width-1)
          ]
          food=new_food if new_food not in snake else None
       window.addch(food[0],food[1],curses.ACS_PI)
    else:
       tail=snake.pop()
       window.addch(tail[0],tail[1],' ') #مسح موقع الذيل
    window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD) #رسم الرأس




        
    
   

    
       

