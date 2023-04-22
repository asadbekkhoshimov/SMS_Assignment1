
(cl:in-package :asdf)

(defsystem "my_city-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :my_city-msg
)
  :components ((:file "_package")
    (:file "WeatherService" :depends-on ("_package_WeatherService"))
    (:file "_package_WeatherService" :depends-on ("_package"))
  ))