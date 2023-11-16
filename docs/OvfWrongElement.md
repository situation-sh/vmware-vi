# OvfWrongElement

If the Ovf descriptor has an element that is not accepted, this exception is thrown.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_wrong_element import OvfWrongElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfWrongElement from a JSON string
ovf_wrong_element_instance = OvfWrongElement.from_json(json)
# print the JSON string representation of the object
print OvfWrongElement.to_json()

# convert the object into a dict
ovf_wrong_element_dict = ovf_wrong_element_instance.to_dict()
# create an instance of OvfWrongElement from a dict
ovf_wrong_element_form_dict = ovf_wrong_element.from_dict(ovf_wrong_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


