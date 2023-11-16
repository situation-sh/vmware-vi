# ArrayOfHostNvmeOverFibreChannelParameters

A boxed array of *HostNvmeOverFibreChannelParameters*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeOverFibreChannelParameters]**](HostNvmeOverFibreChannelParameters.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_over_fibre_channel_parameters import ArrayOfHostNvmeOverFibreChannelParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeOverFibreChannelParameters from a JSON string
array_of_host_nvme_over_fibre_channel_parameters_instance = ArrayOfHostNvmeOverFibreChannelParameters.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeOverFibreChannelParameters.to_json()

# convert the object into a dict
array_of_host_nvme_over_fibre_channel_parameters_dict = array_of_host_nvme_over_fibre_channel_parameters_instance.to_dict()
# create an instance of ArrayOfHostNvmeOverFibreChannelParameters from a dict
array_of_host_nvme_over_fibre_channel_parameters_form_dict = array_of_host_nvme_over_fibre_channel_parameters.from_dict(array_of_host_nvme_over_fibre_channel_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


