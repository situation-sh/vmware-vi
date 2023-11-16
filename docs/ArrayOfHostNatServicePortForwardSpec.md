# ArrayOfHostNatServicePortForwardSpec

A boxed array of *HostNatServicePortForwardSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNatServicePortForwardSpec]**](HostNatServicePortForwardSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nat_service_port_forward_spec import ArrayOfHostNatServicePortForwardSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNatServicePortForwardSpec from a JSON string
array_of_host_nat_service_port_forward_spec_instance = ArrayOfHostNatServicePortForwardSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNatServicePortForwardSpec.to_json()

# convert the object into a dict
array_of_host_nat_service_port_forward_spec_dict = array_of_host_nat_service_port_forward_spec_instance.to_dict()
# create an instance of ArrayOfHostNatServicePortForwardSpec from a dict
array_of_host_nat_service_port_forward_spec_form_dict = array_of_host_nat_service_port_forward_spec.from_dict(array_of_host_nat_service_port_forward_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


