# OvfXmlFormat

Class used to specify if the Ovf XML descriptor could not be parsed  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the XML parser error  High level error description  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_xml_format import OvfXmlFormat

# TODO update the JSON string below
json = "{}"
# create an instance of OvfXmlFormat from a JSON string
ovf_xml_format_instance = OvfXmlFormat.from_json(json)
# print the JSON string representation of the object
print OvfXmlFormat.to_json()

# convert the object into a dict
ovf_xml_format_dict = ovf_xml_format_instance.to_dict()
# create an instance of OvfXmlFormat from a dict
ovf_xml_format_form_dict = ovf_xml_format.from_dict(ovf_xml_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


