# GuestInfoVirtualDiskMapping

Describes the virtual disk backing a local guest disk.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | The key of the VirtualDevice.  *VirtualDevice.key*  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.guest_info_virtual_disk_mapping import GuestInfoVirtualDiskMapping

# TODO update the JSON string below
json = "{}"
# create an instance of GuestInfoVirtualDiskMapping from a JSON string
guest_info_virtual_disk_mapping_instance = GuestInfoVirtualDiskMapping.from_json(json)
# print the JSON string representation of the object
print GuestInfoVirtualDiskMapping.to_json()

# convert the object into a dict
guest_info_virtual_disk_mapping_dict = guest_info_virtual_disk_mapping_instance.to_dict()
# create an instance of GuestInfoVirtualDiskMapping from a dict
guest_info_virtual_disk_mapping_form_dict = guest_info_virtual_disk_mapping.from_dict(guest_info_virtual_disk_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


