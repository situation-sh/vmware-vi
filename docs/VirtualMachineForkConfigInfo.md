# VirtualMachineForkConfigInfo

This data object describes the fork configuration of this virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_enabled** | **bool** | Flag to indicate whether this virtual machine is a parent enabled virtual machine.  If this vm is not a parent enabled vm this property will be unset. When set into the vim.vm.ConfigSpec this flag will be ignored.  ***Since:*** vSphere API 6.0  | [optional] 
**child_fork_group_id** | **str** | The fork group ID identifies the parent group of which this child VirtualMachine is a child.  Applicable for child VirtualMachines only.  ***Since:*** vSphere API 6.0  | [optional] 
**parent_fork_group_id** | **str** | The fork group ID identifies the parent group which this VirtualMachine belongs to.  Applicable for parent VirtualMachines only.  ***Since:*** vSphere API 6.5  | [optional] 
**child_type** | **str** | The flag to indicate the fork child type.  For a persistent child virtual machine, once it is powered on, it will become a linked clone of its parent and this flag will be set to &#39;none&#39;.  See also *VirtualMachineForkConfigInfoChildType_enum*.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_fork_config_info import VirtualMachineForkConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineForkConfigInfo from a JSON string
virtual_machine_fork_config_info_instance = VirtualMachineForkConfigInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineForkConfigInfo.to_json()

# convert the object into a dict
virtual_machine_fork_config_info_dict = virtual_machine_fork_config_info_instance.to_dict()
# create an instance of VirtualMachineForkConfigInfo from a dict
virtual_machine_fork_config_info_form_dict = virtual_machine_fork_config_info.from_dict(virtual_machine_fork_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


