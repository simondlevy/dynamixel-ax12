## Code Description

### `Ax12` Class

This module allows you to connect to the AX-12A servos then read and write to
the various registers that contain information about the servos' current & goal
position, LED light, moving speed, and much more.

The original class can be [found here](https://github.com/aakieu/ax12_control),
and worked for this usecase with little modification.

### `changeID.py`

This is a short script that allows you to connect a single servo and configure
the ID associated with it.

### `singleServo.py`

Short script to display a TKinter window to control a single AX-12A's speed and
position.

## Resources

- [Dynamixel Wizard](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/):
provides visual interface to configure & manage the Dynamixel servos.

- [Dynamixel SDK Docs](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/): the software development kit to interact with the servos using the language of your choice (in this case _Python_).

- [Dynamixel AX-12A E-Manual](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/): documentation about the physical servos, including information about the different values and their registers.
