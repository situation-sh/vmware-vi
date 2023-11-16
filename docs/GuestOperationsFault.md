# GuestOperationsFault

The common base type for all guest operations faults.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_operations_fault import GuestOperationsFault

# TODO update the JSON string below
json = "{}"
# create an instance of GuestOperationsFault from a JSON string
guest_operations_fault_instance = GuestOperationsFault.from_json(json)
# print the JSON string representation of the object
print GuestOperationsFault.to_json()

# convert the object into a dict
guest_operations_fault_dict = guest_operations_fault_instance.to_dict()
# create an instance of GuestOperationsFault from a dict
guest_operations_fault_form_dict = guest_operations_fault.from_dict(guest_operations_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


