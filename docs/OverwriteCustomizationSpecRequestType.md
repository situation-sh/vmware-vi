# OverwriteCustomizationSpecRequestType

The parameters of *CustomizationSpecManager.OverwriteCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**CustomizationSpecItem**](CustomizationSpecItem.md) |  | 

## Example

```python
from vmware_vi.models.overwrite_customization_spec_request_type import OverwriteCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of OverwriteCustomizationSpecRequestType from a JSON string
overwrite_customization_spec_request_type_instance = OverwriteCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print OverwriteCustomizationSpecRequestType.to_json()

# convert the object into a dict
overwrite_customization_spec_request_type_dict = overwrite_customization_spec_request_type_instance.to_dict()
# create an instance of OverwriteCustomizationSpecRequestType from a dict
overwrite_customization_spec_request_type_form_dict = overwrite_customization_spec_request_type.from_dict(overwrite_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


