# VirtualMachineMetadataManagerVmMetadataOwner

VmMetadataOwner defines the namespace for an owner  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A string representing the owner.  Valid values come from *VirtualMachineMetadataManagerVmMetadataOwnerOwner_enum* for vSAN datastores. Otherwise, the owner field is interpreted by the implementation based on the datastore type.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.virtual_machine_metadata_manager_vm_metadata_owner import VirtualMachineMetadataManagerVmMetadataOwner

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMetadataManagerVmMetadataOwner from a JSON string
virtual_machine_metadata_manager_vm_metadata_owner_instance = VirtualMachineMetadataManagerVmMetadataOwner.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMetadataManagerVmMetadataOwner.to_json()

# convert the object into a dict
virtual_machine_metadata_manager_vm_metadata_owner_dict = virtual_machine_metadata_manager_vm_metadata_owner_instance.to_dict()
# create an instance of VirtualMachineMetadataManagerVmMetadataOwner from a dict
virtual_machine_metadata_manager_vm_metadata_owner_form_dict = virtual_machine_metadata_manager_vm_metadata_owner.from_dict(virtual_machine_metadata_manager_vm_metadata_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


