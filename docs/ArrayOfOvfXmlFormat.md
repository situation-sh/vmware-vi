# ArrayOfOvfXmlFormat

A boxed array of *OvfXmlFormat*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfXmlFormat]**](OvfXmlFormat.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_xml_format import ArrayOfOvfXmlFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfXmlFormat from a JSON string
array_of_ovf_xml_format_instance = ArrayOfOvfXmlFormat.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfXmlFormat.to_json()

# convert the object into a dict
array_of_ovf_xml_format_dict = array_of_ovf_xml_format_instance.to_dict()
# create an instance of ArrayOfOvfXmlFormat from a dict
array_of_ovf_xml_format_form_dict = array_of_ovf_xml_format.from_dict(array_of_ovf_xml_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


