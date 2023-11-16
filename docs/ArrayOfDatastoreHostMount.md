# ArrayOfDatastoreHostMount

A boxed array of *DatastoreHostMount*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreHostMount]**](DatastoreHostMount.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_host_mount import ArrayOfDatastoreHostMount

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreHostMount from a JSON string
array_of_datastore_host_mount_instance = ArrayOfDatastoreHostMount.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreHostMount.to_json()

# convert the object into a dict
array_of_datastore_host_mount_dict = array_of_datastore_host_mount_instance.to_dict()
# create an instance of ArrayOfDatastoreHostMount from a dict
array_of_datastore_host_mount_form_dict = array_of_datastore_host_mount.from_dict(array_of_datastore_host_mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


