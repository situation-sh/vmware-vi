# SnapshotRevertIssue

If the virtual machine is migrated to the destination host, there may be a problem reverting to one of its snapshots.  This is a warning. If the snapshot name is not set and the event array is empty, then it the snapshot might possibly revert correctly. If the name is set and the event array is not empty then there surely will be a problem reverting to the snapshot. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_name** | **str** | The name of the problematic snapshot.  | [optional] 
**event** | [**List[Event]**](Event.md) | The problem(s) that would occur on reverting to the snapshot.  This is determined similarly to invoking validateMigration on a powered-off virtual machine with the snapshot&#39;s state. However, not all errors or warnings for virtual machine migration are guaranteed to be detected for snapshots.  | [optional] 
**errors** | **bool** | True if any of the events above are error events.  | 

## Example

```python
from vmware_vi.models.snapshot_revert_issue import SnapshotRevertIssue

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRevertIssue from a JSON string
snapshot_revert_issue_instance = SnapshotRevertIssue.from_json(json)
# print the JSON string representation of the object
print SnapshotRevertIssue.to_json()

# convert the object into a dict
snapshot_revert_issue_dict = snapshot_revert_issue_instance.to_dict()
# create an instance of SnapshotRevertIssue from a dict
snapshot_revert_issue_form_dict = snapshot_revert_issue.from_dict(snapshot_revert_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


