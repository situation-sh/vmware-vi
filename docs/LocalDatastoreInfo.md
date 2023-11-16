# LocalDatastoreInfo

The information details about a datastore that is local to a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The local path on a host.  May not be available when the datastore is not accessible.  | [optional] 

## Example

```python
from vmware_vi.models.local_datastore_info import LocalDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocalDatastoreInfo from a JSON string
local_datastore_info_instance = LocalDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print LocalDatastoreInfo.to_json()

# convert the object into a dict
local_datastore_info_dict = local_datastore_info_instance.to_dict()
# create an instance of LocalDatastoreInfo from a dict
local_datastore_info_form_dict = local_datastore_info.from_dict(local_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


