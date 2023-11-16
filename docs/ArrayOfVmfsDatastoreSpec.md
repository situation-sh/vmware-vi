# ArrayOfVmfsDatastoreSpec

A boxed array of *VmfsDatastoreSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsDatastoreSpec]**](VmfsDatastoreSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_datastore_spec import ArrayOfVmfsDatastoreSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsDatastoreSpec from a JSON string
array_of_vmfs_datastore_spec_instance = ArrayOfVmfsDatastoreSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsDatastoreSpec.to_json()

# convert the object into a dict
array_of_vmfs_datastore_spec_dict = array_of_vmfs_datastore_spec_instance.to_dict()
# create an instance of ArrayOfVmfsDatastoreSpec from a dict
array_of_vmfs_datastore_spec_form_dict = array_of_vmfs_datastore_spec.from_dict(array_of_vmfs_datastore_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


