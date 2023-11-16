# HostLowLevelProvisioningManagerSnapshotLayoutSpec

File layout spec of a snapshot, including path to the vmsn file of the snapshot and the layout of virtual disks when the snapshot was taken.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the snapshot  ***Since:*** vSphere API 5.0  | 
**src_filename** | **str** | Name of the source snapshot file in datastore path.  ***Since:*** vSphere API 5.0  | 
**dst_filename** | **str** | Name of the destination snapshot file in datastore path.  ***Since:*** vSphere API 5.0  | 
**disk** | [**List[HostLowLevelProvisioningManagerDiskLayoutSpec]**](HostLowLevelProvisioningManagerDiskLayoutSpec.md) | Layout of each virtual disk of the virtual machine when the snapshot was taken.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_snapshot_layout_spec import HostLowLevelProvisioningManagerSnapshotLayoutSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerSnapshotLayoutSpec from a JSON string
host_low_level_provisioning_manager_snapshot_layout_spec_instance = HostLowLevelProvisioningManagerSnapshotLayoutSpec.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerSnapshotLayoutSpec.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_snapshot_layout_spec_dict = host_low_level_provisioning_manager_snapshot_layout_spec_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerSnapshotLayoutSpec from a dict
host_low_level_provisioning_manager_snapshot_layout_spec_form_dict = host_low_level_provisioning_manager_snapshot_layout_spec.from_dict(host_low_level_provisioning_manager_snapshot_layout_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


