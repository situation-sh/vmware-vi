# SystemError

Exception type for reporting a low-level operating system error. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | A message to indicate detailed information about the error.  This property is not internationalization friendly and normally reported by the underlying operating system.  | 

## Example

```python
from vmware_vi.models.system_error import SystemError

# TODO update the JSON string below
json = "{}"
# create an instance of SystemError from a JSON string
system_error_instance = SystemError.from_json(json)
# print the JSON string representation of the object
print SystemError.to_json()

# convert the object into a dict
system_error_dict = system_error_instance.to_dict()
# create an instance of SystemError from a dict
system_error_form_dict = system_error.from_dict(system_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


