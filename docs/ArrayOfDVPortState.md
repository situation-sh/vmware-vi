# ArrayOfDVPortState

A boxed array of *DVPortState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVPortState]**](DVPortState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dv_port_state import ArrayOfDVPortState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVPortState from a JSON string
array_of_dv_port_state_instance = ArrayOfDVPortState.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVPortState.to_json()

# convert the object into a dict
array_of_dv_port_state_dict = array_of_dv_port_state_instance.to_dict()
# create an instance of ArrayOfDVPortState from a dict
array_of_dv_port_state_form_dict = array_of_dv_port_state.from_dict(array_of_dv_port_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


