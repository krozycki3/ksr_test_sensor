# ============================================================
# IMPORTY
# ============================================================

# cg (code generation) służy do generowania kodu C++ podczas
# kompilowania konfiguracji ESPHome.
#
# W praktyce: tutaj opisujemy ESPHome, jaką klasę C++ ma utworzyć.
import esphome.codegen as cg


# cv (config validation) służy do definiowania i sprawdzania
# konfiguracji YAML naszego komponentu.
#
# Dzięki temu możemy np. powiedzieć:
# "mój komponent przyjmuje parametr update_interval".
import esphome.config_validation as cv


# Importujemy wbudowany komponent "sensor" ESPHome.
#
# Dzięki temu nasz komponent będzie mógł zachowywać się
# jak normalny sensor ESPHome i publikować wartość:
#
#     this->publish_state(...)
#
# WymAGANE dla naszego przypadku.
from esphome.components import sensor


# CONF_ID to stała ESPHome oznaczająca parametr "id:".
#
# Później używamy jej tutaj:
#
#     config[CONF_ID]
#
# żeby dostać ID naszego obiektu.
#
# WYMAGANE w obecnej wersji to_code().
from esphome.const import CONF_ID


# ============================================================
# NAMESPACE C++
# ============================================================

# Tworzymy namespace C++, w którym będzie znajdowała się
# nasza klasa.
#
# W C++ otrzymamy:
#
# namespace esphome {
# namespace ksr_test_sensor {
#
#     class KsrTestSensor { ... };
#
# }
# }
#
# "ksr_test_sensor" możesz zmienić.
#
# To jest TWOJA nazwa przestrzeni nazw, a nie specjalna
# nazwa wymagana przez ESPHome.
#
# Zwyczajowo dobrze jest zachować nazwę taką samą jak
# nazwa komponentu.
ksr_test_sensor_ns = cg.esphome_ns.namespace("ksr_test_sensor")


# ============================================================
# DEFINICJA KLASY C++
# ============================================================

# Tutaj informujemy ESPHome:
#
# "Chcę utworzyć klasę C++ o nazwie KsrTestSensor".
#
# Ta nazwa musi odpowiadać klasie, którą później zdefiniujesz
# w pliku:
#
#     ksr_test_sensor.h
#
# czyli:
#
#     class KsrTestSensor ...
#
# ------------------------------------------------------------
#
# cg.PollingComponent
#
# mówi ESPHome, że nasz komponent będzie miał metodę:
#
#     update()
#
# wywoływaną automatycznie w określonych odstępach czasu.
#
# To jest bardzo przydatne, jeśli później będziemy np.
# odpytwać Twój serwer.
#
# ------------------------------------------------------------
#
# sensor.Sensor
#
# mówi ESPHome, że nasza klasa jest sensorem.
#
# Dzięki temu będziemy mogli w C++ zrobić:
#
#     this->publish_state(11);
#
# ------------------------------------------------------------
#
# cg.PollingComponent oraz sensor.Sensor są tutaj istotne.
#
# Nazwę "KsrTestSensor" możesz zmienić, ale wtedy musisz
# zmienić ją również w plikach C++.
KsrTestSensor = ksr_test_sensor_ns.class_(
    "KsrTestSensor",
    cg.PollingComponent,
    sensor.Sensor,
)


# ============================================================
# SCHEMAT KONFIGURACJI YAML
# ============================================================

# CONFIG_SCHEMA opisuje, jak może wyglądać konfiguracja
# naszego komponentu w YAML.
#
# Przykładowo:
#
# sensor:
#   - platform: ksr_test_sensor
#     name: "KSR Test Sensor"
#     update_interval: 30s
#
# ESPHome sprawdzi tę konfigurację właśnie tutaj.
#
# ------------------------------------------------------------
#
# sensor.sensor_schema()
#
# pobiera standardowy schemat konfiguracji ESPHome dla sensora.
#
# Dzięki temu otrzymujemy m.in. możliwość używania typowych
# parametrów sensora, takich jak:
#
#     name:
#     id:
#     unit_of_measurement:
#     accuracy_decimals:
#     device_class:
#     state_class:
#
# Nie musisz ich definiować samodzielnie.
#
# ------------------------------------------------------------
#
# .extend(...)
#
# rozszerza istniejący schemat o nasze własne elementy.
#
# Tutaj dodajemy ID naszego obiektu C++.
CONFIG_SCHEMA = (
    sensor.sensor_schema()

    .extend(
        {
            # GenerateID() mówi:
            #
            # "jeżeli użytkownik poda id:, użyj go;
            #  jeżeli nie, wygeneruj ID automatycznie."
            #
            # To ID będzie później dostępne jako:
            #
            #     config[CONF_ID]
            #
            # oraz zostanie użyte do utworzenia obiektu C++.
            #
            # Ten fragment jest potrzebny do obecnego
            # sposobu tworzenia obiektu.
            cv.GenerateID(): cv.declare_id(KsrTestSensor),
        }
    )

    .extend(
        # Dodajemy standardową konfigurację PollingComponent.
        #
        # "10s" oznacza DOMYŚLNY interwał.
        #
        # Możesz go zmienić np. na:
        #
        #     "1s"
        #     "30s"
        #     "60s"
        #
        # Możesz też później pozwolić użytkownikowi ustawiać
        # update_interval bezpośrednio w YAML.
        #
        # Ważne: to NIE oznacza, że update() wykona się
        # dokładnie co 10 sekund z laboratoryjną dokładnością.
        # ESPHome zarządza harmonogramem komponentów.
        cv.polling_component_schema("10s")
    )
)


# ============================================================
# GENEROWANIE KODU C++
# ============================================================

# to_code() jest wywoływane przez ESPHome podczas generowania
# firmware.
#
# To tutaj konfiguracja YAML zostaje przekształcona w kod C++.
#
# "async" i "await" wynikają z mechanizmu generowania kodu
# ESPHome.
#
# Na początku nie musisz się tym szczególnie przejmować.
async def to_code(config):

    # Tworzymy obiekt naszej klasy C++.
    #
    # config[CONF_ID] zawiera ID wygenerowane przez
    # cv.GenerateID().
    #
    # W uproszczeniu:
    #
    #     var = nowy KsrTestSensor(...)
    #
    # Nie jest to dosłownie kod wykonywany tutaj na ESP32 —
    # cg.new_Pvariable() generuje odpowiedni kod C++.
    var = cg.new_Pvariable(config[CONF_ID])


    # Rejestrujemy nasz obiekt jako komponent ESPHome.
    #
    # Dzięki temu ESPHome wie, że obiekt ma cykl życia
    # komponentu, np. setup() oraz mechanizm PollingComponent.
    #
    # WYMAGANE dla naszego PollingComponent.
    await cg.register_component(var, config)


    # Rejestrujemy obiekt jako sensor.
    #
    # Dzięki temu ESPHome traktuje KsrTestSensor jako sensor
    # i może go odpowiednio obsłużyć w konfiguracji.
    #
    # WYMAGANE, jeśli chcemy używać sensor.Sensor.
    await sensor.register_sensor(var, config)
