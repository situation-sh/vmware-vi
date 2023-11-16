# HostSystemPowerState

A boxed *HostSystemPowerState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostSystemPowerStateEnum**](HostSystemPowerStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_system_power_state import HostSystemPowerState

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemPowerState from a JSON string
host_system_power_state_instance = HostSystemPowerState.from_json(json)
# print the JSON string representation of the object
print HostSystemPowerState.to_json()

# convert the object into a dict
host_system_power_state_dict = host_system_power_state_instance.to_dict()
# create an instance of HostSystemPowerState from a dict
host_system_power_state_form_dict = host_system_power_state.from_dict(host_system_power_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


