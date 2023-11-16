# OvfUnsupportedSection

If the Ovf descriptor has an unsupported required section.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **str** | The info of the unsupported section  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_section import OvfUnsupportedSection

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedSection from a JSON string
ovf_unsupported_section_instance = OvfUnsupportedSection.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedSection.to_json()

# convert the object into a dict
ovf_unsupported_section_dict = ovf_unsupported_section_instance.to_dict()
# create an instance of OvfUnsupportedSection from a dict
ovf_unsupported_section_form_dict = ovf_unsupported_section.from_dict(ovf_unsupported_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


