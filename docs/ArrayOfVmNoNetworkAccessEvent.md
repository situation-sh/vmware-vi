# ArrayOfVmNoNetworkAccessEvent

A boxed array of *VmNoNetworkAccessEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmNoNetworkAccessEvent]**](VmNoNetworkAccessEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_no_network_access_event import ArrayOfVmNoNetworkAccessEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmNoNetworkAccessEvent from a JSON string
array_of_vm_no_network_access_event_instance = ArrayOfVmNoNetworkAccessEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmNoNetworkAccessEvent.to_json()

# convert the object into a dict
array_of_vm_no_network_access_event_dict = array_of_vm_no_network_access_event_instance.to_dict()
# create an instance of ArrayOfVmNoNetworkAccessEvent from a dict
array_of_vm_no_network_access_event_form_dict = array_of_vm_no_network_access_event.from_dict(array_of_vm_no_network_access_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


