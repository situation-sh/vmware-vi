# HostNumericSensorInfo

Base class for numeric sensor information.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the physical element associated with the sensor It consists of a string of the form: \&quot;description --- state/identifer\&quot;.  ***Since:*** VI API 2.5  | 
**health_state** | [**ElementDescription**](ElementDescription.md) |  | [optional] 
**current_reading** | **int** | The current reading of the element indicated by the sensor.  The actual sensor reading is obtained by multiplying the current reading by the scale factor.  ***Since:*** VI API 2.5  | 
**unit_modifier** | **int** | The unit multiplier for the values returned by the sensor.  All values returned by the sensor are current reading \\* 10 raised to the power of the UnitModifier. If no unitModifier applies the value returned is 0.  ***Since:*** VI API 2.5  | 
**base_units** | **str** | The base units in which the sensor reading is specified.  If rateUnits is set the units of the current reading is further qualified by the rateUnits. Otherwise the value returned is &#39;unspecified&#39;.  See also *HostNumericSensorInfo.rateUnits*.  ***Since:*** VI API 2.5  | 
**rate_units** | **str** | The rate units in which the sensor reading is specified.  For example if the baseUnits is Volts and the rateUnits is per second the value returned by the sensor are in Volts/second. If no rate applies the value returned is &#39;none&#39;.  ***Since:*** VI API 2.5  | [optional] 
**sensor_type** | **str** | The type of the sensor.  If the sensor type is set to Other the sensor name can be used to further identify the type of sensor. The sensor units can also be used to further implicitly determine the type of the sensor.  See also *HostNumericSensorType_enum*.  ***Since:*** VI API 2.5  | 
**id** | **str** | A unique sensor identifier.  A four part value consisting of: BMC device.Entity ID.Instance.SensorNumber Can be used to match a NumericSensorInfo object to esxcli hardware ipmi sdr list  ***Since:*** vSphere API 6.5  | [optional] 
**sensor_number** | **int** | The IPMI Sensor/probe that is reporting this event.  Use this value to locate System Event Log (SEL) entries for this Sensor. It is also reported in &#39;id&#39; in string format. This property is intended to be used with vim.host.SystemEventInfo.sensorNumber  | [optional] 
**time_stamp** | **str** | Reports the ISO 8601 Timestamp when this sensor was last updated by management controller if the this sensor is capable of tracking when it was last updated.  ***Since:*** vSphere API 6.5  | [optional] 
**fru** | [**HostFru**](HostFru.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_numeric_sensor_info import HostNumericSensorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostNumericSensorInfo from a JSON string
host_numeric_sensor_info_instance = HostNumericSensorInfo.from_json(json)
# print the JSON string representation of the object
print HostNumericSensorInfo.to_json()

# convert the object into a dict
host_numeric_sensor_info_dict = host_numeric_sensor_info_instance.to_dict()
# create an instance of HostNumericSensorInfo from a dict
host_numeric_sensor_info_form_dict = host_numeric_sensor_info.from_dict(host_numeric_sensor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


