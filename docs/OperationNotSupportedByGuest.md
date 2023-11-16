# OperationNotSupportedByGuest

An OperationNotSupportedByGuest exception is thrown when an operation fails because the guest OS does not support the operation (e.g., Registry manipulation in Linux guests.).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.operation_not_supported_by_guest import OperationNotSupportedByGuest

# TODO update the JSON string below
json = "{}"
# create an instance of OperationNotSupportedByGuest from a JSON string
operation_not_supported_by_guest_instance = OperationNotSupportedByGuest.from_json(json)
# print the JSON string representation of the object
print OperationNotSupportedByGuest.to_json()

# convert the object into a dict
operation_not_supported_by_guest_dict = operation_not_supported_by_guest_instance.to_dict()
# create an instance of OperationNotSupportedByGuest from a dict
operation_not_supported_by_guest_form_dict = operation_not_supported_by_guest.from_dict(operation_not_supported_by_guest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


