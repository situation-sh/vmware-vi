# OvfElementInvalidValue

A class used if a element node is found to have an invalid value.  Base class for OvfProperty errors.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the element  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_element_invalid_value import OvfElementInvalidValue

# TODO update the JSON string below
json = "{}"
# create an instance of OvfElementInvalidValue from a JSON string
ovf_element_invalid_value_instance = OvfElementInvalidValue.from_json(json)
# print the JSON string representation of the object
print OvfElementInvalidValue.to_json()

# convert the object into a dict
ovf_element_invalid_value_dict = ovf_element_invalid_value_instance.to_dict()
# create an instance of OvfElementInvalidValue from a dict
ovf_element_invalid_value_form_dict = ovf_element_invalid_value.from_dict(ovf_element_invalid_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


