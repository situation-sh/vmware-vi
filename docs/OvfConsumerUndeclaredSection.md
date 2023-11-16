# OvfConsumerUndeclaredSection

A fault type indicating that an OVF consumer appended an undeclared section to an OST.  An undeclared section means a section with a qualified type that the OVF consumer was not registered as a handler of.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qualified_section_type** | **str** | The undeclared qualified section type appended by the OVF consumer.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_consumer_undeclared_section import OvfConsumerUndeclaredSection

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerUndeclaredSection from a JSON string
ovf_consumer_undeclared_section_instance = OvfConsumerUndeclaredSection.from_json(json)
# print the JSON string representation of the object
print OvfConsumerUndeclaredSection.to_json()

# convert the object into a dict
ovf_consumer_undeclared_section_dict = ovf_consumer_undeclared_section_instance.to_dict()
# create an instance of OvfConsumerUndeclaredSection from a dict
ovf_consumer_undeclared_section_form_dict = ovf_consumer_undeclared_section.from_dict(ovf_consumer_undeclared_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


