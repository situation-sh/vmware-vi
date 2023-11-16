# ArrayOfVmDasUpdateErrorEvent

A boxed array of *VmDasUpdateErrorEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDasUpdateErrorEvent]**](VmDasUpdateErrorEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_das_update_error_event import ArrayOfVmDasUpdateErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDasUpdateErrorEvent from a JSON string
array_of_vm_das_update_error_event_instance = ArrayOfVmDasUpdateErrorEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDasUpdateErrorEvent.to_json()

# convert the object into a dict
array_of_vm_das_update_error_event_dict = array_of_vm_das_update_error_event_instance.to_dict()
# create an instance of ArrayOfVmDasUpdateErrorEvent from a dict
array_of_vm_das_update_error_event_form_dict = array_of_vm_das_update_error_event.from_dict(array_of_vm_das_update_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


