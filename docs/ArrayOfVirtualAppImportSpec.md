# ArrayOfVirtualAppImportSpec

A boxed array of *VirtualAppImportSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualAppImportSpec]**](VirtualAppImportSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_app_import_spec import ArrayOfVirtualAppImportSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualAppImportSpec from a JSON string
array_of_virtual_app_import_spec_instance = ArrayOfVirtualAppImportSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualAppImportSpec.to_json()

# convert the object into a dict
array_of_virtual_app_import_spec_dict = array_of_virtual_app_import_spec_instance.to_dict()
# create an instance of ArrayOfVirtualAppImportSpec from a dict
array_of_virtual_app_import_spec_form_dict = array_of_virtual_app_import_spec.from_dict(array_of_virtual_app_import_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


