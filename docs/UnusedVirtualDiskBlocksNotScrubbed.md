# UnusedVirtualDiskBlocksNotScrubbed

The unused disk blocks of the specified virtual disk have not been scrubbed on the file system.  Typically, this fault is returned as part of a parent fault like *VmConfigIncompatibleForFaultTolerance*, indicating that the unused blocks of the virtual disk must be zeroed-out on the file system before before fault tolerance can be enabled on the associated virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.unused_virtual_disk_blocks_not_scrubbed import UnusedVirtualDiskBlocksNotScrubbed

# TODO update the JSON string below
json = "{}"
# create an instance of UnusedVirtualDiskBlocksNotScrubbed from a JSON string
unused_virtual_disk_blocks_not_scrubbed_instance = UnusedVirtualDiskBlocksNotScrubbed.from_json(json)
# print the JSON string representation of the object
print UnusedVirtualDiskBlocksNotScrubbed.to_json()

# convert the object into a dict
unused_virtual_disk_blocks_not_scrubbed_dict = unused_virtual_disk_blocks_not_scrubbed_instance.to_dict()
# create an instance of UnusedVirtualDiskBlocksNotScrubbed from a dict
unused_virtual_disk_blocks_not_scrubbed_form_dict = unused_virtual_disk_blocks_not_scrubbed.from_dict(unused_virtual_disk_blocks_not_scrubbed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


