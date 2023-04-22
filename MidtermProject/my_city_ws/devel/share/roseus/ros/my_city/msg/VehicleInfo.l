;; Auto-generated. Do not edit!


(when (boundp 'my_city::VehicleInfo)
  (if (not (find-package "MY_CITY"))
    (make-package "MY_CITY"))
  (shadow 'VehicleInfo (find-package "MY_CITY")))
(unless (find-package "MY_CITY::VEHICLEINFO")
  (make-package "MY_CITY::VEHICLEINFO"))

(in-package "ROS")
;;//! \htmlinclude VehicleInfo.msg.html


(defclass my_city::VehicleInfo
  :super ros::object
  :slots (_plate_number _speed ))

(defmethod my_city::VehicleInfo
  (:init
   (&key
    ((:plate_number __plate_number) "")
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _plate_number (string __plate_number))
   (setq _speed (float __speed))
   self)
  (:plate_number
   (&optional __plate_number)
   (if __plate_number (setq _plate_number __plate_number)) _plate_number)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; string _plate_number
    4 (length _plate_number)
    ;; float64 _speed
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _plate_number
       (write-long (length _plate_number) s) (princ _plate_number s)
     ;; float64 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _plate_number
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _plate_number (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _speed
     (setq _speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_city::VehicleInfo :md5sum-) "150932e63a69537c3aca6070ad51a55f")
(setf (get my_city::VehicleInfo :datatype-) "my_city/VehicleInfo")
(setf (get my_city::VehicleInfo :definition-)
      "string plate_number
float64 speed
")



(provide :my_city/VehicleInfo "150932e63a69537c3aca6070ad51a55f")


