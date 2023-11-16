# ArrayOfGeneralVmInfoEvent

A boxed array of *GeneralVmInfoEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralVmInfoEvent]**](GeneralVmInfoEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_general_vm_info_event import ArrayOfGeneralVmInfoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGeneralVmInfoEvent from a JSON string
array_of_general_vm_info_event_instance = ArrayOfGeneralVmInfoEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfGeneralVmInfoEvent.to_json()

# convert the object into a dict
array_of_general_vm_info_event_dict = array_of_general_vm_info_event_instance.to_dict()
# create an instance of ArrayOfGeneralVmInfoEvent from a dict
array_of_general_vm_info_event_form_dict = array_of_general_vm_info_event.from_dict(array_of_general_vm_info_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


