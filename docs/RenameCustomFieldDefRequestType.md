# RenameCustomFieldDefRequestType

The parameters of *CustomFieldsManager.RenameCustomFieldDef*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | The unique key for the field definition.  | 
**name** | **str** | The new name for the field.  | 

## Example

```python
from vmware_vi.models.rename_custom_field_def_request_type import RenameCustomFieldDefRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RenameCustomFieldDefRequestType from a JSON string
rename_custom_field_def_request_type_instance = RenameCustomFieldDefRequestType.from_json(json)
# print the JSON string representation of the object
print RenameCustomFieldDefRequestType.to_json()

# convert the object into a dict
rename_custom_field_def_request_type_dict = rename_custom_field_def_request_type_instance.to_dict()
# create an instance of RenameCustomFieldDefRequestType from a dict
rename_custom_field_def_request_type_form_dict = rename_custom_field_def_request_type.from_dict(rename_custom_field_def_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


