// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_srv_action_interface_example:action/TurtleStart.idl
// generated code does not contain a copyright notice

#ifndef MSG_SRV_ACTION_INTERFACE_EXAMPLE__ACTION__DETAIL__TURTLE_START__STRUCT_H_
#define MSG_SRV_ACTION_INTERFACE_EXAMPLE__ACTION__DETAIL__TURTLE_START__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'order'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_Goal
{
  rosidl_runtime_c__String order;
} msg_srv_action_interface_example__action__TurtleStart_Goal;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_Goal.
typedef struct msg_srv_action_interface_example__action__TurtleStart_Goal__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_Result
{
  double goal;
} msg_srv_action_interface_example__action__TurtleStart_Result;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_Result.
typedef struct msg_srv_action_interface_example__action__TurtleStart_Result__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_Feedback
{
  double x;
  double y;
  double theta;
} msg_srv_action_interface_example__action__TurtleStart_Feedback;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_Feedback.
typedef struct msg_srv_action_interface_example__action__TurtleStart_Feedback__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "msg_srv_action_interface_example/action/detail/turtle_start__struct.h"

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  msg_srv_action_interface_example__action__TurtleStart_Goal goal;
} msg_srv_action_interface_example__action__TurtleStart_SendGoal_Request;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_SendGoal_Request.
typedef struct msg_srv_action_interface_example__action__TurtleStart_SendGoal_Request__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} msg_srv_action_interface_example__action__TurtleStart_SendGoal_Response;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_SendGoal_Response.
typedef struct msg_srv_action_interface_example__action__TurtleStart_SendGoal_Response__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} msg_srv_action_interface_example__action__TurtleStart_GetResult_Request;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_GetResult_Request.
typedef struct msg_srv_action_interface_example__action__TurtleStart_GetResult_Request__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "msg_srv_action_interface_example/action/detail/turtle_start__struct.h"

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_GetResult_Response
{
  int8_t status;
  msg_srv_action_interface_example__action__TurtleStart_Result result;
} msg_srv_action_interface_example__action__TurtleStart_GetResult_Response;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_GetResult_Response.
typedef struct msg_srv_action_interface_example__action__TurtleStart_GetResult_Response__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "msg_srv_action_interface_example/action/detail/turtle_start__struct.h"

/// Struct defined in action/TurtleStart in the package msg_srv_action_interface_example.
typedef struct msg_srv_action_interface_example__action__TurtleStart_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  msg_srv_action_interface_example__action__TurtleStart_Feedback feedback;
} msg_srv_action_interface_example__action__TurtleStart_FeedbackMessage;

// Struct for a sequence of msg_srv_action_interface_example__action__TurtleStart_FeedbackMessage.
typedef struct msg_srv_action_interface_example__action__TurtleStart_FeedbackMessage__Sequence
{
  msg_srv_action_interface_example__action__TurtleStart_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_srv_action_interface_example__action__TurtleStart_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_SRV_ACTION_INTERFACE_EXAMPLE__ACTION__DETAIL__TURTLE_START__STRUCT_H_
