# ArrayOfVmfsDatastoreCreateSpec

A boxed array of *VmfsDatastoreCreateSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsDatastoreCreateSpec]**](VmfsDatastoreCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_datastore_create_spec import ArrayOfVmfsDatastoreCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsDatastoreCreateSpec from a JSON string
array_of_vmfs_datastore_create_spec_instance = ArrayOfVmfsDatastoreCreateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsDatastoreCreateSpec.to_json()

# convert the object into a dict
array_of_vmfs_datastore_create_spec_dict = array_of_vmfs_datastore_create_spec_instance.to_dict()
# create an instance of ArrayOfVmfsDatastoreCreateSpec from a dict
array_of_vmfs_datastore_create_spec_form_dict = array_of_vmfs_datastore_create_spec.from_dict(array_of_vmfs_datastore_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


