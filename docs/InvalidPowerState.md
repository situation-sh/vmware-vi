# InvalidPowerState

This exception is thrown if the power operation attempted could not be performed given the current power state of the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | [optional] 
**existing_state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.invalid_power_state import InvalidPowerState

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPowerState from a JSON string
invalid_power_state_instance = InvalidPowerState.from_json(json)
# print the JSON string representation of the object
print InvalidPowerState.to_json()

# convert the object into a dict
invalid_power_state_dict = invalid_power_state_instance.to_dict()
# create an instance of InvalidPowerState from a dict
invalid_power_state_form_dict = invalid_power_state.from_dict(invalid_power_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


