// Auto-generated. Do not edit!

// (in-package weather_info.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class WeatherRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.city = null;
    }
    else {
      if (initObj.hasOwnProperty('city')) {
        this.city = initObj.city
      }
      else {
        this.city = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WeatherRequest
    // Serialize message field [city]
    bufferOffset = _serializer.string(obj.city, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WeatherRequest
    let len;
    let data = new WeatherRequest(null);
    // Deserialize message field [city]
    data.city = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.city);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'weather_info/WeatherRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6ca7c9808e023a3417491b7104889ca1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string city
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WeatherRequest(null);
    if (msg.city !== undefined) {
      resolved.city = msg.city;
    }
    else {
      resolved.city = ''
    }

    return resolved;
    }
};

class WeatherResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.city_name = null;
      this.temperature = null;
      this.humidity = null;
      this.description = null;
    }
    else {
      if (initObj.hasOwnProperty('city_name')) {
        this.city_name = initObj.city_name
      }
      else {
        this.city_name = '';
      }
      if (initObj.hasOwnProperty('temperature')) {
        this.temperature = initObj.temperature
      }
      else {
        this.temperature = 0.0;
      }
      if (initObj.hasOwnProperty('humidity')) {
        this.humidity = initObj.humidity
      }
      else {
        this.humidity = 0.0;
      }
      if (initObj.hasOwnProperty('description')) {
        this.description = initObj.description
      }
      else {
        this.description = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WeatherResponse
    // Serialize message field [city_name]
    bufferOffset = _serializer.string(obj.city_name, buffer, bufferOffset);
    // Serialize message field [temperature]
    bufferOffset = _serializer.float32(obj.temperature, buffer, bufferOffset);
    // Serialize message field [humidity]
    bufferOffset = _serializer.float32(obj.humidity, buffer, bufferOffset);
    // Serialize message field [description]
    bufferOffset = _serializer.string(obj.description, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WeatherResponse
    let len;
    let data = new WeatherResponse(null);
    // Deserialize message field [city_name]
    data.city_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [temperature]
    data.temperature = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [humidity]
    data.humidity = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [description]
    data.description = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.city_name);
    length += _getByteLength(object.description);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'weather_info/WeatherResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '182114dcdb307da4818df3386abb39b9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string city_name
    float32 temperature
    float32 humidity
    string description
    
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WeatherResponse(null);
    if (msg.city_name !== undefined) {
      resolved.city_name = msg.city_name;
    }
    else {
      resolved.city_name = ''
    }

    if (msg.temperature !== undefined) {
      resolved.temperature = msg.temperature;
    }
    else {
      resolved.temperature = 0.0
    }

    if (msg.humidity !== undefined) {
      resolved.humidity = msg.humidity;
    }
    else {
      resolved.humidity = 0.0
    }

    if (msg.description !== undefined) {
      resolved.description = msg.description;
    }
    else {
      resolved.description = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: WeatherRequest,
  Response: WeatherResponse,
  md5sum() { return '07a56992612a9868fceaf6083a0c9b4c'; },
  datatype() { return 'weather_info/Weather'; }
};
