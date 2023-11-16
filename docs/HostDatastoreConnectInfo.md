# HostDatastoreConnectInfo

The base data object type for information about datastores on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**DatastoreSummary**](DatastoreSummary.md) |  | 

## Example

```python
from vmware_vi.models.host_datastore_connect_info import HostDatastoreConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreConnectInfo from a JSON string
host_datastore_connect_info_instance = HostDatastoreConnectInfo.from_json(json)
# print the JSON string representation of the object
print HostDatastoreConnectInfo.to_json()

# convert the object into a dict
host_datastore_connect_info_dict = host_datastore_connect_info_instance.to_dict()
# create an instance of HostDatastoreConnectInfo from a dict
host_datastore_connect_info_form_dict = host_datastore_connect_info.from_dict(host_datastore_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


