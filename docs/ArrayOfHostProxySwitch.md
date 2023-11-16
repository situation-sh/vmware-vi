# ArrayOfHostProxySwitch

A boxed array of *HostProxySwitch*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProxySwitch]**](HostProxySwitch.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_proxy_switch import ArrayOfHostProxySwitch

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProxySwitch from a JSON string
array_of_host_proxy_switch_instance = ArrayOfHostProxySwitch.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProxySwitch.to_json()

# convert the object into a dict
array_of_host_proxy_switch_dict = array_of_host_proxy_switch_instance.to_dict()
# create an instance of ArrayOfHostProxySwitch from a dict
array_of_host_proxy_switch_form_dict = array_of_host_proxy_switch.from_dict(array_of_host_proxy_switch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


