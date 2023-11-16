# DpuStatusInfoOperationalInfo

Sensor information provided by DPU that provides health status. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensor_id** | **str** | This string uniquely identifies a sensor in the DPU.  | 
**health_state** | [**ElementDescription**](ElementDescription.md) |  | [optional] 
**reading** | **str** | A description of the state of the sensor such as: N watts, Y RPM, or other measurement.  | 
**units** | **str** | If provided by underying API, the base units in which the sensor reading is specified, \&quot;RPM\&quot;, \&quot;WATTS\&quot; and so forth.  | [optional] 
**time_stamp** | **datetime** | Reports the ISO 8601 Timestamp when this sensor was last updated by management controller if the this sensor is capable of tracking when it was last updated.  Property timeStampRaw, which comes from vendor firmware is convertible to DateTime, it will be provided.  | [optional] 

## Example

```python
from vmware_vi.models.dpu_status_info_operational_info import DpuStatusInfoOperationalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DpuStatusInfoOperationalInfo from a JSON string
dpu_status_info_operational_info_instance = DpuStatusInfoOperationalInfo.from_json(json)
# print the JSON string representation of the object
print DpuStatusInfoOperationalInfo.to_json()

# convert the object into a dict
dpu_status_info_operational_info_dict = dpu_status_info_operational_info_instance.to_dict()
# create an instance of DpuStatusInfoOperationalInfo from a dict
dpu_status_info_operational_info_form_dict = dpu_status_info_operational_info.from_dict(dpu_status_info_operational_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


