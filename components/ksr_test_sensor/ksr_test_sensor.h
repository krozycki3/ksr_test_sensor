#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace ksr_test_sensor {

class KsrTestSensor : public PollingComponent, public sensor::Sensor {
 public:
  KsrTestSensor() : PollingComponent(60000) {}

  void setup() override;
  void update() override;
};

}  // namespace ksr_test_sensor
}  // namespace esphome
