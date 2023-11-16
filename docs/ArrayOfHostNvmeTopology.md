# ArrayOfHostNvmeTopology

A boxed array of *HostNvmeTopology*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeTopology]**](HostNvmeTopology.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_topology import ArrayOfHostNvmeTopology

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeTopology from a JSON string
array_of_host_nvme_topology_instance = ArrayOfHostNvmeTopology.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeTopology.to_json()

# convert the object into a dict
array_of_host_nvme_topology_dict = array_of_host_nvme_topology_instance.to_dict()
# create an instance of ArrayOfHostNvmeTopology from a dict
array_of_host_nvme_topology_form_dict = array_of_host_nvme_topology.from_dict(array_of_host_nvme_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


