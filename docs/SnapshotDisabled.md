# SnapshotDisabled

Fault thrown if a snapshot operation cannot be performed because snapshots are disabled on the virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.snapshot_disabled import SnapshotDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDisabled from a JSON string
snapshot_disabled_instance = SnapshotDisabled.from_json(json)
# print the JSON string representation of the object
print SnapshotDisabled.to_json()

# convert the object into a dict
snapshot_disabled_dict = snapshot_disabled_instance.to_dict()
# create an instance of SnapshotDisabled from a dict
snapshot_disabled_form_dict = snapshot_disabled.from_dict(snapshot_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


