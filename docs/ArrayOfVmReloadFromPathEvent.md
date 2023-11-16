# ArrayOfVmReloadFromPathEvent

A boxed array of *VmReloadFromPathEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmReloadFromPathEvent]**](VmReloadFromPathEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_reload_from_path_event import ArrayOfVmReloadFromPathEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmReloadFromPathEvent from a JSON string
array_of_vm_reload_from_path_event_instance = ArrayOfVmReloadFromPathEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmReloadFromPathEvent.to_json()

# convert the object into a dict
array_of_vm_reload_from_path_event_dict = array_of_vm_reload_from_path_event_instance.to_dict()
# create an instance of ArrayOfVmReloadFromPathEvent from a dict
array_of_vm_reload_from_path_event_form_dict = array_of_vm_reload_from_path_event.from_dict(array_of_vm_reload_from_path_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


