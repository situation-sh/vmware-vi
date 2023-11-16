# OvfToXmlUnsupportedElement

Unsupported element to export to XML  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the xml element we could not write to the xml descriptor  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_to_xml_unsupported_element import OvfToXmlUnsupportedElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfToXmlUnsupportedElement from a JSON string
ovf_to_xml_unsupported_element_instance = OvfToXmlUnsupportedElement.from_json(json)
# print the JSON string representation of the object
print OvfToXmlUnsupportedElement.to_json()

# convert the object into a dict
ovf_to_xml_unsupported_element_dict = ovf_to_xml_unsupported_element_instance.to_dict()
# create an instance of OvfToXmlUnsupportedElement from a dict
ovf_to_xml_unsupported_element_form_dict = ovf_to_xml_unsupported_element.from_dict(ovf_to_xml_unsupported_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


