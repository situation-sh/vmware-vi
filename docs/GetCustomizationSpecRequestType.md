# GetCustomizationSpecRequestType

The parameters of *CustomizationSpecManager.GetCustomizationSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name identifying the requested customization specification.  | 

## Example

```python
from vmware_vi.models.get_customization_spec_request_type import GetCustomizationSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomizationSpecRequestType from a JSON string
get_customization_spec_request_type_instance = GetCustomizationSpecRequestType.from_json(json)
# print the JSON string representation of the object
print GetCustomizationSpecRequestType.to_json()

# convert the object into a dict
get_customization_spec_request_type_dict = get_customization_spec_request_type_instance.to_dict()
# create an instance of GetCustomizationSpecRequestType from a dict
get_customization_spec_request_type_form_dict = get_customization_spec_request_type.from_dict(get_customization_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


