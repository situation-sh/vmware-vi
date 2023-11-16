# ArrayOfCustomFieldDef

A boxed array of *CustomFieldDef*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldDef]**](CustomFieldDef.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_def import ArrayOfCustomFieldDef

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldDef from a JSON string
array_of_custom_field_def_instance = ArrayOfCustomFieldDef.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldDef.to_json()

# convert the object into a dict
array_of_custom_field_def_dict = array_of_custom_field_def_instance.to_dict()
# create an instance of ArrayOfCustomFieldDef from a dict
array_of_custom_field_def_form_dict = array_of_custom_field_def.from_dict(array_of_custom_field_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


