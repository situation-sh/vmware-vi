# RetrieveSnapshotDetailsRequestType

The parameters of *VcenterVStorageObjectManager.RetrieveSnapshotDetails*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_snapshot_details_request_type import RetrieveSnapshotDetailsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveSnapshotDetailsRequestType from a JSON string
retrieve_snapshot_details_request_type_instance = RetrieveSnapshotDetailsRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveSnapshotDetailsRequestType.to_json()

# convert the object into a dict
retrieve_snapshot_details_request_type_dict = retrieve_snapshot_details_request_type_instance.to_dict()
# create an instance of RetrieveSnapshotDetailsRequestType from a dict
retrieve_snapshot_details_request_type_form_dict = retrieve_snapshot_details_request_type.from_dict(retrieve_snapshot_details_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


