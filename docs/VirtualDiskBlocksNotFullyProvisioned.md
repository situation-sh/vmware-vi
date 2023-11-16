# VirtualDiskBlocksNotFullyProvisioned

The disk blocks of the specified virtual disk have not been fully provisioned on the file system.  Typically, this fault is returned as part of a parent fault like *VmConfigIncompatibleForFaultTolerance*, indicating that the disk blocks of the virtual disk must be fully provisioned on the file system before fault tolerance can be enabled on the associated virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_disk_blocks_not_fully_provisioned import VirtualDiskBlocksNotFullyProvisioned

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskBlocksNotFullyProvisioned from a JSON string
virtual_disk_blocks_not_fully_provisioned_instance = VirtualDiskBlocksNotFullyProvisioned.from_json(json)
# print the JSON string representation of the object
print VirtualDiskBlocksNotFullyProvisioned.to_json()

# convert the object into a dict
virtual_disk_blocks_not_fully_provisioned_dict = virtual_disk_blocks_not_fully_provisioned_instance.to_dict()
# create an instance of VirtualDiskBlocksNotFullyProvisioned from a dict
virtual_disk_blocks_not_fully_provisioned_form_dict = virtual_disk_blocks_not_fully_provisioned.from_dict(virtual_disk_blocks_not_fully_provisioned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


