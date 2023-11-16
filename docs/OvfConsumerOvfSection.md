# OvfConsumerOvfSection

A self-contained OVF section  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | The line number in the OVF descriptor on which this section starts.  The line number is only present on sections that were imported as part of an OVF descriptor (as opposed to sections that are about to be exported to OVF).  The value is zero if the section did not originate from an OVF descriptor.  ***Since:*** vSphere API 5.0  | 
**xml** | **str** | The XML fragment for the section.  The XML fragment must explicitly define all namespaces and namespace prefixes that are used in the fragment, including the default namespace.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_ovf_section import OvfConsumerOvfSection

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerOvfSection from a JSON string
ovf_consumer_ovf_section_instance = OvfConsumerOvfSection.from_json(json)
# print the JSON string representation of the object
print OvfConsumerOvfSection.to_json()

# convert the object into a dict
ovf_consumer_ovf_section_dict = ovf_consumer_ovf_section_instance.to_dict()
# create an instance of OvfConsumerOvfSection from a dict
ovf_consumer_ovf_section_form_dict = ovf_consumer_ovf_section.from_dict(ovf_consumer_ovf_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


