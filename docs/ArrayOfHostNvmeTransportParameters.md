# ArrayOfHostNvmeTransportParameters

A boxed array of *HostNvmeTransportParameters*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeTransportParameters]**](HostNvmeTransportParameters.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_transport_parameters import ArrayOfHostNvmeTransportParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeTransportParameters from a JSON string
array_of_host_nvme_transport_parameters_instance = ArrayOfHostNvmeTransportParameters.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeTransportParameters.to_json()

# convert the object into a dict
array_of_host_nvme_transport_parameters_dict = array_of_host_nvme_transport_parameters_instance.to_dict()
# create an instance of ArrayOfHostNvmeTransportParameters from a dict
array_of_host_nvme_transport_parameters_form_dict = array_of_host_nvme_transport_parameters.from_dict(array_of_host_nvme_transport_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


