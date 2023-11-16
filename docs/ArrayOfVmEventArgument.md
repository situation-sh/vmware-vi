# ArrayOfVmEventArgument

A boxed array of *VmEventArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmEventArgument]**](VmEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_event_argument import ArrayOfVmEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmEventArgument from a JSON string
array_of_vm_event_argument_instance = ArrayOfVmEventArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmEventArgument.to_json()

# convert the object into a dict
array_of_vm_event_argument_dict = array_of_vm_event_argument_instance.to_dict()
# create an instance of ArrayOfVmEventArgument from a dict
array_of_vm_event_argument_form_dict = array_of_vm_event_argument.from_dict(array_of_vm_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


