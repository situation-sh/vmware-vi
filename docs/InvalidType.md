# InvalidType

InvalidType is thrown when a managed object request refers to an unexpected or unknown type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **str** | Name of the argument that was malformed.  | [optional] 

## Example

```python
from vmware_vi.models.invalid_type import InvalidType

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidType from a JSON string
invalid_type_instance = InvalidType.from_json(json)
# print the JSON string representation of the object
print InvalidType.to_json()

# convert the object into a dict
invalid_type_dict = invalid_type_instance.to_dict()
# create an instance of InvalidType from a dict
invalid_type_form_dict = invalid_type.from_dict(invalid_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


