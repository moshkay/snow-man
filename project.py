#!usr/bin/python
try:
    from turtle import *
except:
    print("import error")
#the shapes' classes
hideturtle()
screensize(1000,1000)
title("Snow Characters")

class CreateRectangle:
    """The class that creates the rectangles in this program
    ****************************************************
    This class takes the attributes
    *height
    *width
    *x and y for the coordinates
    *color
    """
    

    def __init__(self,height,width,x,y,color=None):
        """The constructor for the class that creates the rectangles"""
        self.height=height
        self.width=width
        self.x=x
        self.y=y
        self.color=color

        #calling the drawRect methods
        self.drawRect()
        
    
    def __str__(self):
        """The method that returns the instance this class"""
        return "({0},{1},{2},{3},{4})".format(self.height,self.width,self.x,self.y,self.color)

    def drawRect(self):
        """The method that draw lines
        using the height attribute and x,y as cordinates.
        it can also use color if given"""
        pu()
        home()
        color(self.color)
        begin_fill()
        goto(self.x,self.y)
        pd()
        fd(self.width);lt(90);fd(self.height);lt(90);fd(self.width);lt(90);fd(self.height)
        end_fill()
        
    

#the Circle class 
class CreateCircle:
    """The class that creates a create circle
    ******************************************
    this takes in the attributes
    *x any for the coordinates
    *radius of the circle 
    
    *"""
    def __init__(self,x,y,radius):
        """the constructor for the class that creates the circles"""
        self.radius=radius
        self.x=x
        self.y=y 
        #calling the method drawcircle that draws the circle
        self.drawCircle()
    
    def __str__(self):
        """The method that returns the instance this class"""
        return "({0},{1},{2})".format(self.x,self.y,self.radius)

    def drawCircle(self):
        """the method that draws the circle"""
        pu()
        #taking the cursor to the point coordinates for the circle
        goto(self.x,self.y)
        pd()
        circle(self.radius)#drawing circle
        

#the line class
class CreateLine:
    """The class that creates a create the lines on the canvas"""
    def __init__(self,length,x,y,lt=None,rt=None):
        """the constructor for the class that creates the lines"""
        self.length=length
        self.x=x
        self.y=y
        self.rt=rt
        self.lt=lt
        
        #calling the drawline method that performs the line drawing operation
        self.drawLine()
    
    def __str__(self):
        """The method that returns the instance this class"""
        return "({0},{1},{2},{3},{4})".format(self.length,self.x,self.y,self.lt,self.rt)

    def drawLine(self):
        
        pu()
        goto(self.x,self.y)#taking the cursor to the point coordinates for the line
        pd()
        rt(self.rt)
        lt(self.lt)
        fd(self.length)#drawing the line

#the triangle class
class CreateTriangle:
    """The class that creates a create the lines on the canvas"""
    def __init__(self,x,y,dist,color=None):
        """the constructor for the class that creates the lines
        x and y are the coordinates and dist is the distance"""
        self.x=x
        self.y=y
        self.dist=dist
        self.color=color

        #calling the method that will draw the triangle
        self.drawTriangle()
    
    def __str__(self):
        """The __str__ method for the class"""
        return "({0},{1},{2},{3})".format(self.x,self.y,self.dist,self.color)
    
    def drawTriangle(self):
        """the method that draw the triangles with the use of lines"""
        color(self.color)#color of the triangle
        penup()
        goto(self.x,self.y)#coordinates
        pd()
        begin_fill()
        rt(120)
        fd(self.dist)
        #loop to draw the triangle
        for i in range(3):
            lt(120);fd(self.dist)
        end_fill()
        
#the dot class
class CreateDot:
    """The class that creates a create the lines on the canvas"""
    def __init__(self,radius,x,y,color=None):
        """the constructor for the class that creates the lines"""
        self.radius=radius
        self.x=x
        self.y=y
        self.color=color
        #calling the drawdot method
        self.drawDot()
    
    def __str__(self):
        """The __str__ method for the class"""
        return "({0},{1},{2},{3})".format(self.radius,self.x,self.y,self.color)

    def drawDot(self):
        """the method that draws the dots"""
        pu()
        goto(self.x,self.y)#coordinates
        pd()
        dot(self.radius,self.color)#drawing the dot

#the snowperson class
class SnowPersons:
    """The class that creates a snow human being
    ********************************************
    it has the following methods
    head:: it creates the head of the object
    body:: it creates the body of the object
    nose:: it creates the nose of the object
    mouth:: it cretes the mouth of the object
    button:: it creates the button on the object
    the parent class
    *********************************************
    """
    def __init__(self,x,y,radius,color,button_color=None):
        """the constructor for SnowPersons class"""
        #globalising the variables
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
        self.button_color=button_color

        #the methods in this class
        self.head()
        self.body()
        self.nose()
        self.mouth()
        self.button()

    def __str__(self):
        """The method that returns the instance this class"""
        return "({0},{1},{2},{3},{4})".format(self.x,self.y,self.radius,self.color,self.button_color)

    def head(self):
        """this method creates the Head of the object"""

        #drawing the circle for the held
        CreateCircle(self.x,self.y,self.radius)

        #creating the eyes of the object
        CreateDot((15/50)*self.radius,(self.radius/-2)+self.x,(self.radius+(self.radius/2))+self.y,"red")
        CreateDot((15/50)*self.radius,((1/2)*self.radius)+self.x,self.radius*(75/50)+self.y,"red")

    def body(self):
        """the method that creates the two other circles"""

        rad=self.radius
        
        #creating the circles for the body of the object 
        #sec_circle
        sec_circle=rad+10
        x=0+self.x
        y=-2*sec_circle+self.y
        #drawing the sec_circle
        CreateCircle(x,y,rad+10)
        #creating the third circle
        third_circle=rad+15
        x=0+self.x
        y=-4*third_circle+self.y
        #drawing the circle for the third circle
        CreateCircle(x,y,rad+20)
        
    def nose(self):
        """creating the nose on the human"""
        #properties for the nose
        distance=(10/50)*self.radius

        #creating the triangle for the nose
        CreateTriangle(0+self.x,self.radius+self.y,distance,"green")

    def mouth(self):
        """This method uses the CreateLine Class to create mouth"""
        #proties for the mouth
        lenght=self.radius
        dist=(5/50)*lenght

        #creating the mouth with the aid of the createline method
        CreateLine(dist,-lenght/2+self.x,lenght/2+self.y,lt=60,rt=0)
        x,y=pos()#getting the present position of the turtle
        CreateLine(lenght,x,y,lt=60,rt=0)
        x,y=pos()
        CreateLine(dist,x,y,lt=60,rt=0)

    def button(self):
        """This creates the buttons on the chests"""
        #properties for the buttons
        rad=(10/50)*self.radius
        value=(20/50)*self.radius
        increment=(80/120)*(2*(self.radius+10))
        rem_circle1=(20/120)*(2*(self.radius+10))
        rem_circle2=(30/140)*(2*(self.radius+20))

        #drawing buttons for the object
        for count in range(1,5):
            CreateDot(rad,0+self.x,-value+self.y,self.button_color)
            if count!=2:
                value+=increment
            else:
                value+=rem_circle1+rem_circle2
    
                
#the snow man class
class SnowMan(SnowPersons):
    """The class that creates a snow_man\n
    but inherits from the SnowPersons' class\n
    to add a male attribute
    it adds the malecap  and hands to object"""
    

    def __init__(self,x_cor,y_cor,man_radius,man_color,button_color,capColor):
        """the constructor for SnowLady class"""
        home()
        SnowPersons.__init__(self,x_cor,y_cor,man_radius,man_color,button_color)

        #globalising the variables
        self.capColor=capColor
        self.x=x_cor
        self.y=y_cor
        self.radius=man_radius
        self.man_color=man_color
        self.button_col=button_color

        #calling the methods in this class
        self.maleCap()
        self.maleHand()
        
    def __str__(self):
        """The method that returns the instance this class"""
        return "({0},{1},{2},{3},{4},{5})".format(self.x,self.y,self.radius,
                    self.man_color,self.button_col,self.capColor)
        
            
    def maleCap(self):
        """this method that adds a male cap to the Snowman created\n
        in the snowperson' class
        """
        pu()
        home()
        
        #propeties of the tip of cap
        width=2*self.radius
        height=(10/50)*self.radius
        x = -(self.radius)+self.x
        y=(2*self.radius)-((10/50)*self.radius)+self.y
        #drawing the tip of the cap
        
        CreateRectangle(height,width,x,y,self.capColor)

        #properties of the body of the cap
        height=(40/50)*self.radius
        width=self.radius
        x=(-self.radius/2)+self.x
        y=(self.radius*2)+self.y

        #drawing the body of the cap
        CreateRectangle(height,width,x,y,self.capColor)

    def maleHand(self):
        """the method thats adds a male hands to the body"""
        pu()
        home()
        #turning the hand to the left
        x=(self.radius+10)
        width((5/50)*self.radius)
        CreateLine(self.radius*2,-x+self.x,-x+self.y,rt=200,lt=0)#left hand
        CreateLine(self.radius*2,x+self.x,-x+self.y,rt=140,lt=0)#right hand
        width(1)
        color("black")
        
               
#the snow lady class        
class SnowLady(SnowPersons):
    """The class that creates a snow_man\n
    but inherits from the SnowPersons' class\n
    to add a male attribute
    it adds the malecap  and hands to object"""

    def __init__(self,x_cor,y_cor,lady_radius,lady_color,button_color,capColor):
        """the constructor for SnowLady class"""
        pu()
        home()
        pd()

        #personalising the variables
        self.capColor=capColor
        SnowPersons.__init__(self,x_cor,y_cor,lady_radius,lady_color,button_color)
        self.capColor=capColor
        self.x=x_cor
        self.y=y_cor
        self.radius=lady_radius
        self.lady_color=lady_color
        self.button_col=button_color

        #calling the methods in this class
        self.ladyHand()
        self.ladyHair() 
        self.ladyCap()
        
        
    def __str__(self):
        """The method that returns the instance this class"""
        return "({0},{1},{2},{3},{4},{5})".format(self.x,self.y,self.radius,
                    self.lady_color,self.button_col,self.capColor)
    
    def ladyCap(self):
        """the methods that creates the lady cap"""
        pu()
        home()
        pd()
        #properties of the lady's cap
        height=self.radius+((8/50)*self.radius)
        x =0+self.x
        y=((2*self.radius)+((86.6/100)*(2*self.radius)))+self.y
        CreateTriangle(x,y,height*2,self.capColor)#creating the cap of the snow lady
        

    def ladyHand(self):
        """the method that creates the Lady hands"""
        pu()
        home()

        #properties for the hands of the lady
        rHand=(self.radius+10)#the coordinate
        width((5/50)*self.radius)
        CreateLine(self.radius*2,-rHand+self.x,-rHand+self.y,rt=200,lt=0)#left hand
        angle=200
        x,y=(rHand+self.x,-rHand+self.y)
        for i in range(2):
            
            CreateLine(self.radius+(self.radius/2),x,y,rt=angle,lt=0)#right hand
            angle=90
            x,y=pos()
        width(1)
    def ladyHair(self):
        """The method that creates the hair of the lady """
        #properties of the hair
        width((1/20)*self.radius)
        y=2*self.radius
        x1=-(self.radius-(self.radius/3.5))
        lenght=2*self.radius
        rgt=25

        #designing the hair on the right hand side
        for i in range(2):
            CreateLine(lenght,x1+self.x,y+self.y,rgt,0)
            x1+=(9/50)*self.radius
            lenght/=2
            if i==0:
                lenght2=lenght
                x2=abs(x1)
            rgt=0

        #designing the hair on the right hand side
        lft=30
        for i in range(2):
            CreateLine(lenght2,x2+self.x,y+self.y,lft,0)
            lenght2*=2
            x2+=(9/50)*self.radius
            lft=0
    
        
    
    

#the main function
def main():
    """
    The main function
    the main function that creates the objects
    both Snowman and the SnowLady
    *******************************
    it calls the Snowman's and Snowlady's classes

    """
    
    SnowMan(-100,40,20,"blue","steelblue","yellow")#snowman class
    SnowLady(100,40,20,"green","yellow","brown")#snowlady class

main()


