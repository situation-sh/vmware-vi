# GuestOperationsUnavailable

A GuestOperationsUnavailable exception is thrown when an operation fails to contact the guest operations agent running inside the virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_operations_unavailable import GuestOperationsUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of GuestOperationsUnavailable from a JSON string
guest_operations_unavailable_instance = GuestOperationsUnavailable.from_json(json)
# print the JSON string representation of the object
print GuestOperationsUnavailable.to_json()

# convert the object into a dict
guest_operations_unavailable_dict = guest_operations_unavailable_instance.to_dict()
# create an instance of GuestOperationsUnavailable from a dict
guest_operations_unavailable_form_dict = guest_operations_unavailable.from_dict(guest_operations_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


