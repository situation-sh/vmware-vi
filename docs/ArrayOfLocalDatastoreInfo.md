# ArrayOfLocalDatastoreInfo

A boxed array of *LocalDatastoreInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LocalDatastoreInfo]**](LocalDatastoreInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_local_datastore_info import ArrayOfLocalDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLocalDatastoreInfo from a JSON string
array_of_local_datastore_info_instance = ArrayOfLocalDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfLocalDatastoreInfo.to_json()

# convert the object into a dict
array_of_local_datastore_info_dict = array_of_local_datastore_info_instance.to_dict()
# create an instance of ArrayOfLocalDatastoreInfo from a dict
array_of_local_datastore_info_form_dict = array_of_local_datastore_info.from_dict(array_of_local_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


