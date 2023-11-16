# NvdimmNamespaceDeleteSpec

Arguments for deleting a namespace  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Universally unique identifier of the namespace to be deleted  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.nvdimm_namespace_delete_spec import NvdimmNamespaceDeleteSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NvdimmNamespaceDeleteSpec from a JSON string
nvdimm_namespace_delete_spec_instance = NvdimmNamespaceDeleteSpec.from_json(json)
# print the JSON string representation of the object
print NvdimmNamespaceDeleteSpec.to_json()

# convert the object into a dict
nvdimm_namespace_delete_spec_dict = nvdimm_namespace_delete_spec_instance.to_dict()
# create an instance of NvdimmNamespaceDeleteSpec from a dict
nvdimm_namespace_delete_spec_form_dict = nvdimm_namespace_delete_spec.from_dict(nvdimm_namespace_delete_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


