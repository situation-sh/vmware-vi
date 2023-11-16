# CreateCustomizationSpecRequestType

The parameters of *CustomizationSpecManager.CreateCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**CustomizationSpecItem**](CustomizationSpecItem.md) |  | 

## Example

```python
from vmware_vi.models.create_customization_spec_request_type import CreateCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomizationSpecRequestType from a JSON string
create_customization_spec_request_type_instance = CreateCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print CreateCustomizationSpecRequestType.to_json()

# convert the object into a dict
create_customization_spec_request_type_dict = create_customization_spec_request_type_instance.to_dict()
# create an instance of CreateCustomizationSpecRequestType from a dict
create_customization_spec_request_type_form_dict = create_customization_spec_request_type.from_dict(create_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


