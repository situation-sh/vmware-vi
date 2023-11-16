# RemoveCustomFieldDefRequestType

The parameters of *CustomFieldsManager.RemoveCustomFieldDef*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | The unique key for the field definition.  | 

## Example

```python
from vmware_vi.models.remove_custom_field_def_request_type import RemoveCustomFieldDefRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCustomFieldDefRequestType from a JSON string
remove_custom_field_def_request_type_instance = RemoveCustomFieldDefRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveCustomFieldDefRequestType.to_json()

# convert the object into a dict
remove_custom_field_def_request_type_dict = remove_custom_field_def_request_type_instance.to_dict()
# create an instance of RemoveCustomFieldDefRequestType from a dict
remove_custom_field_def_request_type_form_dict = remove_custom_field_def_request_type.from_dict(remove_custom_field_def_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


