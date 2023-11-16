# ArrayOfVirtualDiskBlocksNotFullyProvisioned

A boxed array of *VirtualDiskBlocksNotFullyProvisioned*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDiskBlocksNotFullyProvisioned]**](VirtualDiskBlocksNotFullyProvisioned.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_disk_blocks_not_fully_provisioned import ArrayOfVirtualDiskBlocksNotFullyProvisioned

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDiskBlocksNotFullyProvisioned from a JSON string
array_of_virtual_disk_blocks_not_fully_provisioned_instance = ArrayOfVirtualDiskBlocksNotFullyProvisioned.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDiskBlocksNotFullyProvisioned.to_json()

# convert the object into a dict
array_of_virtual_disk_blocks_not_fully_provisioned_dict = array_of_virtual_disk_blocks_not_fully_provisioned_instance.to_dict()
# create an instance of ArrayOfVirtualDiskBlocksNotFullyProvisioned from a dict
array_of_virtual_disk_blocks_not_fully_provisioned_form_dict = array_of_virtual_disk_blocks_not_fully_provisioned.from_dict(array_of_virtual_disk_blocks_not_fully_provisioned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


