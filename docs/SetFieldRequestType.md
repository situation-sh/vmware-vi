# SetFieldRequestType

The parameters of *CustomFieldsManager.SetField*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**key** | **int** |  | 
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.set_field_request_type import SetFieldRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetFieldRequestType from a JSON string
set_field_request_type_instance = SetFieldRequestType.from_json(json)
# print the JSON string representation of the object
print SetFieldRequestType.to_json()

# convert the object into a dict
set_field_request_type_dict = set_field_request_type_instance.to_dict()
# create an instance of SetFieldRequestType from a dict
set_field_request_type_form_dict = set_field_request_type.from_dict(set_field_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


