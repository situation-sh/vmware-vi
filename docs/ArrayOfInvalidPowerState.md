# ArrayOfInvalidPowerState

A boxed array of *InvalidPowerState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidPowerState]**](InvalidPowerState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_power_state import ArrayOfInvalidPowerState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidPowerState from a JSON string
array_of_invalid_power_state_instance = ArrayOfInvalidPowerState.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidPowerState.to_json()

# convert the object into a dict
array_of_invalid_power_state_dict = array_of_invalid_power_state_instance.to_dict()
# create an instance of ArrayOfInvalidPowerState from a dict
array_of_invalid_power_state_form_dict = array_of_invalid_power_state.from_dict(array_of_invalid_power_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


