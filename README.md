## turtle_test_suite

터틀심의 pose를 가져와 x좌표로 parameter 값만큼 이동 후 복귀 

> ### pakage
>   > ##### turtle_test_suite
>   > - main node and launch file
>   > ##### turtle_test_msgs
>   > - msg type of turtle_test_suite 

#### launch
```bash
ros2 launch turtle_test_suite turtle_test_suite.launch.py
```
```bash
ros2 topic pub --once /turtle1/start turtle_test_suite_msgs/msg/Start data:\ 1.0\
```

#### if use run
```bash
ros2 run turtlesim turtlesim_node
ros2 run turtle_test_suite turtle_test_suite_node
```
```bash
ros2 topic pub --once /turtle1/start turtle_test_suite_msgs/msg/Start data:\ 1.0\
```
