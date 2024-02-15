"""Defines devices, entity types, supported entities per device and per version."""

CTS602_DEVICE_TYPES = {
    2: "Comfort light",
    4: "VPL 15c",
    10: "CompactS",
    12: "VP18cCom",
    13: "COMFORT",
    19: "VP 18c",
    20: "VP 18ek",
    21: "VP 18cek",
    25: "VPL 25c",
    31: "COMFORTn",
    33: "COMBI 300 N",
    35: "COMBI 302",
    36: "COMBI 302 T",
    38: "VGU180 ek",
    44: "CompactP",
}

CTS602_ENTITY_MAP = {
    "get_bus_version": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_controller_software_version": {
        "entity_type": "config",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_controller_hardware_version": {
        "entity_type": "config",
        "min_bus_version": 21,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_user_function_1_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 2,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_smoke_alarm_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_user_function_2_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 2,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_t0_controller_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_t1_intake_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_t2_inlet_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_t3_exhaust_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            13,
            31,
        ),
    },
    "get_t4_outlet": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            10,
            12,
            13,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_t5_condenser_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_t6_evaporator_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_t7_inlet_temperature_after_heater": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_t8_outdoor_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            13,
            31,
        ),
    },
    "get_t9_heater_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_t10_external_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_t11_electric_water_heater_temperature": {
        "entity_type": "water_heater",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_t12_compressor_water_heater_temperature": {
        "entity_type": "water_heater",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_t13_return_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (38,),
    },
    "get_t14_supply_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            38,
            44,
        ),
    },
    "get_t15_user_panel_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_t16_sacrificial_anode_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_humidity": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_co2_sensor_value": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "extra_type": "co2",
        "supported_devices": ("all",),
    },
    "get_alarm_count": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "alarm_reset": {
        "entity_type": "select",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_control_state": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_time_in_control_state": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_actual_vent_set": {
        "entity_type": "sensor",
        "min_bus_version": 9,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_supply_fan_level": {
        "entity_type": "sensor",
        "min_bus_version": 9,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_return_fan_level": {
        "entity_type": "sensor",
        "min_bus_version": 9,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_days_since_air_filter_change": {
        "entity_type": "sensor",
        "min_bus_version": 9,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_days_to_air_filter_change": {
        "entity_type": "sensor",
        "min_bus_version": 9,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_summer_state": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_control_temperature": {
        "entity_type": "climate",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_room_master_temperature": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_exchanger_efficiency": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_hps_alarm_count": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_anode_state": {
        "entity_type": "sensor",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
        ),
    },
    "get_central_heating_setpoint": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            38,
            44,
        ),
    },
    "get_hps_t17_supply_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_hps_t16_return_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_hps_t22_shw_bottom_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_hps_t20_ambient_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_hps_output_compvolt1": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_hps_heat_pump_state": {
        "entity_type": "sensor",
        "min_hps_bus_version": 1,
        "supported_devices": (44,),
    },
    "get_display_led_1_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "max_bus_version": 19,
        "supported_devices": ("all",),
    },
    "get_display_led_2_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "max_bus_version": 19,
        "supported_devices": ("all",),
    },
    "get_display_text_1": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "max_bus_version": 19,
        "supported_devices": ("all",),
    },
    "get_display_text_2": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "max_bus_version": 19,
        "supported_devices": ("all",),
    },
    "get_bypass_flap_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            10,
            13,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_after_heating_element_capacity": {
        "entity_type": "sensor",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_co2_present": {
        "entity_type": "config",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_average_humidity": {
        "entity_type": "sensor",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_ventilation_state": {
        "entity_type": "sensor",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_hps_t21_shw_top_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
    "get_hps_t18_tank_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
    "get_hps_t35_pressure_pipe_temperature": {
        "entity_type": "sensor",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
    "get_hps_compressor_capacity": {
        "entity_type": "sensor",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
    "get_compressor_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_electric_water_heater_state": {
        "entity_type": "water_heater",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_circulation_pump_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            38,
            44,
        ),
    },
    "get_heater_relay_1_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            44,
        ),
    },
    "get_heater_relay_2_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            44,
        ),
    },
    "get_heater_relay_3_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            44,
        ),
    },
    "get_defrost_state": {
        "entity_type": "binary_sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_return_fan_speed": {
        "entity_type": "sensor",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_supply_fan_speed": {
        "entity_type": "sensor",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_time": {
        "entity_type": "sensor",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "set_time": {
        "entity_type": "button",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_machine_type": {
        "entity_type": "config",
        "min_bus_version": 3,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_run_state": {
        "entity_type": "climate",
        "min_bus_version": 3,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_operation_mode": {
        "entity_type": "climate",
        "min_bus_version": 3,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_ventilation_step": {
        "entity_type": "climate",
        "min_bus_version": 3,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_user_temperature_setpoint": {
        "entity_type": "climate",
        "min_bus_version": 3,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_air_exchange_mode": {
        "entity_type": "climate",
        "min_bus_version": 1,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            44,
        ),
    },
    "get_cooling_mode_ventilation_step": {
        "entity_type": "select",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            21,
            25,
            33,
            35,
            36,
            44,
        ),
    },
    "get_air_filter_alarm_interval": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_cooling_setpoint": {
        "entity_type": "select",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            12,
            19,
            21,
            25,
            33,
            35,
            36,
            44,
        ),
    },
    "get_min_supply_air_summer_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_min_supply_air_winter_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_max_supply_air_summer_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            13,
            19,
            20,
            21,
            25,
            31,
            44,
        ),
    },
    "get_max_supply_air_winter_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            13,
            19,
            20,
            21,
            25,
            31,
            44,
        ),
    },
    "get_summer_state_change_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_air_heat_select": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            44,
        ),
    },
    "get_low_temperature_curve": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            38,
            44,
        ),
    },
    "get_high_temperature_curve": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            38,
            44,
        ),
    },
    "get_low_temperature_compressor_start_setpoint": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            4,
            10,
            12,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_compressor_stop_time": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_electric_water_heater_setpoint": {
        "entity_type": "water_heater",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_compressor_water_heater_setpoint": {
        "entity_type": "water_heater",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_compressor_priority": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            19,
            20,
            21,
            44,
        ),
    },
    "get_scalding_protection_setpoint": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            12,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_legionella_day": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            10,
            19,
            20,
            21,
            38,
            44,
        ),
    },
    "get_external_heating_offset": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_central_heat_select": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            12,
            20,
            21,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_ch_min_supply_temperature": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            12,
            20,
            21,
            38,
            44,
        ),
    },
    "get_ch_max_supply_temperature": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            12,
            20,
            21,
            38,
            44,
        ),
    },
    "get_central_heat_supply_curve_offset": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            12,
            20,
            21,
            38,
            44,
        ),
    },
    "get_central_heat_supply_curve": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            12,
            20,
            21,
            38,
            44,
        ),
    },
    "get_circulation_pump_mode": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            20,
            21,
            38,
            44,
        ),
    },
    "get_central_heat_type": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            20,
            21,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_supply_heating_pid_time": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            20,
            21,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_hps_water_heater_setpoint": {
        "entity_type": "number",
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_low_humidity_step": {
        "entity_type": "select",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_high_humidity_step": {
        "entity_type": "select",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_user_humidity_setpoint": {
        "entity_type": "climate",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_max_high_humidity_vent_time": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_co2_ventilation_high_step": {
        "entity_type": "select",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "extra_type": "co2",
        "supported_devices": ("all",),
    },
    "get_co2_low_limit_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "extra_type": "co2",
        "supported_devices": ("all",),
    },
    "get_co2_high_limit_setpoint": {
        "entity_type": "number",
        "min_bus_version": 4,
        "min_hps_bus_version": 1,
        "extra_type": "co2",
        "supported_devices": ("all",),
    },
    "set_display_button": {
        "entity_type": "button",
        "min_bus_version": 1,
        "max_bus_version": 19,
        "supported_devices": (None,),
    },
    "get_user_menu_state": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_hmi_language": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": ("all",),
    },
    "get_low_outdoor_temperature_setpoint": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_low_outdoor_temperature_ventilation_step": {
        "entity_type": "select",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_after_heating_type": {
        "entity_type": "sensor",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_supply_heater_delay": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            12,
            13,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_low_room_temperature_setpoint": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_supply_air_after_heating": {
        "entity_type": "switch",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (None,),
    },
    "get_min_supply_step": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_min_return_step": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": ("all",),
    },
    "get_max_return_step": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "excluded_bus_versions": (
            20,
            21,
        ),
        "supported_devices": ("all",),
    },
    "get_fan_startup_delay": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            44,
        ),
    },
    "get_defrost_ventilation_level": {
        "entity_type": "select",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            38,
            44,
        ),
    },
    "get_time_between_defrost": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            33,
            35,
            38,
            44,
        ),
    },
    "get_defrost_start_setpoint": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_defrost_stop_setpoint": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            33,
            35,
            36,
            38,
            44,
        ),
    },
    "get_maximum_compressor_defrost_time": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            33,
            35,
            44,
        ),
    },
    "get_maximum_outlet_defrost_time": {
        "entity_type": "number",
        "min_bus_version": 11,
        "min_hps_bus_version": 1,
        "supported_devices": (
            33,
            35,
            44,
        ),
    },
    "get_minimum_defrost_time": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            4,
            10,
            19,
            20,
            21,
            25,
            38,
            44,
        ),
    },
    "get_supply_power_at_level_1": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_supply_power_at_level_2": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_supply_power_at_level_3": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_supply_power_at_level_4": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            2,
            4,
            10,
            12,
            13,
            19,
            20,
            21,
            25,
            31,
            33,
            35,
            36,
            44,
        ),
    },
    "get_return_power_at_level_1": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_return_power_at_level_2": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_return_power_at_level_3": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_return_power_at_level_4": {
        "entity_type": "number",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_air_quality_control_type": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": ("all",),
    },
    "get_pre_heater_defrost_select": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            33,
            35,
            36,
        ),
    },
    "get_pre_heater_temp_set": {
        "entity_type": "select",
        "min_bus_version": 19,
        "min_hps_bus_version": 1,
        "supported_devices": (
            33,
            35,
            36,
        ),
    },
    "get_hps_main_switch": {
        "entity_type": "switch",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
    "get_hps_season_mode": {
        "entity_type": "select",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
    "get_hps_heating_setpoint_min": {
        "entity_type": "number",
        "min_hps_bus_version": 2,
        "supported_devices": (44,),
    },
}
