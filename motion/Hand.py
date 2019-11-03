import qi
import argparse
import sys
import time


def main(session):
    """
    This example demonstrates how to use the ALVideoRecorder module to record a
    video file on the robot.
    """
    # Get the service ALVideoRecorder.

    vid_recorder_service = session.service("ALVideoRecorder")
    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")
    #motion_service.weakUp()

    posture_service.goToPosture("StandInit", 0.5)

    t1=time.time()
    motion_service.closeHand("RHand")
    print(time.time()-t1)

    t2=time.time()
    motion_service.closeHand("LHand")
    print(time.time()-t2)
    time.sleep(10)

    motion_service.openHand("RHand")

    motion_service.openHand("LHand")

    #motion_service.stopMove()
    #motion_service.rest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.10.132",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.10.132'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)