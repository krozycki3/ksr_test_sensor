#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace ksr_test_sensor {

class KsrTestSensor : public Component, public sensor::Sensor {
 public:
  void setup() override;
  void loop() override;
};

}  // namespace ksr_test_sensor
}  // namespace esphome
