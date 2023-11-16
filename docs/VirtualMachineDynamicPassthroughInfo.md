# VirtualMachineDynamicPassthroughInfo

Description of a Dynamic DirectPath PCI device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** | The vendor name of this PCI device.  ***Since:*** vSphere API 7.0  | 
**device_name** | **str** | The device name of this PCI device.  ***Since:*** vSphere API 7.0  | 
**custom_label** | **str** | The custom label attached to this PCI device.  ***Since:*** vSphere API 7.0  | [optional] 
**vendor_id** | **int** | PCI vendor ID for this device.  ***Since:*** vSphere API 7.0  | 
**device_id** | **int** | PCI device ID for this device.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_dynamic_passthrough_info import VirtualMachineDynamicPassthroughInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDynamicPassthroughInfo from a JSON string
virtual_machine_dynamic_passthrough_info_instance = VirtualMachineDynamicPassthroughInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDynamicPassthroughInfo.to_json()

# convert the object into a dict
virtual_machine_dynamic_passthrough_info_dict = virtual_machine_dynamic_passthrough_info_instance.to_dict()
# create an instance of VirtualMachineDynamicPassthroughInfo from a dict
virtual_machine_dynamic_passthrough_info_form_dict = virtual_machine_dynamic_passthrough_info.from_dict(virtual_machine_dynamic_passthrough_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


