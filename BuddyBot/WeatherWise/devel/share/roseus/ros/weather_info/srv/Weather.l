;; Auto-generated. Do not edit!


(when (boundp 'weather_info::Weather)
  (if (not (find-package "WEATHER_INFO"))
    (make-package "WEATHER_INFO"))
  (shadow 'Weather (find-package "WEATHER_INFO")))
(unless (find-package "WEATHER_INFO::WEATHER")
  (make-package "WEATHER_INFO::WEATHER"))
(unless (find-package "WEATHER_INFO::WEATHERREQUEST")
  (make-package "WEATHER_INFO::WEATHERREQUEST"))
(unless (find-package "WEATHER_INFO::WEATHERRESPONSE")
  (make-package "WEATHER_INFO::WEATHERRESPONSE"))

(in-package "ROS")





(defclass weather_info::WeatherRequest
  :super ros::object
  :slots (_city ))

(defmethod weather_info::WeatherRequest
  (:init
   (&key
    ((:city __city) "")
    )
   (send-super :init)
   (setq _city (string __city))
   self)
  (:city
   (&optional __city)
   (if __city (setq _city __city)) _city)
  (:serialization-length
   ()
   (+
    ;; string _city
    4 (length _city)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _city
       (write-long (length _city) s) (princ _city s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _city
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _city (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass weather_info::WeatherResponse
  :super ros::object
  :slots (_city_name _temperature _humidity _description ))

(defmethod weather_info::WeatherResponse
  (:init
   (&key
    ((:city_name __city_name) "")
    ((:temperature __temperature) 0.0)
    ((:humidity __humidity) 0.0)
    ((:description __description) "")
    )
   (send-super :init)
   (setq _city_name (string __city_name))
   (setq _temperature (float __temperature))
   (setq _humidity (float __humidity))
   (setq _description (string __description))
   self)
  (:city_name
   (&optional __city_name)
   (if __city_name (setq _city_name __city_name)) _city_name)
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:humidity
   (&optional __humidity)
   (if __humidity (setq _humidity __humidity)) _humidity)
  (:description
   (&optional __description)
   (if __description (setq _description __description)) _description)
  (:serialization-length
   ()
   (+
    ;; string _city_name
    4 (length _city_name)
    ;; float32 _temperature
    4
    ;; float32 _humidity
    4
    ;; string _description
    4 (length _description)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _city_name
       (write-long (length _city_name) s) (princ _city_name s)
     ;; float32 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _humidity
       (sys::poke _humidity (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _description
       (write-long (length _description) s) (princ _description s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _city_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _city_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _temperature
     (setq _temperature (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _humidity
     (setq _humidity (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _description
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _description (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass weather_info::Weather
  :super ros::object
  :slots ())

(setf (get weather_info::Weather :md5sum-) "07a56992612a9868fceaf6083a0c9b4c")
(setf (get weather_info::Weather :datatype-) "weather_info/Weather")
(setf (get weather_info::Weather :request) weather_info::WeatherRequest)
(setf (get weather_info::Weather :response) weather_info::WeatherResponse)

(defmethod weather_info::WeatherRequest
  (:response () (instance weather_info::WeatherResponse :init)))

(setf (get weather_info::WeatherRequest :md5sum-) "07a56992612a9868fceaf6083a0c9b4c")
(setf (get weather_info::WeatherRequest :datatype-) "weather_info/WeatherRequest")
(setf (get weather_info::WeatherRequest :definition-)
      "string city
---
string city_name
float32 temperature
float32 humidity
string description


")

(setf (get weather_info::WeatherResponse :md5sum-) "07a56992612a9868fceaf6083a0c9b4c")
(setf (get weather_info::WeatherResponse :datatype-) "weather_info/WeatherResponse")
(setf (get weather_info::WeatherResponse :definition-)
      "string city
---
string city_name
float32 temperature
float32 humidity
string description


")



(provide :weather_info/Weather "07a56992612a9868fceaf6083a0c9b4c")


