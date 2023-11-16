# ArrayOfHostNvmeOverRdmaParameters

A boxed array of *HostNvmeOverRdmaParameters*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeOverRdmaParameters]**](HostNvmeOverRdmaParameters.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_over_rdma_parameters import ArrayOfHostNvmeOverRdmaParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeOverRdmaParameters from a JSON string
array_of_host_nvme_over_rdma_parameters_instance = ArrayOfHostNvmeOverRdmaParameters.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeOverRdmaParameters.to_json()

# convert the object into a dict
array_of_host_nvme_over_rdma_parameters_dict = array_of_host_nvme_over_rdma_parameters_instance.to_dict()
# create an instance of ArrayOfHostNvmeOverRdmaParameters from a dict
array_of_host_nvme_over_rdma_parameters_form_dict = array_of_host_nvme_over_rdma_parameters.from_dict(array_of_host_nvme_over_rdma_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


