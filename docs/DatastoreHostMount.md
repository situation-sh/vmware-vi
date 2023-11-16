# DatastoreHostMount

Host-specific datastore information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**mount_info** | [**HostMountInfo**](HostMountInfo.md) |  | 

## Example

```python
from vmware_vi.models.datastore_host_mount import DatastoreHostMount

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreHostMount from a JSON string
datastore_host_mount_instance = DatastoreHostMount.from_json(json)
# print the JSON string representation of the object
print DatastoreHostMount.to_json()

# convert the object into a dict
datastore_host_mount_dict = datastore_host_mount_instance.to_dict()
# create an instance of DatastoreHostMount from a dict
datastore_host_mount_form_dict = datastore_host_mount.from_dict(datastore_host_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


