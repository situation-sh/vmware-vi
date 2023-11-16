# ArrayOfVmDateRolledBackEvent

A boxed array of *VmDateRolledBackEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDateRolledBackEvent]**](VmDateRolledBackEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_date_rolled_back_event import ArrayOfVmDateRolledBackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDateRolledBackEvent from a JSON string
array_of_vm_date_rolled_back_event_instance = ArrayOfVmDateRolledBackEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDateRolledBackEvent.to_json()

# convert the object into a dict
array_of_vm_date_rolled_back_event_dict = array_of_vm_date_rolled_back_event_instance.to_dict()
# create an instance of ArrayOfVmDateRolledBackEvent from a dict
array_of_vm_date_rolled_back_event_form_dict = array_of_vm_date_rolled_back_event.from_dict(array_of_vm_date_rolled_back_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


