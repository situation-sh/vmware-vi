# ArrayOfHostNvmeSpec

A boxed array of *HostNvmeSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeSpec]**](HostNvmeSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_spec import ArrayOfHostNvmeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeSpec from a JSON string
array_of_host_nvme_spec_instance = ArrayOfHostNvmeSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeSpec.to_json()

# convert the object into a dict
array_of_host_nvme_spec_dict = array_of_host_nvme_spec_instance.to_dict()
# create an instance of ArrayOfHostNvmeSpec from a dict
array_of_host_nvme_spec_form_dict = array_of_host_nvme_spec.from_dict(array_of_host_nvme_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


