# HostDatastoreExistsConnectInfo

This data object type describes a datastore on the host that matches an existing datastore on VirtualCenter that has a different name. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_datastore_name** | **str** | The name of a matching datastore on VirtualCenter.  The datastore on the host will be renamed to this name.  | 

## Example

```python
from vmware_vi.models.host_datastore_exists_connect_info import HostDatastoreExistsConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreExistsConnectInfo from a JSON string
host_datastore_exists_connect_info_instance = HostDatastoreExistsConnectInfo.from_json(json)
# print the JSON string representation of the object
print HostDatastoreExistsConnectInfo.to_json()

# convert the object into a dict
host_datastore_exists_connect_info_dict = host_datastore_exists_connect_info_instance.to_dict()
# create an instance of HostDatastoreExistsConnectInfo from a dict
host_datastore_exists_connect_info_form_dict = host_datastore_exists_connect_info.from_dict(host_datastore_exists_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


