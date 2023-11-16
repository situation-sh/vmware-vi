# OvfNoSupportedHardwareFamily


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version found that was not supported  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_no_supported_hardware_family import OvfNoSupportedHardwareFamily

# TODO update the JSON string below
json = "{}"
# create an instance of OvfNoSupportedHardwareFamily from a JSON string
ovf_no_supported_hardware_family_instance = OvfNoSupportedHardwareFamily.from_json(json)
# print the JSON string representation of the object
print OvfNoSupportedHardwareFamily.to_json()

# convert the object into a dict
ovf_no_supported_hardware_family_dict = ovf_no_supported_hardware_family_instance.to_dict()
# create an instance of OvfNoSupportedHardwareFamily from a dict
ovf_no_supported_hardware_family_form_dict = ovf_no_supported_hardware_family.from_dict(ovf_no_supported_hardware_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


