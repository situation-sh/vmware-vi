# InvalidDatastorePath

An InvalidDatastorePath exception is thrown if a datastore path violates the expected format.  The expected format is \"\\[dsName\\] path\", e.g. \"\\[storage1\\] folder/Vm1.vmdk\". This exception is also thrown if a datastore corresponding to the given datastore path is not found. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_path** | **str** | The invalid datastore path name, if one was provided.  | 

## Example

```python
from vmware_vi.models.invalid_datastore_path import InvalidDatastorePath

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDatastorePath from a JSON string
invalid_datastore_path_instance = InvalidDatastorePath.from_json(json)
# print the JSON string representation of the object
print InvalidDatastorePath.to_json()

# convert the object into a dict
invalid_datastore_path_dict = invalid_datastore_path_instance.to_dict()
# create an instance of InvalidDatastorePath from a dict
invalid_datastore_path_form_dict = invalid_datastore_path.from_dict(invalid_datastore_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


