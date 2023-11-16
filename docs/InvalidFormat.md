# InvalidFormat

Throws when an invalid format is detected.  For example, when a virtual machine is registered and the system is unable to parse the files as a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_format import InvalidFormat

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidFormat from a JSON string
invalid_format_instance = InvalidFormat.from_json(json)
# print the JSON string representation of the object
print InvalidFormat.to_json()

# convert the object into a dict
invalid_format_dict = invalid_format_instance.to_dict()
# create an instance of InvalidFormat from a dict
invalid_format_form_dict = invalid_format.from_dict(invalid_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


