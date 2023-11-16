# HostLowLevelProvisioningManagerDiskLayoutSpec

File layout spec of a virtual disk.  The disk could be either a base-disk or a delta disk.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_type** | **str** | Disk controller type, e.g.  vim.vm.device.VirtualSCSIController or vim.vm.device.VirtualIDEController.  ***Since:*** vSphere API 5.0  | 
**bus_number** | **int** | Bus number associated with the controller for this disk.  ***Since:*** vSphere API 5.0  | 
**unit_number** | **int** | Unit number of this disk on its controller.  ***Since:*** vSphere API 5.0  | 
**src_filename** | **str** | Source disk filename in datastore path.  ***Since:*** vSphere API 5.0  | 
**dst_filename** | **str** | Destination filename in datastore path.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_disk_layout_spec import HostLowLevelProvisioningManagerDiskLayoutSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerDiskLayoutSpec from a JSON string
host_low_level_provisioning_manager_disk_layout_spec_instance = HostLowLevelProvisioningManagerDiskLayoutSpec.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerDiskLayoutSpec.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_disk_layout_spec_dict = host_low_level_provisioning_manager_disk_layout_spec_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerDiskLayoutSpec from a dict
host_low_level_provisioning_manager_disk_layout_spec_form_dict = host_low_level_provisioning_manager_disk_layout_spec.from_dict(host_low_level_provisioning_manager_disk_layout_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


