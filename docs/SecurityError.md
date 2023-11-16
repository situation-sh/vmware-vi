# SecurityError

Thrown when the client is not allowed access to the property or method. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.security_error import SecurityError

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityError from a JSON string
security_error_instance = SecurityError.from_json(json)
# print the JSON string representation of the object
print SecurityError.to_json()

# convert the object into a dict
security_error_dict = security_error_instance.to_dict()
# create an instance of SecurityError from a dict
security_error_form_dict = security_error.from_dict(security_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


