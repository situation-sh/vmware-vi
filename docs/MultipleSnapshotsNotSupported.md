# MultipleSnapshotsNotSupported

Fault thrown when an attempt is made to create a second snapshot on a VM that only supports a single snapshot at a time. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.multiple_snapshots_not_supported import MultipleSnapshotsNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MultipleSnapshotsNotSupported from a JSON string
multiple_snapshots_not_supported_instance = MultipleSnapshotsNotSupported.from_json(json)
# print the JSON string representation of the object
print MultipleSnapshotsNotSupported.to_json()

# convert the object into a dict
multiple_snapshots_not_supported_dict = multiple_snapshots_not_supported_instance.to_dict()
# create an instance of MultipleSnapshotsNotSupported from a dict
multiple_snapshots_not_supported_form_dict = multiple_snapshots_not_supported.from_dict(multiple_snapshots_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


