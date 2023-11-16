# RevertToCurrentSnapshotRequestType

The parameters of *VirtualMachine.RevertToCurrentSnapshot_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**suppress_power_on** | **bool** | (optional) If set to true, the virtual machine will not be powered on regardless of the power state when the current snapshot was created. Default to false.  | [optional] 

## Example

```python
from vmware_vi.models.revert_to_current_snapshot_request_type import RevertToCurrentSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RevertToCurrentSnapshotRequestType from a JSON string
revert_to_current_snapshot_request_type_instance = RevertToCurrentSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print RevertToCurrentSnapshotRequestType.to_json()

# convert the object into a dict
revert_to_current_snapshot_request_type_dict = revert_to_current_snapshot_request_type_instance.to_dict()
# create an instance of RevertToCurrentSnapshotRequestType from a dict
revert_to_current_snapshot_request_type_form_dict = revert_to_current_snapshot_request_type.from_dict(revert_to_current_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


