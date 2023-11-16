# ArrayOfHostNumericSensorInfo

A boxed array of *HostNumericSensorInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNumericSensorInfo]**](HostNumericSensorInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_numeric_sensor_info import ArrayOfHostNumericSensorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNumericSensorInfo from a JSON string
array_of_host_numeric_sensor_info_instance = ArrayOfHostNumericSensorInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNumericSensorInfo.to_json()

# convert the object into a dict
array_of_host_numeric_sensor_info_dict = array_of_host_numeric_sensor_info_instance.to_dict()
# create an instance of ArrayOfHostNumericSensorInfo from a dict
array_of_host_numeric_sensor_info_form_dict = array_of_host_numeric_sensor_info.from_dict(array_of_host_numeric_sensor_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


