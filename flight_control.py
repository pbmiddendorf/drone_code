def takeoff():
    # TODO takeoff control
    # ascend to set height, HEIGHT?
    return 0


def check_altitude():
    # TODO poll altimeter
    # return current height
    return 0


def adjust_lift(rpm):
    # TODO interact with ESC to change altitude
    # increase or decrease lift
    return 0


def check_manual_override():
    # TODO check if manual override initiated
    # if manual override then land
    # else return 0
    return 0


def compare_heading_to_waypoint():
    # TODO compare current heading to heading required to reach active waypoint
    # return difference
    return 0


def adjust_heading():
    # TODO call left/right motor adjustments to change heading
    return 0


def adjust_left_motor(rpm):
    # TODO change rpm of left motor by passed amount
    # ESC interaction
    return 0


def adjust_right_motor(rpm):
    # TODO change rpm of right motor by passed amount
    # ESC interaction
    return 0


def check_range_finder():
    # TODO poll LIDAR for obstructions and avoid objects
    # object detection confidence defined as # of detections. ie 17 out of the last 20
    # checks returned an object, then assume obstruction is real
    # if object detected scan for object edge using pan servo
    # once edge detected adjust heading by degrees LIDAR is away from straight ahead
    # ie if the servo pans 20 degrees to the left and the LIDAR doesn't see anything
    # turn the heading 20 degrees to the left
    # then fly in that direction the distance that was last reported that the object
    # was from the vehicle. Then resume normal flight
    return 0


def check_battery():
    # TODO poll battery monitor
    # probably using GPIO pin raw input
    return 0


def return_to_home():
    # TODO reverse the travelled path and replace the future path
    # enable home waypoint
    return 0


def check_current_location():
    # TODO compare the current gps coords with the active waypoint
    # if they're the same then advance to next waypoint
    # within error of antenna + error of program
    # if the current location == home waypoint and home waypoint is enabled then land
    return 0


def land():
    # TODO reduce lift to lower vehicle to the ground
    # then exit?
    return 0


if __name__ == "__main__" :
    # Main flight control loop
    takeoff()

    while True:
        check_altitude()
        if True: # if the altitude returned is outside bounds
            adjust_lift()

        check_current_location()
        compare_heading_to_waypoint()
        if True: # if the heading is outside the bounds
            adjust_heading()

        check_manual_override()
        if True: # if the manual override is sent
            return_to_home()

        check_range_finder()

        check_battery()
        if True: # if the battery level is below thresh
            return_to_home()