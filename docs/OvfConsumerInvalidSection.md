# OvfConsumerInvalidSection

A fault type indicating that the XML of a section appended by an OVF consumer was invalid.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | The line number in the section on which the error was found.  ***Since:*** vSphere API 5.0  | 
**description** | **str** | The XML parser error message.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_invalid_section import OvfConsumerInvalidSection

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerInvalidSection from a JSON string
ovf_consumer_invalid_section_instance = OvfConsumerInvalidSection.from_json(json)
# print the JSON string representation of the object
print OvfConsumerInvalidSection.to_json()

# convert the object into a dict
ovf_consumer_invalid_section_dict = ovf_consumer_invalid_section_instance.to_dict()
# create an instance of OvfConsumerInvalidSection from a dict
ovf_consumer_invalid_section_form_dict = ovf_consumer_invalid_section.from_dict(ovf_consumer_invalid_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


