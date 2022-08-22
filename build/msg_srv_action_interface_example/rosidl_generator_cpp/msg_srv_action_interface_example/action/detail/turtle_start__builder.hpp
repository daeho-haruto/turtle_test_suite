// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_srv_action_interface_example:action/TurtleStart.idl
// generated code does not contain a copyright notice

#ifndef MSG_SRV_ACTION_INTERFACE_EXAMPLE__ACTION__DETAIL__TURTLE_START__BUILDER_HPP_
#define MSG_SRV_ACTION_INTERFACE_EXAMPLE__ACTION__DETAIL__TURTLE_START__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_srv_action_interface_example/action/detail/turtle_start__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_Goal_order
{
public:
  Init_TurtleStart_Goal_order()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_Goal order(::msg_srv_action_interface_example::action::TurtleStart_Goal::_order_type arg)
  {
    msg_.order = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_Goal>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_Goal_order();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_Result_goal
{
public:
  Init_TurtleStart_Result_goal()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_Result goal(::msg_srv_action_interface_example::action::TurtleStart_Result::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_Result>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_Result_goal();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_Feedback_theta
{
public:
  explicit Init_TurtleStart_Feedback_theta(::msg_srv_action_interface_example::action::TurtleStart_Feedback & msg)
  : msg_(msg)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_Feedback theta(::msg_srv_action_interface_example::action::TurtleStart_Feedback::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_Feedback msg_;
};

class Init_TurtleStart_Feedback_y
{
public:
  explicit Init_TurtleStart_Feedback_y(::msg_srv_action_interface_example::action::TurtleStart_Feedback & msg)
  : msg_(msg)
  {}
  Init_TurtleStart_Feedback_theta y(::msg_srv_action_interface_example::action::TurtleStart_Feedback::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_TurtleStart_Feedback_theta(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_Feedback msg_;
};

class Init_TurtleStart_Feedback_x
{
public:
  Init_TurtleStart_Feedback_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TurtleStart_Feedback_y x(::msg_srv_action_interface_example::action::TurtleStart_Feedback::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_TurtleStart_Feedback_y(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_Feedback>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_Feedback_x();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_SendGoal_Request_goal
{
public:
  explicit Init_TurtleStart_SendGoal_Request_goal(::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request goal(::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request msg_;
};

class Init_TurtleStart_SendGoal_Request_goal_id
{
public:
  Init_TurtleStart_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TurtleStart_SendGoal_Request_goal goal_id(::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_TurtleStart_SendGoal_Request_goal(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Request>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_SendGoal_Request_goal_id();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_SendGoal_Response_stamp
{
public:
  explicit Init_TurtleStart_SendGoal_Response_stamp(::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response stamp(::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response msg_;
};

class Init_TurtleStart_SendGoal_Response_accepted
{
public:
  Init_TurtleStart_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TurtleStart_SendGoal_Response_stamp accepted(::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_TurtleStart_SendGoal_Response_stamp(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_SendGoal_Response>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_SendGoal_Response_accepted();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_GetResult_Request_goal_id
{
public:
  Init_TurtleStart_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_GetResult_Request goal_id(::msg_srv_action_interface_example::action::TurtleStart_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_GetResult_Request>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_GetResult_Request_goal_id();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_GetResult_Response_result
{
public:
  explicit Init_TurtleStart_GetResult_Response_result(::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response result(::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response msg_;
};

class Init_TurtleStart_GetResult_Response_status
{
public:
  Init_TurtleStart_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TurtleStart_GetResult_Response_result status(::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_TurtleStart_GetResult_Response_result(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_GetResult_Response>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_GetResult_Response_status();
}

}  // namespace msg_srv_action_interface_example


namespace msg_srv_action_interface_example
{

namespace action
{

namespace builder
{

class Init_TurtleStart_FeedbackMessage_feedback
{
public:
  explicit Init_TurtleStart_FeedbackMessage_feedback(::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage feedback(::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage msg_;
};

class Init_TurtleStart_FeedbackMessage_goal_id
{
public:
  Init_TurtleStart_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TurtleStart_FeedbackMessage_feedback goal_id(::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_TurtleStart_FeedbackMessage_feedback(msg_);
  }

private:
  ::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_srv_action_interface_example::action::TurtleStart_FeedbackMessage>()
{
  return msg_srv_action_interface_example::action::builder::Init_TurtleStart_FeedbackMessage_goal_id();
}

}  // namespace msg_srv_action_interface_example

#endif  // MSG_SRV_ACTION_INTERFACE_EXAMPLE__ACTION__DETAIL__TURTLE_START__BUILDER_HPP_
