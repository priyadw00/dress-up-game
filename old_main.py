#dress your best
#Priya Dalal-Whelan and Yaya Callahan

from graphics import *

win = GraphWin("dress your best!", 1000, 675)

start_up = Image(Point(510, 300), "img/startup1.gif")
start_up.draw(win)
model = Image(Point(210, 400), "img/model.png")
model.draw(win)

class Finished_cat: 
  def __init__(self, x, y):
    model = Image(Point(x, y), "img/model.png")
    model.draw(win)
    self.top = None 
    self.bottom = None 
    self.hat = None 
    self.acessory = None 
  
  def store_top(self, fname, x, y):
    self.top = fname 
  
  def construct(self):
    finished_model = Image(Point(210, 400), "img/model.png")
    if self.top:
      Image(Poin(x, y), self.top)
    #self.top = 
  def draw(self): 
    finished_model.draw()
    top.draw()
    bottom.draw()
    hat.draw()  
    acessory.draw()


    
     

class button:
    def __init__(self, p1, p2, text, win):
        self.p1 = p1
        self.p2 = p2
        self.text = text
        self.win = win
        buttoninstance = Rectangle(self.p1, self.p2)
        self.buttoninstance = buttoninstance

    def draw(self):
        
        self.buttoninstance.draw(self.win)
        self.buttoninstance.setFill(color_rgb(255, 224, 249))
        self.buttoninstance.setOutline("white")
        self.textinstance = Text(
            Point((self.p2.x - self.p1.x) / 2 + self.p1.x,
                  (self.p2.y - self.p1.y) / 2 + self.p1.y), self.text)
        self.textinstance.draw(self.win)

    def undraw(self):
        print("undraw button")
        self.buttoninstance.undraw()
        self.textinstance.setText("")


button1 = button(Point(525, 50), Point(725, 200), "bottoms", win)
button2 = button(Point(775, 50), Point(975, 200), "tops", win)
button3 = button(Point(525, 250), Point(725, 400), "hats", win)
button4 = button(Point(775, 250), Point(975, 400), "wheee", win)
button5 = button(Point(525, 450), Point(725, 600), "wheee", win)
button6 = button(Point(775, 450), Point(975, 600), "done", win)
backbutton = button(Point(10, 10), Point(150, 75), "back",win)

current_skirt = ''
current_hat = ''
current_top = ''
current_acessory = ''

outfit = []


class Clothes:
    def __init__(self, win, p1, p2, image):
        self.p1 = p1
        self.p2 = p2
        self.win = win
        self.image = image
        clothesinstance = Image(Point(self.p1, self.p2), self.image)
        self.clothesinstance = clothesinstance

    def draw(self):
        self.clothesinstance.draw(self.win)

    def undraw(self):
        self.clothesinstance.undraw()

    def append(self):
        clothes.append(self.clothesinstance)
        return clothes

    def put_on(self):  #this isn't in use anymore
        self.clothesinstance.getWidth()
        self.height = self.clothesinstance.getHeight()
        self.center_prev = self.clothesinstance.getAnchor()
        left_side = int(self.center_prev.getX()) - self.width
        right_side = int(self.center_prev.getX()) + self.width
        bottom = int(self.center_prev.getY()) - self.height
        top = int(self.center_prev.getY()) + self.height

        if (left_side) < mouseclick.x < (right_side) and (
                bottom) < mouseclick.y < (top):
            self.clothesinstance.undraw()
            on_cat = Image(Point(237, 490), self.image)
            self.newclothesinstance.draw(win)

    def get_left_side(self):
        self.width = self.clothesinstance.getWidth()
        self.center_prev = self.clothesinstance.getAnchor()
        left_side = int(self.center_prev.getX()) - self.width
        return left_side

    def get_right_side(self):
        self.width = self.clothesinstance.getWidth()
        self.center_prev = self.clothesinstance.getAnchor()
        right_side = int(self.center_prev.getX()) + self.width
        return right_side

    def get_bottom(self):
        self.height = self.clothesinstance.getHeight()
        self.center_prev = self.clothesinstance.getAnchor()
        bottom = int(self.center_prev.getY()) - self.height
        return bottom

    def get_top(self):
        self.height = self.clothesinstance.getHeight()
        self.center_prev = self.clothesinstance.getAnchor()
        top = int(self.center_prev.getY()) + self.height
        return top


def create_start():

    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()
    button6.draw()


def set_up_closet():

    button1.undraw()
    button2.undraw()
    button3.undraw()
    button4.undraw()
    button5.undraw()
    button6.undraw()
    backbutton.draw()


def main():

    in_closet = "false"
    while True:
        while in_closet == "false":
            create_start()
            print("at menu")
            mouseclick = win.getMouse()
            print("hey", mouseclick.x, mouseclick.y)

            if ((525 < mouseclick.x < 725) and (50 < mouseclick.y < 200)):
                print("set up closet")

                set_up_closet()

                pink_skirt = Clothes(win, 600, 200, "img/pink_skirt.png")
                pink_skirt.draw()
                purple_skirt = Clothes(win, 900, 200, "img/purple_skirt.png")
                purple_skirt.draw()
                current_skirt = 'purple skirt'
                purple_right = purple_skirt.get_right_side()
                purple_left = purple_skirt.get_left_side()
                purple_bottom = purple_skirt.get_bottom()
                purple_top = purple_skirt.get_top()
                # print("purple right:" ,purple_right)
                # print("purple left:", purple_left)
                # print("purple top:", purple_top)
                # print("purple bottom:", purple_bottom)

                pink_right = pink_skirt.get_right_side()
                pink_left = pink_skirt.get_left_side()
                pink_bottom = pink_skirt.get_bottom()
                pink_top = pink_skirt.get_top()
                # print("pink right:" ,pink_right)
                # print("pink left:", pink_left)
                # print("pink top:", pink_top)
                # print("pink bottom:", pink_bottom)

                in_closet = "bottoms"
                print("in closet:", in_closet)

            elif (775 < mouseclick.x < 975 and 50 < mouseclick.y < 200):
                print("in the next loop")
                set_up_closet()

                #pink_skirt = Clothes(win, 600, 200, "img/pink_skirt.png")

                #draw tops

                striped_shirt = Clothes(win, 640, 250,"img/striped_shirt.png")
                striped_shirt.draw()

                in_closet = "tops"
                print("in closet:", in_closet)

            #the other buttons will lead to other categories of clothes
            elif (525 < mouseclick.x < 725 and 250 < mouseclick.y < 400):
                set_up_closet()
                print("in hats")
                crown = Clothes(win, 600, 200, "img/crown.png")
                crown.draw()
                crown_right = crown.get_right_side()
                crown_left = crown.get_left_side()
                crown_bottom = crown.get_bottom()
                crown_top = crown.get_top()

                in_closet = "hats"

            elif (775 < mouseclick.x < 975 and 250 < mouseclick.y < 400):
                set_up_closet()

                in_closet = "weeee"

            elif (525 < mouseclick.x < 725 and 450 < mouseclick.y < 600):
                set_up_closet()

                in_closet = "weeee"

            elif (775 < mouseclick.x < 975 and 450 < mouseclick.y < 600):
                set_up_closet()
                model.undraw()
                cafe= Image(Point(510, 300), "img/cafe.png")
                cafe.draw(win)
                model_two = Image(Point(410, 500), "img/model.png")
                model_two.draw(win)
                #purple_skirt_on_cat.undraw()
                #purple_skirt_on_cat.draw()
                # if current_skirt == 'purple skirt' :
      
                #   purple_skirt_on_cat.undraw()
                #   purple_skirt_on_cat.draw()
                # elif current_skirt == 'pink skirt':
                #   pink_skirt_on_cat.draw(win)

               
                

        while in_closet == "bottoms":
            print("in bottoms")
            mouseclick = win.getMouse()
            print("hey", mouseclick.x, mouseclick.y)

            if (int(purple_left)) < mouseclick.x < (int(purple_right)) and (
                    int(purple_bottom)) < mouseclick.y < (int(purple_top)):
                print("put on purple skirt")
                current_skirt = "purple skirt"
                purple_skirt.undraw()
                purple_skirt_on_cat = Image(Point(237, 490),
                                            "img/purple_skirt.png")

                purple_skirt_on_cat.draw(win)

            if (int(pink_left)) < mouseclick.x < (int(pink_right)) and (
                    int(pink_bottom)) < mouseclick.y < (int(pink_top)):

                print("put on pink skirt")
                current_skirt = "pink skirt"
                pink_skirt.undraw()

                pink_skirt_on_cat = Image(Point(237, 490),
                                          "img/pink_skirt.png")
                pink_skirt_on_cat.draw(win)

            if (187 < mouseclick.x < 287) and (440 < mouseclick.y < 540):
                print("clicked to take off skirt")
                if current_skirt == "pink skirt":
                  print("current skirt is pink") 
                  pink_skirt_on_cat.undraw()
                  pink_skirt = Clothes(win, 600, 200, "img/pink_skirt.png")
                  print("took of pink skirt, redrawing it now")
                  pink_skirt.draw()
                  print("drawing skirt again")
                elif current_skirt == "purple skirt":
                  print("current skirt is purple")
                  purple_skirt_on_cat.undraw() 
                  purple_skirt = Clothes(win, 900, 200, "img/purple_skirt.png")
                  purple_skirt.draw()
                  print("drew")


            #if 237- (pink_skirt.width/2)< mouseclick.x<(pink_skirt.width/2) and < mouseclick.y< :
            #pink_skirt_on_cat =

            #if click on pink_skirt_on_cat
            # pink_skirt_on_cat.undraw()
            # pink_skirt.draw(win)

            # other bottons if needed

            if 10 < mouseclick.x < 150 and 10 < mouseclick.y < 75:
                print("back")
                purple_skirt.undraw()
                pink_skirt.undraw()
                backbutton.undraw()
                in_closet = "false"

        while in_closet == "tops":
            print("in tops")
            mouseclick = win.getMouse()
            print("hey", mouseclick.x, mouseclick.y)

            striped_right = striped_shirt.get_right_side()
            striped_left = striped_shirt.get_left_side()
            striped_bottom = striped_shirt.get_bottom() 
            striped_top = striped_shirt.get_top() 

            
            if (int(striped_left)) < mouseclick.x < (int(striped_right)) and (int(striped_bottom)) < mouseclick.y < (int(striped_top)):
                print("put on striped skirt")
                current_top = "striped shirt"
                striped_shirt.undraw()
                striped_shirt_on_cat = Image(Point(237, 425),
                                          "img/striped_shirt.png")
                striped_shirt_on_cat.draw(win)


            if (187 < mouseclick.x < 287) and (237< mouseclick.y < 425):
                print("clicked to take off shirt")
                if current_top == "striped shirt":
                  print("current top is striked") 
                  striped_shirt_on_cat.undraw()
                  striped_shirt = Clothes(win, 600, 200, "img/striped_shirt.png")
                  print("took off striped top, redrawing it now")
                  striped_shirt.draw()
                  print("drawing top again")
                # elif current_skirt == "purple skirt":
                #   print("current skirt is purple")
                #   purple_skirt_on_cat.undraw() 
                #   purple_skirt = Clothes(win, 900, 200, "img/purple_skirt.png")
                #   purple_skirt.draw()
                #   print("drew")

      

            # if statment for purple top

            #ect

            if 10 < mouseclick.x < 150 and 10 < mouseclick.y < 75:
                print("back")
                backbutton.undraw()
                striped_shirt.undraw()


                #undraw tops
                in_closet = "false"

        while in_closet == "acessories":

            pass

        while in_closet == "hats":
            print("in closet:", in_closet)
            mouseclick = win.getMouse()
            print("hey", mouseclick.x, mouseclick.y)

            if (int(crown_left)) < mouseclick.x < (int(crown_right)) and (
                    int(crown_bottom)) < mouseclick.y < (int(crown_top)):
                print("put on crown")
                crown.undraw()
                crown_on_cat = Image(Point(237, 215), "img/crown.png")
                crown_on_cat.draw(win)
                print("draw crown")
            #if(


# #
#           purple_skirt_on_cat= Image(Point(237, 490), "img/purple_skirt.png")
#           purple_skirt_on_cat.draw(win)

            if 10 < mouseclick.x < 150 and 10 < mouseclick.y < 75:
                print("back")
                backbutton.undraw()
                in_closet = "false"

        #backbutton = button(Point(10,10),Point(150,75), "back", win)

main()

#main()
