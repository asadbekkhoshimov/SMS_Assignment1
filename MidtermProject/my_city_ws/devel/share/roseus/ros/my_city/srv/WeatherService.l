;; Auto-generated. Do not edit!


(when (boundp 'my_city::WeatherService)
  (if (not (find-package "MY_CITY"))
    (make-package "MY_CITY"))
  (shadow 'WeatherService (find-package "MY_CITY")))
(unless (find-package "MY_CITY::WEATHERSERVICE")
  (make-package "MY_CITY::WEATHERSERVICE"))
(unless (find-package "MY_CITY::WEATHERSERVICEREQUEST")
  (make-package "MY_CITY::WEATHERSERVICEREQUEST"))
(unless (find-package "MY_CITY::WEATHERSERVICERESPONSE")
  (make-package "MY_CITY::WEATHERSERVICERESPONSE"))

(in-package "ROS")





(defclass my_city::WeatherServiceRequest
  :super ros::object
  :slots (_gps ))

(defmethod my_city::WeatherServiceRequest
  (:init
   (&key
    ((:gps __gps) (instance my_city::GPSLocation :init))
    )
   (send-super :init)
   (setq _gps __gps)
   self)
  (:gps
   (&rest __gps)
   (if (keywordp (car __gps))
       (send* _gps __gps)
     (progn
       (if __gps (setq _gps (car __gps)))
       _gps)))
  (:serialization-length
   ()
   (+
    ;; my_city/GPSLocation _gps
    (send _gps :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; my_city/GPSLocation _gps
       (send _gps :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; my_city/GPSLocation _gps
     (send _gps :deserialize buf ptr-) (incf ptr- (send _gps :serialization-length))
   ;;
   self)
  )

(defclass my_city::WeatherServiceResponse
  :super ros::object
  :slots (_weather ))

(defmethod my_city::WeatherServiceResponse
  (:init
   (&key
    ((:weather __weather) (instance my_city::WeatherStatus :init))
    )
   (send-super :init)
   (setq _weather __weather)
   self)
  (:weather
   (&rest __weather)
   (if (keywordp (car __weather))
       (send* _weather __weather)
     (progn
       (if __weather (setq _weather (car __weather)))
       _weather)))
  (:serialization-length
   ()
   (+
    ;; my_city/WeatherStatus _weather
    (send _weather :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; my_city/WeatherStatus _weather
       (send _weather :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; my_city/WeatherStatus _weather
     (send _weather :deserialize buf ptr-) (incf ptr- (send _weather :serialization-length))
   ;;
   self)
  )

(defclass my_city::WeatherService
  :super ros::object
  :slots ())

(setf (get my_city::WeatherService :md5sum-) "ec5c854fe33b5ba3e765055cce88be4e")
(setf (get my_city::WeatherService :datatype-) "my_city/WeatherService")
(setf (get my_city::WeatherService :request) my_city::WeatherServiceRequest)
(setf (get my_city::WeatherService :response) my_city::WeatherServiceResponse)

(defmethod my_city::WeatherServiceRequest
  (:response () (instance my_city::WeatherServiceResponse :init)))

(setf (get my_city::WeatherServiceRequest :md5sum-) "ec5c854fe33b5ba3e765055cce88be4e")
(setf (get my_city::WeatherServiceRequest :datatype-) "my_city/WeatherServiceRequest")
(setf (get my_city::WeatherServiceRequest :definition-)
      "my_city/GPSLocation gps

================================================================================
MSG: my_city/GPSLocation
float64 latitude
---
my_city/WeatherStatus weather

================================================================================
MSG: my_city/WeatherStatus
string condition
")

(setf (get my_city::WeatherServiceResponse :md5sum-) "ec5c854fe33b5ba3e765055cce88be4e")
(setf (get my_city::WeatherServiceResponse :datatype-) "my_city/WeatherServiceResponse")
(setf (get my_city::WeatherServiceResponse :definition-)
      "my_city/GPSLocation gps

================================================================================
MSG: my_city/GPSLocation
float64 latitude
---
my_city/WeatherStatus weather

================================================================================
MSG: my_city/WeatherStatus
string condition
")



(provide :my_city/WeatherService "ec5c854fe33b5ba3e765055cce88be4e")


