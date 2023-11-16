# CustomFieldDef

Describes a custom field. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A unique ID used to reference this custom field in assignments.  This ID is unique for the lifetime of the field (even across rename operations).  | 
**name** | **str** | Name of the field.  | 
**type** | **str** | Type of the field.  | 
**managed_object_type** | **str** | Type of object for which the field is valid.  If not specified, the field is valid for all managed objects.  ***Since:*** VI API 2.5  | [optional] 
**field_def_privileges** | [**PrivilegePolicyDef**](PrivilegePolicyDef.md) |  | [optional] 
**field_instance_privileges** | [**PrivilegePolicyDef**](PrivilegePolicyDef.md) |  | [optional] 

## Example

```python
from vmware_vi.models.custom_field_def import CustomFieldDef

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDef from a JSON string
custom_field_def_instance = CustomFieldDef.from_json(json)
# print the JSON string representation of the object
print CustomFieldDef.to_json()

# convert the object into a dict
custom_field_def_dict = custom_field_def_instance.to_dict()
# create an instance of CustomFieldDef from a dict
custom_field_def_form_dict = custom_field_def.from_dict(custom_field_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


