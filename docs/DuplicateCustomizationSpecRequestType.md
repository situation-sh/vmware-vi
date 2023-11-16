# DuplicateCustomizationSpecRequestType

The parameters of *CustomizationSpecManager.DuplicateCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**new_name** | **str** |  | 

## Example

```python
from vmware_vi.models.duplicate_customization_spec_request_type import DuplicateCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateCustomizationSpecRequestType from a JSON string
duplicate_customization_spec_request_type_instance = DuplicateCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print DuplicateCustomizationSpecRequestType.to_json()

# convert the object into a dict
duplicate_customization_spec_request_type_dict = duplicate_customization_spec_request_type_instance.to_dict()
# create an instance of DuplicateCustomizationSpecRequestType from a dict
duplicate_customization_spec_request_type_form_dict = duplicate_customization_spec_request_type.from_dict(duplicate_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


