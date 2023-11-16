# OvfUnsupportedElement

If the Ovf descriptor has an unsupported element where it is not allowed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the unsupported element  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_element import OvfUnsupportedElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedElement from a JSON string
ovf_unsupported_element_instance = OvfUnsupportedElement.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedElement.to_json()

# convert the object into a dict
ovf_unsupported_element_dict = ovf_unsupported_element_instance.to_dict()
# create an instance of OvfUnsupportedElement from a dict
ovf_unsupported_element_form_dict = ovf_unsupported_element.from_dict(ovf_unsupported_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


