# VAppOvfSectionInfo

The OvfSection encapsulates uninterpreted meta-data sections in an OVF descriptor.  When an OVF package is imported, non-required / non-interpreted sections will be stored as OvfSection object. During the creation of an OVF package, these sections will be placed in the OVF descriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A unique key to identify a section.  ***Since:*** vSphere API 4.0  | [optional] 
**namespace** | **str** | The namespace for the value in xsi:type attribute.  ***Since:*** vSphere API 4.0  | [optional] 
**type** | **str** | The value of the xsi:type attribute not including the namespace prefix.  ***Since:*** vSphere API 4.0  | [optional] 
**at_envelope_level** | **bool** | Whether this is a global envelope section  ***Since:*** vSphere API 4.0  | [optional] 
**contents** | **str** | The XML fragment including the top-level &amp;lt;Section...&amp;gt; element.  The fragment is self-contained will all required namespace definitions.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.v_app_ovf_section_info import VAppOvfSectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VAppOvfSectionInfo from a JSON string
v_app_ovf_section_info_instance = VAppOvfSectionInfo.from_json(json)
# print the JSON string representation of the object
print VAppOvfSectionInfo.to_json()

# convert the object into a dict
v_app_ovf_section_info_dict = v_app_ovf_section_info_instance.to_dict()
# create an instance of VAppOvfSectionInfo from a dict
v_app_ovf_section_info_form_dict = v_app_ovf_section_info.from_dict(v_app_ovf_section_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


