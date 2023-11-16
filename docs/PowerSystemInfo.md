# PowerSystemInfo

Power System Info data object.  Shows current state of power management system.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_policy** | [**HostPowerPolicy**](HostPowerPolicy.md) |  | 

## Example

```python
from vmware_vi.models.power_system_info import PowerSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PowerSystemInfo from a JSON string
power_system_info_instance = PowerSystemInfo.from_json(json)
# print the JSON string representation of the object
print PowerSystemInfo.to_json()

# convert the object into a dict
power_system_info_dict = power_system_info_instance.to_dict()
# create an instance of PowerSystemInfo from a dict
power_system_info_form_dict = power_system_info.from_dict(power_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


