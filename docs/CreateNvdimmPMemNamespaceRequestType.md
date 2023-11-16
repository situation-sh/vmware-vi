# CreateNvdimmPMemNamespaceRequestType

The parameters of *HostNvdimmSystem.CreateNvdimmPMemNamespace_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_spec** | [**NvdimmPMemNamespaceCreateSpec**](NvdimmPMemNamespaceCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_nvdimm_p_mem_namespace_request_type import CreateNvdimmPMemNamespaceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNvdimmPMemNamespaceRequestType from a JSON string
create_nvdimm_p_mem_namespace_request_type_instance = CreateNvdimmPMemNamespaceRequestType.from_json(json)
# print the JSON string representation of the object
print CreateNvdimmPMemNamespaceRequestType.to_json()

# convert the object into a dict
create_nvdimm_p_mem_namespace_request_type_dict = create_nvdimm_p_mem_namespace_request_type_instance.to_dict()
# create an instance of CreateNvdimmPMemNamespaceRequestType from a dict
create_nvdimm_p_mem_namespace_request_type_form_dict = create_nvdimm_p_mem_namespace_request_type.from_dict(create_nvdimm_p_mem_namespace_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


