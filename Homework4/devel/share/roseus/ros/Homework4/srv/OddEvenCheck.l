;; Auto-generated. Do not edit!


(when (boundp 'Homework4::OddEvenCheck)
  (if (not (find-package "HOMEWORK4"))
    (make-package "HOMEWORK4"))
  (shadow 'OddEvenCheck (find-package "HOMEWORK4")))
(unless (find-package "HOMEWORK4::ODDEVENCHECK")
  (make-package "HOMEWORK4::ODDEVENCHECK"))
(unless (find-package "HOMEWORK4::ODDEVENCHECKREQUEST")
  (make-package "HOMEWORK4::ODDEVENCHECKREQUEST"))
(unless (find-package "HOMEWORK4::ODDEVENCHECKRESPONSE")
  (make-package "HOMEWORK4::ODDEVENCHECKRESPONSE"))

(in-package "ROS")





(defclass Homework4::OddEvenCheckRequest
  :super ros::object
  :slots (_number ))

(defmethod Homework4::OddEvenCheckRequest
  (:init
   (&key
    ((:number __number) 0)
    )
   (send-super :init)
   (setq _number (round __number))
   self)
  (:number
   (&optional __number)
   (if __number (setq _number __number)) _number)
  (:serialization-length
   ()
   (+
    ;; int32 _number
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _number
       (write-long _number s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _number
     (setq _number (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass Homework4::OddEvenCheckResponse
  :super ros::object
  :slots (_answer ))

(defmethod Homework4::OddEvenCheckResponse
  (:init
   (&key
    ((:answer __answer) "")
    )
   (send-super :init)
   (setq _answer (string __answer))
   self)
  (:answer
   (&optional __answer)
   (if __answer (setq _answer __answer)) _answer)
  (:serialization-length
   ()
   (+
    ;; string _answer
    4 (length _answer)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _answer
       (write-long (length _answer) s) (princ _answer s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _answer
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _answer (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass Homework4::OddEvenCheck
  :super ros::object
  :slots ())

(setf (get Homework4::OddEvenCheck :md5sum-) "4ff0b0ab1ed04611e3a2b4090af9ee4f")
(setf (get Homework4::OddEvenCheck :datatype-) "Homework4/OddEvenCheck")
(setf (get Homework4::OddEvenCheck :request) Homework4::OddEvenCheckRequest)
(setf (get Homework4::OddEvenCheck :response) Homework4::OddEvenCheckResponse)

(defmethod Homework4::OddEvenCheckRequest
  (:response () (instance Homework4::OddEvenCheckResponse :init)))

(setf (get Homework4::OddEvenCheckRequest :md5sum-) "4ff0b0ab1ed04611e3a2b4090af9ee4f")
(setf (get Homework4::OddEvenCheckRequest :datatype-) "Homework4/OddEvenCheckRequest")
(setf (get Homework4::OddEvenCheckRequest :definition-)
      "int32 number
---
string answer

")

(setf (get Homework4::OddEvenCheckResponse :md5sum-) "4ff0b0ab1ed04611e3a2b4090af9ee4f")
(setf (get Homework4::OddEvenCheckResponse :datatype-) "Homework4/OddEvenCheckResponse")
(setf (get Homework4::OddEvenCheckResponse :definition-)
      "int32 number
---
string answer

")



(provide :Homework4/OddEvenCheck "4ff0b0ab1ed04611e3a2b4090af9ee4f")


