# DeleteCustomizationSpecRequestType

The parameters of *CustomizationSpecManager.DeleteCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from vmware_vi.models.delete_customization_spec_request_type import DeleteCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomizationSpecRequestType from a JSON string
delete_customization_spec_request_type_instance = DeleteCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteCustomizationSpecRequestType.to_json()

# convert the object into a dict
delete_customization_spec_request_type_dict = delete_customization_spec_request_type_instance.to_dict()
# create an instance of DeleteCustomizationSpecRequestType from a dict
delete_customization_spec_request_type_form_dict = delete_customization_spec_request_type.from_dict(delete_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


