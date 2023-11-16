# CannotDisableSnapshot

Fault thrown when an attempt is made to disable snapshots on a virtual machine which has a snapshot.  To disable the snapshot feature, the virtual machine must not currently have a snapshot.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_disable_snapshot import CannotDisableSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of CannotDisableSnapshot from a JSON string
cannot_disable_snapshot_instance = CannotDisableSnapshot.from_json(json)
# print the JSON string representation of the object
print CannotDisableSnapshot.to_json()

# convert the object into a dict
cannot_disable_snapshot_dict = cannot_disable_snapshot_instance.to_dict()
# create an instance of CannotDisableSnapshot from a dict
cannot_disable_snapshot_form_dict = cannot_disable_snapshot.from_dict(cannot_disable_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


