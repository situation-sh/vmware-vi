# InvalidName

A InvalidName fault is thrown when the name contains an invalid character or format. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The invalid name.  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.invalid_name import InvalidName

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidName from a JSON string
invalid_name_instance = InvalidName.from_json(json)
# print the JSON string representation of the object
print InvalidName.to_json()

# convert the object into a dict
invalid_name_dict = invalid_name_instance.to_dict()
# create an instance of InvalidName from a dict
invalid_name_form_dict = invalid_name.from_dict(invalid_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


