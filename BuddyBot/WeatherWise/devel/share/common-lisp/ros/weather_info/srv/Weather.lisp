; Auto-generated. Do not edit!


(cl:in-package weather_info-srv)


;//! \htmlinclude Weather-request.msg.html

(cl:defclass <Weather-request> (roslisp-msg-protocol:ros-message)
  ((city
    :reader city
    :initarg :city
    :type cl:string
    :initform ""))
)

(cl:defclass Weather-request (<Weather-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Weather-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Weather-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name weather_info-srv:<Weather-request> is deprecated: use weather_info-srv:Weather-request instead.")))

(cl:ensure-generic-function 'city-val :lambda-list '(m))
(cl:defmethod city-val ((m <Weather-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weather_info-srv:city-val is deprecated.  Use weather_info-srv:city instead.")
  (city m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Weather-request>) ostream)
  "Serializes a message object of type '<Weather-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'city))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'city))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Weather-request>) istream)
  "Deserializes a message object of type '<Weather-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'city) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'city) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Weather-request>)))
  "Returns string type for a service object of type '<Weather-request>"
  "weather_info/WeatherRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Weather-request)))
  "Returns string type for a service object of type 'Weather-request"
  "weather_info/WeatherRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Weather-request>)))
  "Returns md5sum for a message object of type '<Weather-request>"
  "07a56992612a9868fceaf6083a0c9b4c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Weather-request)))
  "Returns md5sum for a message object of type 'Weather-request"
  "07a56992612a9868fceaf6083a0c9b4c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Weather-request>)))
  "Returns full string definition for message of type '<Weather-request>"
  (cl:format cl:nil "string city~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Weather-request)))
  "Returns full string definition for message of type 'Weather-request"
  (cl:format cl:nil "string city~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Weather-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'city))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Weather-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Weather-request
    (cl:cons ':city (city msg))
))
;//! \htmlinclude Weather-response.msg.html

(cl:defclass <Weather-response> (roslisp-msg-protocol:ros-message)
  ((city_name
    :reader city_name
    :initarg :city_name
    :type cl:string
    :initform "")
   (temperature
    :reader temperature
    :initarg :temperature
    :type cl:float
    :initform 0.0)
   (humidity
    :reader humidity
    :initarg :humidity
    :type cl:float
    :initform 0.0)
   (description
    :reader description
    :initarg :description
    :type cl:string
    :initform ""))
)

(cl:defclass Weather-response (<Weather-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Weather-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Weather-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name weather_info-srv:<Weather-response> is deprecated: use weather_info-srv:Weather-response instead.")))

(cl:ensure-generic-function 'city_name-val :lambda-list '(m))
(cl:defmethod city_name-val ((m <Weather-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weather_info-srv:city_name-val is deprecated.  Use weather_info-srv:city_name instead.")
  (city_name m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <Weather-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weather_info-srv:temperature-val is deprecated.  Use weather_info-srv:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'humidity-val :lambda-list '(m))
(cl:defmethod humidity-val ((m <Weather-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weather_info-srv:humidity-val is deprecated.  Use weather_info-srv:humidity instead.")
  (humidity m))

(cl:ensure-generic-function 'description-val :lambda-list '(m))
(cl:defmethod description-val ((m <Weather-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader weather_info-srv:description-val is deprecated.  Use weather_info-srv:description instead.")
  (description m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Weather-response>) ostream)
  "Serializes a message object of type '<Weather-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'city_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'city_name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'temperature))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'humidity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'description))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'description))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Weather-response>) istream)
  "Deserializes a message object of type '<Weather-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'city_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'city_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temperature) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'humidity) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'description) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'description) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Weather-response>)))
  "Returns string type for a service object of type '<Weather-response>"
  "weather_info/WeatherResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Weather-response)))
  "Returns string type for a service object of type 'Weather-response"
  "weather_info/WeatherResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Weather-response>)))
  "Returns md5sum for a message object of type '<Weather-response>"
  "07a56992612a9868fceaf6083a0c9b4c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Weather-response)))
  "Returns md5sum for a message object of type 'Weather-response"
  "07a56992612a9868fceaf6083a0c9b4c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Weather-response>)))
  "Returns full string definition for message of type '<Weather-response>"
  (cl:format cl:nil "string city_name~%float32 temperature~%float32 humidity~%string description~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Weather-response)))
  "Returns full string definition for message of type 'Weather-response"
  (cl:format cl:nil "string city_name~%float32 temperature~%float32 humidity~%string description~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Weather-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'city_name))
     4
     4
     4 (cl:length (cl:slot-value msg 'description))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Weather-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Weather-response
    (cl:cons ':city_name (city_name msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':humidity (humidity msg))
    (cl:cons ':description (description msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Weather)))
  'Weather-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Weather)))
  'Weather-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Weather)))
  "Returns string type for a service object of type '<Weather>"
  "weather_info/Weather")