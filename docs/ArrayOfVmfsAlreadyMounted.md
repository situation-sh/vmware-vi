# ArrayOfVmfsAlreadyMounted

A boxed array of *VmfsAlreadyMounted*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmfsAlreadyMounted]**](VmfsAlreadyMounted.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vmfs_already_mounted import ArrayOfVmfsAlreadyMounted

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmfsAlreadyMounted from a JSON string
array_of_vmfs_already_mounted_instance = ArrayOfVmfsAlreadyMounted.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmfsAlreadyMounted.to_json()

# convert the object into a dict
array_of_vmfs_already_mounted_dict = array_of_vmfs_already_mounted_instance.to_dict()
# create an instance of ArrayOfVmfsAlreadyMounted from a dict
array_of_vmfs_already_mounted_form_dict = array_of_vmfs_already_mounted.from_dict(array_of_vmfs_already_mounted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


