# ArrayOfPowerSystemInfo

A boxed array of *PowerSystemInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PowerSystemInfo]**](PowerSystemInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_power_system_info import ArrayOfPowerSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPowerSystemInfo from a JSON string
array_of_power_system_info_instance = ArrayOfPowerSystemInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfPowerSystemInfo.to_json()

# convert the object into a dict
array_of_power_system_info_dict = array_of_power_system_info_instance.to_dict()
# create an instance of ArrayOfPowerSystemInfo from a dict
array_of_power_system_info_form_dict = array_of_power_system_info.from_dict(array_of_power_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


