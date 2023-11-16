# ArrayOfHostFirewallInfo

A boxed array of *HostFirewallInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFirewallInfo]**](HostFirewallInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_firewall_info import ArrayOfHostFirewallInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFirewallInfo from a JSON string
array_of_host_firewall_info_instance = ArrayOfHostFirewallInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFirewallInfo.to_json()

# convert the object into a dict
array_of_host_firewall_info_dict = array_of_host_firewall_info_instance.to_dict()
# create an instance of ArrayOfHostFirewallInfo from a dict
array_of_host_firewall_info_form_dict = array_of_host_firewall_info.from_dict(array_of_host_firewall_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


