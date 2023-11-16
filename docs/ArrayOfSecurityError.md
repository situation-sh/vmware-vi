# ArrayOfSecurityError

A boxed array of *SecurityError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SecurityError]**](SecurityError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_security_error import ArrayOfSecurityError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSecurityError from a JSON string
array_of_security_error_instance = ArrayOfSecurityError.from_json(json)
# print the JSON string representation of the object
print ArrayOfSecurityError.to_json()

# convert the object into a dict
array_of_security_error_dict = array_of_security_error_instance.to_dict()
# create an instance of ArrayOfSecurityError from a dict
array_of_security_error_form_dict = array_of_security_error.from_dict(array_of_security_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


