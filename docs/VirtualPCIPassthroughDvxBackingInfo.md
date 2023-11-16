# VirtualPCIPassthroughDvxBackingInfo

DVX Device specific information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_class** | **str** | The device class that backs this DVX device.  During add operations, this value must be a non-empty string. During edit operations, if this value is not set or is an empty string, the current device class remains unchanged.  | [optional] 
**config_params** | [**List[OptionValue]**](OptionValue.md) | The configuration parameters for this device class.  All required configuration parameters must be provided for both add and edit operations. The provided configuration parameters replace the previous ones. In particular, passing an empty array will unset all existing configuration parameters.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_dvx_backing_info import VirtualPCIPassthroughDvxBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughDvxBackingInfo from a JSON string
virtual_pci_passthrough_dvx_backing_info_instance = VirtualPCIPassthroughDvxBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughDvxBackingInfo.to_json()

# convert the object into a dict
virtual_pci_passthrough_dvx_backing_info_dict = virtual_pci_passthrough_dvx_backing_info_instance.to_dict()
# create an instance of VirtualPCIPassthroughDvxBackingInfo from a dict
virtual_pci_passthrough_dvx_backing_info_form_dict = virtual_pci_passthrough_dvx_backing_info.from_dict(virtual_pci_passthrough_dvx_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


