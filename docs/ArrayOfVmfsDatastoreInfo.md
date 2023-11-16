# ArrayOfVmfsDatastoreInfo

A boxed array of *VmfsDatastoreInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsDatastoreInfo]**](VmfsDatastoreInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_datastore_info import ArrayOfVmfsDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsDatastoreInfo from a JSON string
array_of_vmfs_datastore_info_instance = ArrayOfVmfsDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsDatastoreInfo.to_json()

# convert the object into a dict
array_of_vmfs_datastore_info_dict = array_of_vmfs_datastore_info_instance.to_dict()
# create an instance of ArrayOfVmfsDatastoreInfo from a dict
array_of_vmfs_datastore_info_form_dict = array_of_vmfs_datastore_info.from_dict(array_of_vmfs_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


