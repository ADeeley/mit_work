from ps2 import *

def rectangular_room_test_suite():
    # instantiate a RectangularRoom object
    r = RectangularRoom(5,2)
    print(r.width)
    print(r.height)
    print(r.tiles)

    def test_clean_tile(x,y):
        p = Position(x,y)
        print("test_clean_tile", r.cleanTileAtPosition((p)))
        
    test_clean_tile(0,0)
    test_clean_tile(r.width-1, r.height-1)
    test_clean_tile(0.5,1.2)


    print(r.isTileCleaned(0,0))
    print(r.isTileCleaned(r.width-1, r.height-1))

    print(r.getNumTiles())

    print(r.getNumCleanedTiles())

    for n in range(0,100):
        print(r.getRandomPosition(), end=", "),

    def test_position_in_room(x,y):
        p = Position(x,y)
        print("test_clean_tile", r.isPositionInRoom((p)), end="\n")
        
    test_position_in_room(0,0)
    test_position_in_room(3.2,0.9)
    test_position_in_room(r.width-1, r.height-1)
    test_position_in_room(0.0,-10)
    test_position_in_room(-0.12, 0.0)
    test_position_in_room(4.9, 1.9)

def robot_test_suite(room_width, room_height, speed=2):
    r = RectangularRoom(room_width, room_height)
    robot = Robot(r, speed)
    print(robot.getRobotPosition(), "is within range: (", room_width, " ",
            room_height, ")") 
    
    print("Robot direction is: ", robot.getRobotDirection(), " should be ", 
             robot.direction)
    

    
    
#robot_test_suite(1,2, 2)
robot_test_suite(9, 9, 2)
robot_test_suite(3.4, 5.8, 2)
robot_test_suite(1, 4, 2)
robot_test_suite(4, 1, 2)

robot_test_suite(3, 5, 1)
robot_test_suite(3, 5, 9999)

