# ArrayOfHostDnsConfigSpec

A boxed array of *HostDnsConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDnsConfigSpec]**](HostDnsConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_dns_config_spec import ArrayOfHostDnsConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDnsConfigSpec from a JSON string
array_of_host_dns_config_spec_instance = ArrayOfHostDnsConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDnsConfigSpec.to_json()

# convert the object into a dict
array_of_host_dns_config_spec_dict = array_of_host_dns_config_spec_instance.to_dict()
# create an instance of ArrayOfHostDnsConfigSpec from a dict
array_of_host_dns_config_spec_form_dict = array_of_host_dns_config_spec.from_dict(array_of_host_dns_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


