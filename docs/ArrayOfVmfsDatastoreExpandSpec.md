# ArrayOfVmfsDatastoreExpandSpec

A boxed array of *VmfsDatastoreExpandSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsDatastoreExpandSpec]**](VmfsDatastoreExpandSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_datastore_expand_spec import ArrayOfVmfsDatastoreExpandSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsDatastoreExpandSpec from a JSON string
array_of_vmfs_datastore_expand_spec_instance = ArrayOfVmfsDatastoreExpandSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsDatastoreExpandSpec.to_json()

# convert the object into a dict
array_of_vmfs_datastore_expand_spec_dict = array_of_vmfs_datastore_expand_spec_instance.to_dict()
# create an instance of ArrayOfVmfsDatastoreExpandSpec from a dict
array_of_vmfs_datastore_expand_spec_form_dict = array_of_vmfs_datastore_expand_spec.from_dict(array_of_vmfs_datastore_expand_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


