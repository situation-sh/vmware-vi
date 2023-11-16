# OvfUnexpectedElement

Class used to indicate an unexpected element in the Ovf descriptor  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_unexpected_element import OvfUnexpectedElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnexpectedElement from a JSON string
ovf_unexpected_element_instance = OvfUnexpectedElement.from_json(json)
# print the JSON string representation of the object
print OvfUnexpectedElement.to_json()

# convert the object into a dict
ovf_unexpected_element_dict = ovf_unexpected_element_instance.to_dict()
# create an instance of OvfUnexpectedElement from a dict
ovf_unexpected_element_form_dict = ovf_unexpected_element.from_dict(ovf_unexpected_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


