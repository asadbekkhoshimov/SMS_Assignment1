
(cl:in-package :asdf)

(defsystem "weather_info-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Weather" :depends-on ("_package_Weather"))
    (:file "_package_Weather" :depends-on ("_package"))
  ))