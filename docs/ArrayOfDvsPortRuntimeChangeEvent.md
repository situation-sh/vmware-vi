# ArrayOfDvsPortRuntimeChangeEvent

A boxed array of *DvsPortRuntimeChangeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsPortRuntimeChangeEvent]**](DvsPortRuntimeChangeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_port_runtime_change_event import ArrayOfDvsPortRuntimeChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsPortRuntimeChangeEvent from a JSON string
array_of_dvs_port_runtime_change_event_instance = ArrayOfDvsPortRuntimeChangeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsPortRuntimeChangeEvent.to_json()

# convert the object into a dict
array_of_dvs_port_runtime_change_event_dict = array_of_dvs_port_runtime_change_event_instance.to_dict()
# create an instance of ArrayOfDvsPortRuntimeChangeEvent from a dict
array_of_dvs_port_runtime_change_event_form_dict = array_of_dvs_port_runtime_change_event.from_dict(array_of_dvs_port_runtime_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


