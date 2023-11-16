# ReleaseManagedSnapshotRequestType

The parameters of *VirtualDiskManager.ReleaseManagedSnapshot*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vdisk** | **str** | \\- The name of the disk to release, either a datastore path or a URL referring to the virtual disk.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.release_managed_snapshot_request_type import ReleaseManagedSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseManagedSnapshotRequestType from a JSON string
release_managed_snapshot_request_type_instance = ReleaseManagedSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print ReleaseManagedSnapshotRequestType.to_json()

# convert the object into a dict
release_managed_snapshot_request_type_dict = release_managed_snapshot_request_type_instance.to_dict()
# create an instance of ReleaseManagedSnapshotRequestType from a dict
release_managed_snapshot_request_type_form_dict = release_managed_snapshot_request_type.from_dict(release_managed_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


