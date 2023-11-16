# HostDatastoreNameConflictConnectInfo

This data object type describes a datastore on the host that has the same name as a different datastore on VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_datastore_name** | **str** | To resolve a conflict with existing datastores, a suggested new name of the datastore can be provided.  | 

## Example

```python
from vmware_vi.models.host_datastore_name_conflict_connect_info import HostDatastoreNameConflictConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreNameConflictConnectInfo from a JSON string
host_datastore_name_conflict_connect_info_instance = HostDatastoreNameConflictConnectInfo.from_json(json)
# print the JSON string representation of the object
print HostDatastoreNameConflictConnectInfo.to_json()

# convert the object into a dict
host_datastore_name_conflict_connect_info_dict = host_datastore_name_conflict_connect_info_instance.to_dict()
# create an instance of HostDatastoreNameConflictConnectInfo from a dict
host_datastore_name_conflict_connect_info_form_dict = host_datastore_name_conflict_connect_info.from_dict(host_datastore_name_conflict_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


