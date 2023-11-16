# ArrayOfAutoStartPowerInfo

A boxed array of *AutoStartPowerInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AutoStartPowerInfo]**](AutoStartPowerInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_auto_start_power_info import ArrayOfAutoStartPowerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAutoStartPowerInfo from a JSON string
array_of_auto_start_power_info_instance = ArrayOfAutoStartPowerInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfAutoStartPowerInfo.to_json()

# convert the object into a dict
array_of_auto_start_power_info_dict = array_of_auto_start_power_info_instance.to_dict()
# create an instance of ArrayOfAutoStartPowerInfo from a dict
array_of_auto_start_power_info_form_dict = array_of_auto_start_power_info.from_dict(array_of_auto_start_power_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


