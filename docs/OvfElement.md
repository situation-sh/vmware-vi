# OvfElement

A base fault for element exceptions in the Ovf XML descriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the element  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_element import OvfElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfElement from a JSON string
ovf_element_instance = OvfElement.from_json(json)
# print the JSON string representation of the object
print OvfElement.to_json()

# convert the object into a dict
ovf_element_dict = ovf_element_instance.to_dict()
# create an instance of OvfElement from a dict
ovf_element_form_dict = ovf_element.from_dict(ovf_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


