# ArrayOfHostNvmeOpaqueTransportParameters

A boxed array of *HostNvmeOpaqueTransportParameters*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeOpaqueTransportParameters]**](HostNvmeOpaqueTransportParameters.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_opaque_transport_parameters import ArrayOfHostNvmeOpaqueTransportParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeOpaqueTransportParameters from a JSON string
array_of_host_nvme_opaque_transport_parameters_instance = ArrayOfHostNvmeOpaqueTransportParameters.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeOpaqueTransportParameters.to_json()

# convert the object into a dict
array_of_host_nvme_opaque_transport_parameters_dict = array_of_host_nvme_opaque_transport_parameters_instance.to_dict()
# create an instance of ArrayOfHostNvmeOpaqueTransportParameters from a dict
array_of_host_nvme_opaque_transport_parameters_form_dict = array_of_host_nvme_opaque_transport_parameters.from_dict(array_of_host_nvme_opaque_transport_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


