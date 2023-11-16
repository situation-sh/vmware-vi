# CloneFromSnapshotNotSupported

An attempt is being made to clone a virtual machine from a snapshot point, and this is not supported.  See also *VirtualMachineCloneSpec.snapshot*, *VirtualMachineCapability.snapshotConfigSupported*, *HostCapability.cloneFromSnapshotSupported*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.clone_from_snapshot_not_supported import CloneFromSnapshotNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of CloneFromSnapshotNotSupported from a JSON string
clone_from_snapshot_not_supported_instance = CloneFromSnapshotNotSupported.from_json(json)
# print the JSON string representation of the object
print CloneFromSnapshotNotSupported.to_json()

# convert the object into a dict
clone_from_snapshot_not_supported_dict = clone_from_snapshot_not_supported_instance.to_dict()
# create an instance of CloneFromSnapshotNotSupported from a dict
clone_from_snapshot_not_supported_form_dict = clone_from_snapshot_not_supported.from_dict(clone_from_snapshot_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


