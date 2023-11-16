# OperationDisabledByGuest

An OperationDisabledByGuest exception is thrown when an operation fails because the guest operations agent has been configured to disable the operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.operation_disabled_by_guest import OperationDisabledByGuest

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDisabledByGuest from a JSON string
operation_disabled_by_guest_instance = OperationDisabledByGuest.from_json(json)
# print the JSON string representation of the object
print OperationDisabledByGuest.to_json()

# convert the object into a dict
operation_disabled_by_guest_dict = operation_disabled_by_guest_instance.to_dict()
# create an instance of OperationDisabledByGuest from a dict
operation_disabled_by_guest_form_dict = operation_disabled_by_guest.from_dict(operation_disabled_by_guest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


