# WillResetSnapshotDirectory

This fault is reported when the execution of a storage vmotion or relocate operation would reset the snapshotDirectory settings to its default value (VM's home/config directory).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.will_reset_snapshot_directory import WillResetSnapshotDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of WillResetSnapshotDirectory from a JSON string
will_reset_snapshot_directory_instance = WillResetSnapshotDirectory.from_json(json)
# print the JSON string representation of the object
print WillResetSnapshotDirectory.to_json()

# convert the object into a dict
will_reset_snapshot_directory_dict = will_reset_snapshot_directory_instance.to_dict()
# create an instance of WillResetSnapshotDirectory from a dict
will_reset_snapshot_directory_form_dict = will_reset_snapshot_directory.from_dict(will_reset_snapshot_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


