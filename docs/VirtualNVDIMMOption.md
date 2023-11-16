# VirtualNVDIMMOption

The VirtualNVDIMMOption contains information about a virtual NVDIMM capacity limits and rules for capacity growth operations.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_mb** | [**LongOption**](LongOption.md) |  | 
**growable** | **bool** | Option to show if device capacity growth is supported for powered off VMs.  ***Since:*** vSphere API 6.7  | 
**hot_growable** | **bool** | Option to show if device capacity growth is supported for powered on VMs.  ***Since:*** vSphere API 6.7  | 
**granularity_in_mb** | **int** | Option to show capacity growth granularity if growth operation is supported in MB.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.virtual_nvdimm_option import VirtualNVDIMMOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNVDIMMOption from a JSON string
virtual_nvdimm_option_instance = VirtualNVDIMMOption.from_json(json)
# print the JSON string representation of the object
print VirtualNVDIMMOption.to_json()

# convert the object into a dict
virtual_nvdimm_option_dict = virtual_nvdimm_option_instance.to_dict()
# create an instance of VirtualNVDIMMOption from a dict
virtual_nvdimm_option_form_dict = virtual_nvdimm_option.from_dict(virtual_nvdimm_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


