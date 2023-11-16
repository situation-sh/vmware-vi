# RenameCustomizationSpecRequestType

The parameters of *CustomizationSpecManager.RenameCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**new_name** | **str** |  | 

## Example

```python
from vmware_vi.models.rename_customization_spec_request_type import RenameCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RenameCustomizationSpecRequestType from a JSON string
rename_customization_spec_request_type_instance = RenameCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print RenameCustomizationSpecRequestType.to_json()

# convert the object into a dict
rename_customization_spec_request_type_dict = rename_customization_spec_request_type_instance.to_dict()
# create an instance of RenameCustomizationSpecRequestType from a dict
rename_customization_spec_request_type_form_dict = rename_customization_spec_request_type.from_dict(rename_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


