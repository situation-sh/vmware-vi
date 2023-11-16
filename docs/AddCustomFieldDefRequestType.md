# AddCustomFieldDefRequestType

The parameters of *CustomFieldsManager.AddCustomFieldDef*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field.  | 
**mo_type** | **str** | The managed object type to which this field will apply  | [optional] 
**field_def_policy** | [**PrivilegePolicyDef**](PrivilegePolicyDef.md) |  | [optional] 
**field_policy** | [**PrivilegePolicyDef**](PrivilegePolicyDef.md) |  | [optional] 

## Example

```python
from vmware_vi.models.add_custom_field_def_request_type import AddCustomFieldDefRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomFieldDefRequestType from a JSON string
add_custom_field_def_request_type_instance = AddCustomFieldDefRequestType.from_json(json)
# print the JSON string representation of the object
print AddCustomFieldDefRequestType.to_json()

# convert the object into a dict
add_custom_field_def_request_type_dict = add_custom_field_def_request_type_instance.to_dict()
# create an instance of AddCustomFieldDefRequestType from a dict
add_custom_field_def_request_type_form_dict = add_custom_field_def_request_type.from_dict(add_custom_field_def_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


