# ArrayOfSnapshotRevertIssue

A boxed array of *SnapshotRevertIssue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SnapshotRevertIssue]**](SnapshotRevertIssue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_snapshot_revert_issue import ArrayOfSnapshotRevertIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSnapshotRevertIssue from a JSON string
array_of_snapshot_revert_issue_instance = ArrayOfSnapshotRevertIssue.from_json(json)
# print the JSON string representation of the object
print ArrayOfSnapshotRevertIssue.to_json()

# convert the object into a dict
array_of_snapshot_revert_issue_dict = array_of_snapshot_revert_issue_instance.to_dict()
# create an instance of ArrayOfSnapshotRevertIssue from a dict
array_of_snapshot_revert_issue_form_dict = array_of_snapshot_revert_issue.from_dict(array_of_snapshot_revert_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


