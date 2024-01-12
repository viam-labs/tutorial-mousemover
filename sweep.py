#This Viam project creates a mouse mover that makes a continuous servo turn at random angles clockwise and counterclockwise between 80 and 93 degrees for random lengths of time between 5 and 20 seconds long.

import asyncio
from time import sleep
import random

#Here we are stating what services from the Viam App we need to use in the SDK.
from viam.robot.client import RobotClient
from viam.components.servo import Servo
from viam.rpc.dial import Credentials, DialOptions

#This code connects the SDK to the Viam App. You can get this code from the "CODE SAMPLE" tab from your robots page in the Viam App.
async def connect():
  opts = RobotClient.Options.with_api_key(
      # Replace "<API-KEY>" (including brackets) with your robot's API key
      api_key='<API-KEY>',
      # Replace "<API-KEY-ID>" (including brackets) with your robot's API key ID
      api_key_id='<API-KEY-ID>'
  )
  return await RobotClient.at_address("<PASTE YOUR ROBOT'S ADDRESS HERE>", opts)

#This is where you put your controlling code:
async def main():
    while True:
        # Define the sequence of positions to sweep the servo through.
        sequence = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]
        robot = await connect()
        # Connecting to the servo in Viam (fs90r is the name of my servo in the app), renaming it myServo for this code.
        myServo = Servo.from_robot(robot=robot, name='fs90r')
        # This will print the robot connection status to the Viam App.
        #print('Resources:')
        #print(robot.resource_names)
         
        for _ in sequence:
            # Move the servo to a random position between 80 and 93.
            position = random.randint(80, 93)
            print(f"Turning at angle: {position}")
            await myServo.move(position)
          
            # Wait for a random amount of time between 5 and 20 seconds before moving to the next position.
            pause_time = random.uniform(5, 20)
            await asyncio.sleep(pause_time)

if __name__ == '__main__':
    asyncio.run(main())
