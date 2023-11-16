# OvfDuplicateElement

OvfDuplicateElement is thrown if Ovf descriptor contains an invalid duplicate element.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_duplicate_element import OvfDuplicateElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDuplicateElement from a JSON string
ovf_duplicate_element_instance = OvfDuplicateElement.from_json(json)
# print the JSON string representation of the object
print OvfDuplicateElement.to_json()

# convert the object into a dict
ovf_duplicate_element_dict = ovf_duplicate_element_instance.to_dict()
# create an instance of OvfDuplicateElement from a dict
ovf_duplicate_element_form_dict = ovf_duplicate_element.from_dict(ovf_duplicate_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


