# VirtualTPMOption

This data object type contains the options for the virtual TPM class.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_firmware** | **List[str]** | List of supported firmware selections, using *GuestOsDescriptorFirmwareType_enum* enumeration.  There is at least one value in this array.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_tpm_option import VirtualTPMOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualTPMOption from a JSON string
virtual_tpm_option_instance = VirtualTPMOption.from_json(json)
# print the JSON string representation of the object
print VirtualTPMOption.to_json()

# convert the object into a dict
virtual_tpm_option_dict = virtual_tpm_option_instance.to_dict()
# create an instance of VirtualTPMOption from a dict
virtual_tpm_option_form_dict = virtual_tpm_option.from_dict(virtual_tpm_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


