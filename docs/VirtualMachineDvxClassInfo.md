# VirtualMachineDvxClassInfo

Description of a Device Virtualization Extensions (DVX) device class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_class** | [**ElementDescription**](ElementDescription.md) |  | 
**vendor_name** | **str** | The label for the vendor name of this class.  The value is defined by vendors of the DVX device class as part of their localizable messages.  | 
**sriov_nic** | **bool** | Indicates whether the devices of this class are SR-IOV NICs.  | 
**config_params** | [**List[OptionDef]**](OptionDef.md) | The configuration parameters for this DVX device class.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_dvx_class_info import VirtualMachineDvxClassInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDvxClassInfo from a JSON string
virtual_machine_dvx_class_info_instance = VirtualMachineDvxClassInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDvxClassInfo.to_json()

# convert the object into a dict
virtual_machine_dvx_class_info_dict = virtual_machine_dvx_class_info_instance.to_dict()
# create an instance of VirtualMachineDvxClassInfo from a dict
virtual_machine_dvx_class_info_form_dict = virtual_machine_dvx_class_info.from_dict(virtual_machine_dvx_class_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


