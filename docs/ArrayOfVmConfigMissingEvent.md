# ArrayOfVmConfigMissingEvent

A boxed array of *VmConfigMissingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmConfigMissingEvent]**](VmConfigMissingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_config_missing_event import ArrayOfVmConfigMissingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmConfigMissingEvent from a JSON string
array_of_vm_config_missing_event_instance = ArrayOfVmConfigMissingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmConfigMissingEvent.to_json()

# convert the object into a dict
array_of_vm_config_missing_event_dict = array_of_vm_config_missing_event_instance.to_dict()
# create an instance of ArrayOfVmConfigMissingEvent from a dict
array_of_vm_config_missing_event_form_dict = array_of_vm_config_missing_event.from_dict(array_of_vm_config_missing_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


