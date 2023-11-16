# PhysicalNicIpHint

This data object type describes a network in network hint where the network is specified using IP addresses, for example, 10.27.49.1-10.27.49.254 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_subnet** | **str** | The network IP addresses.  | 

## Example

```python
from vmware_vi.models.physical_nic_ip_hint import PhysicalNicIpHint

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicIpHint from a JSON string
physical_nic_ip_hint_instance = PhysicalNicIpHint.from_json(json)
# print the JSON string representation of the object
print PhysicalNicIpHint.to_json()

# convert the object into a dict
physical_nic_ip_hint_dict = physical_nic_ip_hint_instance.to_dict()
# create an instance of PhysicalNicIpHint from a dict
physical_nic_ip_hint_form_dict = physical_nic_ip_hint.from_dict(physical_nic_ip_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


