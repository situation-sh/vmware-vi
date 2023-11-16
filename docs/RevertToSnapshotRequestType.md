# RevertToSnapshotRequestType

The parameters of *VirtualMachineSnapshot.RevertToSnapshot_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**suppress_power_on** | **bool** | (optional) If set to true, the virtual machine will not be powered on regardless of the power state when the snapshot was created. Default to false.  | [optional] 

## Example

```python
from vmware_vi.models.revert_to_snapshot_request_type import RevertToSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RevertToSnapshotRequestType from a JSON string
revert_to_snapshot_request_type_instance = RevertToSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print RevertToSnapshotRequestType.to_json()

# convert the object into a dict
revert_to_snapshot_request_type_dict = revert_to_snapshot_request_type_instance.to_dict()
# create an instance of RevertToSnapshotRequestType from a dict
revert_to_snapshot_request_type_form_dict = revert_to_snapshot_request_type.from_dict(revert_to_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


