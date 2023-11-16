# CheckCustomizationSpecRequestType

The parameters of *VirtualMachine.CheckCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**CustomizationSpec**](CustomizationSpec.md) |  | 

## Example

```python
from vmware_vi.models.check_customization_spec_request_type import CheckCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckCustomizationSpecRequestType from a JSON string
check_customization_spec_request_type_instance = CheckCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print CheckCustomizationSpecRequestType.to_json()

# convert the object into a dict
check_customization_spec_request_type_dict = check_customization_spec_request_type_instance.to_dict()
# create an instance of CheckCustomizationSpecRequestType from a dict
check_customization_spec_request_type_form_dict = check_customization_spec_request_type.from_dict(check_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


