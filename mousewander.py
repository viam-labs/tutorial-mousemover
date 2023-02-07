import asyncio
import time
from time import sleep
import os
import RPi.GPIO as GPIO

# Here we are stating what services from the Viam App we need to use in the SDK
from viam.robot.client import RobotClient
from viam.components.board import Board
from viam.components.servo import ServoClient 
from viam.components.servo import Servo
from viam.rpc.dial import Credentials, DialOptions


# "CODE SAMPLE" from the Viam App connects the SDK to the Viam App
async def connect():
  creds = Credentials(
    type='robot-location-secret',
    payload='XXXXXSECRETXXXXX') 
  opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(credentials=creds))
  return await RobotClient.at_address('XXXXXSECRETXXXXX', opts)

async def main():
    robot = await connect()

    # This will print the connection status to the Viam App
    print('Resources:')
    print(robot.resource_names)
    
    # connecting to the servo in Viam (fs90r is the name in the app), renaming it myServo for this code
    myServo = Servo.from_robot(robot=robot, name='fs90r')
    
    # The further away from 90, the faster the servo spins. 90 even is a stop. 
    # 93 and 84 seem to be the equivalent speed for the FS90R.  
    
    print("Sweeping")
    await myServo.move(92) # Here we are calling to the servo and telling it to move to the right (90+ and above is right)
    time.sleep(2) # 2 is the amount of seconds this will run in this direction
    await myServo.move(84) # Here we are calling to the servo and telling it to move to the left (-90 and under is left)
    time.sleep(2)
    print("Stop for 15 seconds") 
    await myServo.stop() # Here we are calling the servo to stop
    time.sleep(15)
    print("Sweeping")
    await myServo.move(92) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(1)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(1)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(1)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(3)
    print("Stop for 30 seconds")
    await myServo.stop()
    time.sleep(30)
    print("Sweeping")
    await myServo.move(92) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    print("Stop for 60 seconds")
    await myServo.stop()
    time.sleep(60)
    print("Sweeping")
    await myServo.move(92) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(92) 
    time.sleep(5)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(5)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    print("Stop for 60 seconds")
    await myServo.stop()
    time.sleep(60)
    print("Sweeping")
    await myServo.move(92) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(92) 
    time.sleep(5)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(3)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(5)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    await myServo.move(93) 
    time.sleep(2)
    await myServo.move(84)
    time.sleep(2)
    
    await myServo.stop()
if __name__ == '__main__':
    asyncio.run(main())