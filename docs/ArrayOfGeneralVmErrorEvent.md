# ArrayOfGeneralVmErrorEvent

A boxed array of *GeneralVmErrorEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralVmErrorEvent]**](GeneralVmErrorEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_general_vm_error_event import ArrayOfGeneralVmErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGeneralVmErrorEvent from a JSON string
array_of_general_vm_error_event_instance = ArrayOfGeneralVmErrorEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfGeneralVmErrorEvent.to_json()

# convert the object into a dict
array_of_general_vm_error_event_dict = array_of_general_vm_error_event_instance.to_dict()
# create an instance of ArrayOfGeneralVmErrorEvent from a dict
array_of_general_vm_error_event_form_dict = array_of_general_vm_error_event.from_dict(array_of_general_vm_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


